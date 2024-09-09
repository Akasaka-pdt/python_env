import streamlit as st
import io
import contextlib

# タイトル
st.title("Pythonコード実行アプリ")

# テキストエリアにPythonコードを入力
code = st.text_area("ここにPythonコードを入力してください:")

# サイドバーに標準入��の数を指定するフィールドを配置
num_inputs = st.sidebar.number_input("標準入力の数を指定してください:", min_value=1, max_value=10, value=1)

# サイドバーに複数の標準入力フィールドを配置
inputs = []
for i in range(num_inputs):
    user_input = st.sidebar.text_input(f"標準入力 {i+1}:", key=f"input_{i}")
    inputs.append(user_input)

# 実行ボタン
if st.button("実行"):
    # 標準出力をキャプチャするためのStringIOオブジェクトを作成
    output = io.StringIO()
    
    # 標準入力をキャプチャするための関数を定義
    input_counter = iter(inputs)
    def mock_input(prompt=''):
        return next(input_counter)
    
    # 標準入力をモックするためにbuiltins.inputを置き換える
    import builtins
    original_input = builtins.input
    builtins.input = mock_input
    
    # 標準出力をキャプチャ
    with contextlib.redirect_stdout(output):
        try:
            # 入力されたコードを実行
            exec(code)
        except Exception as e:
            # エラーが発生した場合はエラーメッセージを表示
            st.error(f"エラーが発生しました: {e}")
    
    # builtins.inputを元に戻す
    builtins.input = original_input
    
    # キャプチャした標準出力を表示
    st.text("実行結果:")
    st.text(output.getvalue())