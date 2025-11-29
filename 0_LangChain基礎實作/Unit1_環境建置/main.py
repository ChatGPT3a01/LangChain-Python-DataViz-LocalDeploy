# Unit 1: LangChain 環境建置與基礎
# 本程式示範如何設定 LangChain 環境並進行基本對話

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# 載入環境變數
load_dotenv()

def main():
    print("=" * 50)
    print("Unit 1: LangChain 環境建置與基礎")
    print("=" * 50)

    # 建立 ChatOpenAI 實例
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    )

    # 方法一：簡單字串呼叫
    print("\n[方法一] 簡單字串呼叫:")
    response = llm.invoke("請用一句話介紹 Python")
    print(f"回應: {response.content}")

    # 方法二：使用訊息物件
    print("\n[方法二] 使用訊息物件:")
    messages = [
        SystemMessage(content="你是一位熱心的程式教學助教"),
        HumanMessage(content="什麼是 LangChain？")
    ]
    response = llm.invoke(messages)
    print(f"回應: {response.content}")

    # 方法三：調整參數
    print("\n[方法三] 調整 temperature 參數:")

    # 低溫度 - 較為確定的回答
    llm_low = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    response_low = llm_low.invoke("1+1=?")
    print(f"低溫度 (0): {response_low.content}")

    # 高溫度 - 較為創意的回答
    llm_high = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)
    response_high = llm_high.invoke("寫一句有趣的開場白")
    print(f"高溫度 (1): {response_high.content}")

    print("\n" + "=" * 50)
    print("環境建置完成！LangChain 運作正常")
    print("=" * 50)

if __name__ == "__main__":
    main()
