from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition, ToolNode
from agent_tools import decryption, encryption
from utils.context_manager import init_context
import os
import asyncio
from contextlib import asynccontextmanager
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv

load_dotenv()


# Make the graph with MCP context
@asynccontextmanager
async def make_graph():
    mcp_client = MultiServerMCPClient(
        {
            "add-one": {
                # make sure you start your weather server on port 8000
                "url": f"http://localhost:{os.getenv('MCP_SERVER_PORT')}/sse",
                "transport": "sse",
            }
        }
    )

    #Nodes
    def assistant(state: MessagesState):
        system_message = SystemMessage(content="You are a helpful agent who helps user encrypt and decrypt data using its tools of homomophic encryption.")
        return {"messages":[llm.invoke([system_message] + state["messages"])]}

    async with mcp_client:
        init_context()
        mcp_tools = mcp_client.get_tools()
        print(f"Available tools: {[tool.name for tool in mcp_tools]}")
        llm = ChatOpenAI(model="gpt-4o-mini")
        local_tools = [encryption.list_encryption, decryption.list_decryption]
        tools = mcp_tools + local_tools
        llm = llm.bind_tools(tools)

        #Graph
        builder = StateGraph(MessagesState)

        # Adding Nodes
        builder.add_node("assistant",assistant)
        builder.add_node("tools", ToolNode(tools))

        # Adding Edges
        builder.add_edge(START, "assistant")
        builder.add_conditional_edges("assistant", tools_condition)
        builder.add_edge("tools", "assistant")

        # Compiling graph
        react_graph = builder.compile()
        react_graph.name = "Tool Agent"
        yield react_graph

# Run the graph with question
async def main():
    async with make_graph() as graph:
        
        """
        Can you encrypt this list of numbers [1,3,56] using your tools and stored it in a file
        Can you decrypt the list of encrypted numbers using your tools which are stored in the file `data/encrypted_data.txt`
        """
        # Agent
        messages = [HumanMessage(content="Can you add_one to the list of encrypted numbers stored in the file `data/encrypted_data.txt` using your tools and stored it in a file")]
        messages = await graph.ainvoke({"messages":messages})

        for m in messages['messages']:
            m.pretty_print()
asyncio.run(main())