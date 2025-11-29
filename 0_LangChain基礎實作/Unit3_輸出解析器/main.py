# Unit 3: LangChain 輸出解析器
# 本程式示範各種 Output Parser 的使用方式

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

# 載入環境變數
load_dotenv()

# 定義 Pydantic 模型
class Restaurant(BaseModel):
    name: str = Field(description="餐廳名稱")
    cuisine: str = Field(description="料理類型")
    price_range: str = Field(description="價格範圍")
    rating: float = Field(description="評分 1-5")
    features: List[str] = Field(description="特色標籤")

class MovieReview(BaseModel):
    title: str = Field(description="電影名稱")
    rating: int = Field(description="評分 1-10")
    pros: List[str] = Field(description="優點列表")
    cons: List[str] = Field(description="缺點列表")
    recommendation: str = Field(description="推薦程度：強烈推薦/推薦/普通/不推薦")

def main():
    print("=" * 50)
    print("Unit 3: LangChain 輸出解析器")
    print("=" * 50)

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # ===== StrOutputParser =====
    print("\n[1] StrOutputParser - 字串輸出:")

    str_prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一位詩人，請用優美的文字回答"),
        ("human", "請描述 {season}")
    ])

    str_chain = str_prompt | llm | StrOutputParser()
    result = str_chain.invoke({"season": "秋天"})
    print(f"結果類型: {type(result)}")
    print(f"內容: {result}")

    # ===== JsonOutputParser =====
    print("\n[2] JsonOutputParser - JSON 輸出:")

    json_prompt = ChatPromptTemplate.from_messages([
        ("system", """分析以下城市並輸出 JSON 格式：
{{"city": "城市名", "country": "國家", "population": "人口數", "famous_for": ["特色1", "特色2"]}}"""),
        ("human", "分析城市：{city}")
    ])

    json_parser = JsonOutputParser()
    json_chain = json_prompt | llm | json_parser

    result = json_chain.invoke({"city": "台北"})
    print(f"結果類型: {type(result)}")
    print(f"內容: {result}")
    print(f"取得城市: {result.get('city')}")

    # ===== PydanticOutputParser =====
    print("\n[3] PydanticOutputParser - 結構化輸出:")

    from langchain.output_parsers import PydanticOutputParser

    restaurant_parser = PydanticOutputParser(pydantic_object=Restaurant)

    restaurant_prompt = ChatPromptTemplate.from_messages([
        ("system", """你是美食評論家。請分析餐廳並輸出指定格式。
{format_instructions}"""),
        ("human", "請推薦一間台北的 {cuisine} 餐廳")
    ])

    restaurant_chain = restaurant_prompt | llm | restaurant_parser

    result = restaurant_chain.invoke({
        "cuisine": "日式料理",
        "format_instructions": restaurant_parser.get_format_instructions()
    })

    print(f"結果類型: {type(result)}")
    print(f"餐廳名稱: {result.name}")
    print(f"料理類型: {result.cuisine}")
    print(f"價格範圍: {result.price_range}")
    print(f"評分: {result.rating}")
    print(f"特色: {result.features}")

    # ===== 電影評論範例 =====
    print("\n[4] 實用範例 - 電影評論解析:")

    movie_parser = PydanticOutputParser(pydantic_object=MovieReview)

    movie_prompt = ChatPromptTemplate.from_messages([
        ("system", """你是專業影評人。請分析電影並輸出評論。
{format_instructions}"""),
        ("human", "請評論電影：{movie}")
    ])

    movie_chain = movie_prompt | llm | movie_parser

    result = movie_chain.invoke({
        "movie": "乘風破浪",
        "format_instructions": movie_parser.get_format_instructions()
    })

    print(f"電影: {result.title}")
    print(f"評分: {result.rating}/10")
    print(f"優點: {', '.join(result.pros)}")
    print(f"缺點: {', '.join(result.cons)}")
    print(f"推薦: {result.recommendation}")

    # ===== 批次處理範例 =====
    print("\n[5] 批次處理多個項目:")

    cities = ["東京", "紐約", "巴黎"]

    for city in cities:
        result = json_chain.invoke({"city": city})
        print(f"\n{city}: {result.get('famous_for', [])}")

    print("\n" + "=" * 50)
    print("輸出解析器範例完成！")
    print("=" * 50)

if __name__ == "__main__":
    main()
