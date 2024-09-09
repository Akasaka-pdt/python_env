import streamlit as st
import io
import contextlib


st.title("Pythonコード実行アプリ")

code = st.text_area("ここにPythonコードを入力してください:", placeholder="ここにPythonコードを入力してください。右下をドラッグすると、枠の縦幅を変えることができます。")

num_inputs = st.sidebar.number_input("標準入力の数を指定してください:", min_value=1, max_value=10, value=1)


inputs = []
for i in range(num_inputs):
    user_input = st.sidebar.text_input(f"標準入力 {i+1}:", key=f"input_{i}")
    inputs.append(user_input)

if st.button("実行"):
    with st.spinner('実行中...'):
        output = io.StringIO()
        
        input_counter = iter(inputs)
        def mock_input(prompt=''):
            return next(input_counter)
        
        import builtins
        original_input = builtins.input
        builtins.input = mock_input
        
        with contextlib.redirect_stdout(output):
            try:
                exec(code)
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
        
        builtins.input = original_input
        
        st.text("実行結果:")
        st.text(output.getvalue())
