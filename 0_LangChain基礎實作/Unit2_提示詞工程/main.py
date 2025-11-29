# Unit 2: LangChain 提示詞工程
# 本程式示範 PromptTemplate 和 ChatPromptTemplate 的使用方式

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

# 載入環境變數
load_dotenv()

def main():
    print("=" * 50)
    print("Unit 2: LangChain 提示詞工程")
    print("=" * 50)

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # ===== 基礎 PromptTemplate =====
    print("\n[1] 基礎 PromptTemplate:")

    simple_prompt = PromptTemplate.from_template(
        "請用繁體中文簡單介紹 {topic}"
    )

    formatted = simple_prompt.format(topic="機器學習")
    print(f"格式化後: {formatted}")

    response = llm.invoke(formatted)
    print(f"回應: {response.content[:100]}...")

    # ===== 多變數 PromptTemplate =====
    print("\n[2] 多變數 PromptTemplate:")

    multi_prompt = PromptTemplate(
        input_variables=["product", "audience", "tone"],
        template="請為 {product} 撰寫一段廣告文案，目標對象是 {audience}，語氣要 {tone}"
    )

    formatted = multi_prompt.format(
        product="智慧手錶",
        audience="年輕上班族",
        tone="活潑有趣"
    )
    print(f"格式化後: {formatted}")

    response = llm.invoke(formatted)
    print(f"回應: {response.content}")

    # ===== ChatPromptTemplate =====
    print("\n[3] ChatPromptTemplate (角色扮演):")

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一位專業的 {role}，請用專業但易懂的方式回答問題"),
        ("human", "{question}")
    ])

    messages = chat_prompt.format_messages(
        role="營養師",
        question="每天應該喝多少水？"
    )

    print(f"訊息列表: {messages}")

    response = llm.invoke(messages)
    print(f"回應: {response.content}")

    # ===== 進階：多輪對話模板 =====
    print("\n[4] 多輪對話模板:")

    conversation_prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一位友善的 {language} 語言老師"),
        ("human", "我想學習 {language}"),
        ("ai", "太好了！讓我們從基礎開始。你有什麼程度呢？"),
        ("human", "{user_input}")
    ])

    messages = conversation_prompt.format_messages(
        language="日文",
        user_input="我是完全的初學者"
    )

    response = llm.invoke(messages)
    print(f"回應: {response.content}")

    # ===== 實用範例：翻譯助手 =====
    print("\n[5] 實用範例 - 翻譯助手:")

    translator_prompt = ChatPromptTemplate.from_messages([
        ("system", """你是專業翻譯員。
請將以下文字翻譯成 {target_language}。
要求：
- 保持原文語意
- 使用自然流暢的表達
- 專有名詞可保留原文"""),
        ("human", "{text}")
    ])

    messages = translator_prompt.format_messages(
        target_language="英文",
        text="人工智慧正在改變我們的生活方式"
    )

    response = llm.invoke(messages)
    print(f"翻譯結果: {response.content}")

    print("\n" + "=" * 50)
    print("提示詞工程範例完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()
