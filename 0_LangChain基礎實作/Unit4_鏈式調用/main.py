# Unit 4: LangChain 鏈式調用 (LCEL)
# 本程式示範 LangChain Expression Language 的各種用法

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

# 載入環境變數
load_dotenv()

def main():
    print("=" * 50)
    print("Unit 4: LangChain 鏈式調用 (LCEL)")
    print("=" * 50)

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # ===== 基礎鏈 =====
    print("\n[1] 基礎鏈: Prompt -> LLM -> Parser")

    basic_prompt = ChatPromptTemplate.from_template(
        "請用一句話解釋 {concept}"
    )

    basic_chain = basic_prompt | llm | StrOutputParser()

    result = basic_chain.invoke({"concept": "人工智慧"})
    print(f"結果: {result}")

    # ===== 多步驟鏈 =====
    print("\n[2] 多步驟鏈: 翻譯 -> 摘要")

    # 第一步：翻譯
    translate_prompt = ChatPromptTemplate.from_template(
        "將以下文字翻譯成英文：\n{text}"
    )
    translate_chain = translate_prompt | llm | StrOutputParser()

    # 第二步：摘要
    summary_prompt = ChatPromptTemplate.from_template(
        "請用一句話摘要以下英文內容：\n{english_text}"
    )
    summary_chain = summary_prompt | llm | StrOutputParser()

    # 組合鏈
    def process_translation(inputs):
        translated = translate_chain.invoke({"text": inputs["text"]})
        summary = summary_chain.invoke({"english_text": translated})
        return {"translated": translated, "summary": summary}

    text = "深度學習是機器學習的一個分支，使用多層神經網路來學習數據的特徵表示"
    result = process_translation({"text": text})
    print(f"原文: {text}")
    print(f"翻譯: {result['translated']}")
    print(f"摘要: {result['summary']}")

    # ===== RunnablePassthrough =====
    print("\n[3] RunnablePassthrough - 傳遞原始輸入")

    analysis_prompt = ChatPromptTemplate.from_template(
        "分析這個主題的重要性：{topic}\n請提供3個要點"
    )

    chain_with_passthrough = (
        {"topic": RunnablePassthrough()}
        | analysis_prompt
        | llm
        | StrOutputParser()
    )

    result = chain_with_passthrough.invoke("氣候變遷")
    print(f"分析結果:\n{result}")

    # ===== RunnableLambda - 自定義處理 =====
    print("\n[4] RunnableLambda - 自定義處理函數")

    def add_context(text):
        return f"[台灣視角] {text}"

    def format_output(text):
        return f"{'='*40}\n{text}\n{'='*40}"

    custom_chain = (
        RunnableLambda(add_context)
        | ChatPromptTemplate.from_template("請評論：{text}")
        | llm
        | StrOutputParser()
        | RunnableLambda(format_output)
    )

    # 修正：直接傳入字串給 RunnableLambda
    result = custom_chain.invoke("半導體產業發展")
    print(result)

    # ===== 平行處理 =====
    print("\n[5] 平行處理多個任務")

    from langchain_core.runnables import RunnableParallel

    positive_prompt = ChatPromptTemplate.from_template(
        "列出 {topic} 的3個優點"
    )
    negative_prompt = ChatPromptTemplate.from_template(
        "列出 {topic} 的3個缺點"
    )

    parallel_chain = RunnableParallel(
        pros=positive_prompt | llm | StrOutputParser(),
        cons=negative_prompt | llm | StrOutputParser()
    )

    result = parallel_chain.invoke({"topic": "遠距工作"})
    print(f"優點:\n{result['pros']}")
    print(f"\n缺點:\n{result['cons']}")

    # ===== 實用範例：內容產生器 =====
    print("\n[6] 實用範例 - 部落格文章產生器")

    # 標題產生
    title_prompt = ChatPromptTemplate.from_template(
        "為關於 {topic} 的部落格文章想一個吸引人的標題"
    )

    # 大綱產生
    outline_prompt = ChatPromptTemplate.from_template(
        "為標題「{title}」的文章列出3個主要段落標題"
    )

    # 組合
    title_chain = title_prompt | llm | StrOutputParser()

    def create_article_structure(topic):
        title = title_chain.invoke({"topic": topic})
        outline = (outline_prompt | llm | StrOutputParser()).invoke({"title": title})
        return {
            "topic": topic,
            "title": title,
            "outline": outline
        }

    blog_chain = RunnableLambda(create_article_structure)

    result = blog_chain.invoke("Python 學習技巧")
    print(f"主題: {result['topic']}")
    print(f"標題: {result['title']}")
    print(f"大綱:\n{result['outline']}")

    # ===== 條件分支 =====
    print("\n[7] 條件分支處理")

    def route_by_length(text):
        if len(text) < 20:
            return "short"
        else:
            return "long"

    short_prompt = ChatPromptTemplate.from_template(
        "這是簡短文字，請擴充說明：{text}"
    )
    long_prompt = ChatPromptTemplate.from_template(
        "這是較長文字，請摘要重點：{text}"
    )

    def conditional_process(text):
        route = route_by_length(text)
        if route == "short":
            return (short_prompt | llm | StrOutputParser()).invoke({"text": text})
        else:
            return (long_prompt | llm | StrOutputParser()).invoke({"text": text})

    short_text = "AI 很重要"
    long_text = "人工智慧是計算機科學的一個分支，旨在創建能夠執行通常需要人類智慧的任務的系統，包括學習、推理、問題解決和語言理解"

    print(f"短文字處理: {conditional_process(short_text)[:100]}...")
    print(f"長文字處理: {conditional_process(long_text)[:100]}...")

    print("\n" + "=" * 50)
    print("鏈式調用範例完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()
