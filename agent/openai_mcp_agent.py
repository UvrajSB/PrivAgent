from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition, ToolNode
from agent_tools import decryption, encryption, decrypt_interest_results
from utils.context_manager import init_context
import os
import asyncio
from contextlib import asynccontextmanager
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv


load_dotenv()

@asynccontextmanager
async def make_graph():
    mcp_client = MultiServerMCPClient(
        {
            "add-one": {
                "url": f"http://localhost:{os.getenv('MCP_SERVER_PORT')}/sse",
                "transport": "sse",
            }
        }
    )

    #Nodes
    async def assistant(state: MessagesState):
        system_message = SystemMessage(content="You are a helpful agent who helps user encrypt and decrypt data using its tools of homomophic encryption.")
        result = await llm.ainvoke([system_message] + state["messages"])
        return {"messages": [result]}


    async with mcp_client:
        init_context()
        mcp_tools = mcp_client.get_tools()
        print(f"Available tools: {[tool.name for tool in mcp_tools]}")
        llm = ChatOpenAI(model="gpt-4o-mini")
        local_tools = [encryption.list_encryption, decryption.list_decryption, decrypt_interest_results.decrypt_interest_results]
        tools = mcp_tools + local_tools
        print(f"Available tools: {[tool.name for tool in mcp_tools]}")
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
        enc_prompt = "Can you encrypt this list of numbers [1,9,2] using your tools and stored it in a file"
        dec_prompt = "Can you decrypt the list of encrypted numbers using your tools which are stored in the file `data/encrypted_data.txt`"
        mcp_prompt = "Match my encrypted interest vector against available movie profiles and store the similarity scores and tell me the name of the file"
        decrypt_results_prompt = "Can you decrypt and tell me the results stored in data/interest_results using your tools "

        # Agent
        # messages = [HumanMessage(content=enc_prompt)]
        # messages = await graph.ainvoke({"messages":messages})
        
        # messages = [HumanMessage(content=dec_prompt)]
        # messages = await graph.ainvoke({"messages":messages})
        
        # messages = [HumanMessage(content=mcp_prompt)]
        # messages = await graph.ainvoke({"messages":messages})
        
        messages = [HumanMessage(content=decrypt_results_prompt)]
        messages = await graph.ainvoke({"messages":messages})

        for m in messages['messages']:
            m.pretty_print()
asyncio.run(main())