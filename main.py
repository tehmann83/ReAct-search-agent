# main.py

from dotenv import load_dotenv

load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4")
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt=react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor


def main():
    print("Hello, react-search-agent!")

    result = chain.invoke(
        input={
            "input": "Search for 3 recently posted job postings for an AI Engineer/Full Stack Developer in Valencia, Spain on linkedin and list their details."
        }
    )

    print(result)


if __name__ == "__main__":
    main()
