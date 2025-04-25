import os
import asyncio
import json

from mcp import ClientSession, StdioServerParameters
from langchain_mcp_adapters.client import MultiServerMCPClient
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

base_dir = os.path.dirname(os.path.realpath(__file__))
openai_key = "..."
os.environ["OPENAI_API_KEY"] = openai_key
model = ChatOpenAI(model="gpt-4o")

async def run_multi(question: str):
    async with MultiServerMCPClient(
        {
            "gmail": {
                "command": "npx",
                "args": [
                    "-y",
                    "@gongrzhe/server-gmail-autoauth-mcp"
                ],
                "env": {
                    "GMAIL_CREDENTIALS_PATH": os.path.join(base_dir, "credentials.json")
                }
            },
            "filesystem": {
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    os.path.join(base_dir, "files")
                ]
            }
        }
    ) as client:
        messages = [
            SystemMessage(
                content="You are a precise and efficient assistant that helps users by opening documents, summarizing their content in a concise and clear way, and preparing summaries to be sent via email. Always use a professional and neutral tone in your summaries. If the file is too long or complex, prioritize the most important points and key sections. Do not include sensitive or private information unless explicitly requested. If the user doesn't provide the recipient email, don't send anything and respond with asking the user to also supply recipient email in the prompt. Only look for files within the allowed directory, so that users don't need to provide the full path of the file."
            ),
            HumanMessage(
                content=question
            )
        ]
        agent = create_react_agent(model, client.get_tools())
        agent_response = await agent.ainvoke({"messages": messages})
        return agent_response


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    resp = asyncio.run(run_multi(prompt))
    for msg in resp["messages"]:
        if isinstance(msg, AIMessage):
            print(msg.content)