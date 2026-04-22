import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from client import get_mcp_client


async def main():
    load_dotenv()

    client = get_mcp_client()
    tools = await client.get_tools()

    llm = ChatOpenAI(model="gpt-4o-mini")

    agent = create_react_agent(llm, tools)

    query = input("Enter your question: ")

    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": query}]}
    )

    print("\nFinal Answer:\n")
    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
