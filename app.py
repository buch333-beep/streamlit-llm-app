import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

# LLM呼び出し関数
def get_llm_response(user_input, expert_type):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    if expert_type == "キャリアコンサルタント":
        system_prompt = "あなたは優秀なキャリアコンサルタントです。論理的かつ実践的にアドバイスしてください。"
    else:
        system_prompt = "あなたは共感力の高い心理カウンセラーです。優しく寄り添う形で回答してください。"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)
    return response.content


# Streamlit UI
st.title("専門家に相談できるLLMアプリ")

st.write("""
このアプリでは、選択した専門家になりきったAIがあなたの相談に回答します。
専門家を選び、質問を入力してください。
""")

expert = st.radio(
    "専門家を選択してください",
    ("キャリアコンサルタント", "心理カウンセラー")
)

user_input = st.text_area("相談内容を入力してください")

if st.button("送信"):
    if user_input:
        answer = get_llm_response(user_input, expert)
        st.subheader("回答")
        st.write(answer)
    else:
        st.warning("相談内容を入力してください。")