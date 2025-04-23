# 🔐 Privacy-First Computing with Agent MCP

This project showcases a groundbreaking approach to privacy-preserving computation using **homomorphic encryption** through a **Model Computation & Processing (MCP) server**. This project demonstrate the technology with a practical movie recommendation system that keeps user preferences completely private.

---

## 🌐 Vision & Core Technology

### Homomorphic Encryption & MCP Server
At the heart of this project is the MCP server, which enables a revolutionary approach to data processing:

- **Compute on Encrypted Data**: Using homomorphic encryption (HE), the server performs calculations on encrypted data without ever seeing the actual values
- **Zero Knowledge Processing**: The server remains completely blind to both input data and computation results
- **Mathematical Operations**: Supports operations like dot products and vector similarity calculations while data remains encrypted
- **End-to-End Privacy**: Data stays encrypted during transit, processing, and storage

### Privacy-First Architecture
```
User Device                    MCP Server
[Plaintext Data]     →     [Encrypted Processing]
     ↓                             ↓
[Encryption]                [Compute on Encrypted Data]
     ↓                             ↓
[Encrypted Data]     →     [No Data Visibility]
     ↓                             ↓
[Decryption]        ←     [Encrypted Results]
```

---

## 💡 Practical Application: Movie Recommendations

We demonstrate this technology through a privacy-preserving movie recommendation system:

### How It Works
1. **User Preferences**
   - Users' movie preferences are converted into feature vectors
   - These vectors are encrypted on the user's device using BFV homomorphic encryption
   - Only encrypted versions ever leave the user's device

2. **Secure Processing**
   ```python
   @mcp.tool()
   def match_movies() -> str:
       # Server only sees encrypted vectors
       encrypted_preferences = deserialize_bfvvector(encrypted_b64, context)
       
       # Movie matching happens on encrypted data
       for title, movie_vector in MOVIES.items():
           # Compute similarity while data remains encrypted
           similarity_score = encrypted_preferences * movie_vector
           results[title] = serialize_bfvvector(similarity_score)
   ```

3. **Privacy-Preserving Matching**
   - Movie vectors are stored on the server
   - Similarity scores are computed through encrypted dot products
   - Results are returned in encrypted form
   - Only the user's device can decrypt and interpret the recommendations

---

## 🛠️ Technical Implementation

### Core Components

1. **Encryption Layer (TenSEAL)**
   - BFV scheme for integer operations
   - Secure context management
   - Serialization support for encrypted vectors

2. **MCP Server**
   - FastMCP implementation
   - SSE transport layer
   - Encrypted vector operations
   - Zero-knowledge computation engine

3. **Agent System**
   - OpenAI and Ollama LLM support
   - LangChain/LangGraph orchestration
   - Encryption/decryption tools
   - Asynchronous operation support

---

## 🚀 Getting Started

1. **Installation**
   ```bash
   git clone <repository-url>
   cd PrivRec
   pip install -r requirements.txt
   ```

2. **Configuration**
   ```env
   MCP_SERVER_PORT=<your-port>
   MCP_SERVER_LOG_LEVEL=INFO
   ```

3. **Usage Example**
   ```python
   # On user device
   preferences = [8, 2, 9]  # User's movie preferences
   encrypted_prefs = list_encryption(preferences)
   
   # On MCP server (data remains encrypted)
   recommendations = match_movies(encrypted_prefs)
   
   # Back on user device
   decrypted_results = decrypt_interest_results(recommendations)
   ```

---

## 🔐 Key Features

- ✅ **True Data Privacy**: Computations on fully encrypted data
- ✅ **Homomorphic Encryption**: BFV scheme via TenSEAL
- ✅ **Zero-Knowledge Server**: MCP never sees plaintext data
- ✅ **Practical Application**: Privacy-preserving recommendations
- ✅ **Extensible Architecture**: Adaptable to other use cases
- ✅ **Multiple LLM Support**: OpenAI and Ollama integration

---

## 🎯 Future Applications

This technology can be extended to any scenario requiring privacy-preserving computations:
- Financial data processing
- Healthcare analytics
- Secure voting systems
- Private machine learning
- Confidential business intelligence

---

## 📝 Contributing

We welcome contributions! For major changes, please open an issue first to discuss your ideas.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
