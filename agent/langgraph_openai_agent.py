from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition, ToolNode
from agent_tools import add, decryption, encryption
from utils.context_manager import init_context

init_context()

llm = ChatOpenAI(model="gpt-4o-mini")

system_message = SystemMessage(content="You are a helpful agent who helps user encrypt and decrypt data using its tools of homomophic encryption.")

#Nodes
def assistant(state: MessagesState):
    return {"messages":[llm.invoke([system_message] + state["messages"])]}

tools = [encryption.list_encryption, decryption.list_decryption]

llm = llm.bind_tools(tools, parallel_tool_calls=False)
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

# Agent
messages = [HumanMessage(content="Can you decrypt the list of encrypted numbers using your tools which are stored in encrypted_data/encrypted_vector.txt")]
messages = react_graph.invoke({"messages":messages})

for m in messages['messages']:
    m.pretty_print()