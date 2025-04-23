# 🔐 Encrypted Health Insights Agent

This project demonstrates how **on-device LLM agents** can collaborate with a remote **MCP (Model Computation & Processing) server** to analyze **homomorphically encrypted health data**, enabling powerful AI-driven insights without compromising user privacy.

---

## 💡 What It Does

- You interact with an AI agent via a chat interface.
- The agent **encrypts your health vitals** (like heart rate readings) directly on your device.
- It sends the **encrypted data** to a remote **MCP server**.
- The MCP server performs analysis (e.g., calculates average heart rate, detects trends) **without ever decrypting the data**.
- The encrypted result is returned to the agent, who **decrypts it locally** and gives you a natural-language insight.

At no point is your sensitive data exposed to the server in plaintext.

---

## 🧠 Why This Matters

In traditional systems, data must be shared with the cloud or third-party services for analysis — putting user privacy at risk.

In this system:
- Data remains encrypted at rest, in transit, and during computation.
- The **MCP server** can perform computations directly on encrypted data using **homomorphic encryption** (HE).
- Only your device can decrypt the result — ensuring full privacy.

---

## 🛠️ Technical Architecture

### Components

1. **Agent System**
   - Multiple agent implementations available:
     - OpenAI-based agent (`openai_agent.py`)
     - Ollama-based agent (`ollama_agent.py`)
   - Uses LangChain and LangGraph for agent orchestration
   - Supports both synchronous and asynchronous operations

2. **Encryption Layer**
   - Uses TenSEAL for homomorphic encryption
   - BFV scheme implementation for integer operations
   - Secure context management with serialization support
   - Tools for encryption/decryption operations

3. **MCP Server**
   - FastMCP implementation for secure computations
   - Supports Server-Sent Events (SSE) transport
   - Handles encrypted vector operations
   - Movie recommendation system as a demo use case

4. **Data Management**
   - Mock data generation for testing
   - Secure serialization/deserialization of encrypted vectors
   - File-based storage for encrypted data and results

---

## 🚀 Setup and Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd PrivRec
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**
   Create a `.env` file with:
   ```
   MCP_SERVER_PORT=<your-port>
   MCP_SERVER_LOG_LEVEL=INFO
   ```

4. **Initialize the Context**
   The system will automatically initialize the encryption context on first run.

---

## 🔧 Core Components

### Encryption Tools
```python
# Example of encrypting data
@tool
def list_encryption(l:list)-> str:
    context = get_context()
    return serialize_bfvvector(ts.bfv_tensor(context, l))
```

### MCP Server Operations
```python
# Example of secure computation
@mcp.tool()
def match_movies() -> str:
    # Performs computations on encrypted vectors
    # Returns encrypted similarity scores
```

### Agent Tools
- `encryption.py`: Handles data encryption
- `decryption.py`: Manages secure decryption
- `decrypt_interest_results.py`: Processes encrypted analysis results

---

## 🩺 Example Use Cases

1. **Health Data Analysis**
   - Secure heart rate trend analysis
   - Privacy-preserving vital signs monitoring
   - Encrypted health metrics comparison

2. **Recommendation System**
   - Encrypted user interest vectors
   - Secure movie matching
   - Privacy-preserving similarity scoring

---

## 🔐 Key Features

- ✅ **On-device agent with LLM reasoning**
- ✅ **Encryption and decryption using homomorphic encryption (BFV via TenSEAL)**
- ✅ **MCP server that performs computations without access to raw data**
- ✅ **Streamlit-based user interface**
- ✅ **Privacy-preserving by design**
- ✅ **Multiple LLM backend support (OpenAI, Ollama)**
- ✅ **Asynchronous operation support**
- ✅ **Modular and extensible architecture**

---

## 🌐 Vision

This prototype is a step toward building **confidential AI systems**, where sensitive data can be intelligently analyzed without ever being exposed. The collaboration between on-device agents and an encrypted computation server (**MCP**) shows how we can move toward **trustless, privacy-first AI architectures** in healthcare and beyond.

---

## 📝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
