# PrivAgents: Privacy-Enhancing Agents with Encrypted Computation

**PrivAgents** is a privacy-first framework that showcases how autonomous agents, both on-device and in the cloud, can perform secure data processing while ensuring complete confidentiality. It leverages **Privacy-Enhancing Technologies (PETs)** herein **Homomorphic Encryption (HE)** to compute on encrypted data without ever accessing raw information.

Through a conversational agent interface, user data is encrypted on the device, sent to a secure processing unit (MCP), and the results are returned in encrypted form to be decrypted locally. This creates a secure and intelligent system for sensitive environments such as healthcare, personalization, and finance.

![PET enabled MCP server](https://github.com/user-attachments/assets/1c8f39ea-809a-4bf7-95c0-c359cfaa9bf2)


---

## 🔐 Why PrivAgents

On-device models offer privacy but are often limited in power. Cloud models offer power but raise trust concerns. PrivAgents solves this by combining the strengths of both:

- On-device or cloud-based agents to suit your compute and trust needs  
- Homomorphic encryption ensures data remains private during processing  
- Modular MCP server performs encrypted similarity calculations on the backend  
- End-to-end encrypted pipeline for secure data interaction  

---

## ⚙️ Supported Agents

- ✅ **Ollama Agent** for on-device reasoning using local models  
- ✅ **OpenAI Agent** for cloud-based intelligence via API  

Choose your agent type based on privacy constraints and available resources.

---

## 🧠 Architecture Overview

```plaintext
      +------------------------+
      |     User Device        |
      |  (Agent + Encryption)  |
      +------------------------+
         |   Encrypted Input
         v
+------------------------+   ← Secure Channel →
|     MCP Server         |  (Encrypted Similarity Calculation)
+------------------------+
         |   Encrypted Result
         v
      +------------------------+
      |  User Device (Decrypt) |
      +------------------------+
```

---

## 📁 Project Structure

```
PrivAgents/
│
├── agent/           # Ollama and OpenAI agent implementations with PET tools
├── mcp/             # Encrypted processing logic for similarity-based analysis
├── utils/           # Context setup, encryption helpers
├── data/            # Sample inputs and encrypted output files
└── .env             # Configuration for ports and logging
```

---

## 🚀 Getting Started

### 1. Clone and Set Up

```bash
git clone https://github.com/UvrajSB/PrivRec.git
cd PrivRec
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Start the MCP Server

From the root directory:

```bash
PYTHONPATH=. python mcp/server.py
```

### 3. Run an Agent

- **Ollama Agent (Local Execution)**

```bash
PYTHONPATH=. python agent/ollama_mcp_agent.py
```

- **OpenAI Agent (Cloud Execution)**

```bash
PYTHONPATH=. python agent/openai_mcp_agent.py
```

Each agent encrypts the user input, sends it for encrypted similarity calculation, and decrypts the response privately on-device.

---

## 🎬 Movie Preference Matching: Encrypted End-to-End Personalization

The movie preference matching use case is a working demonstration of how **privacy-preserving recommendation systems** can function without accessing user data in plaintext. It showcases the **end-to-end use of homomorphic encryption** to encrypt user preferences, run secure similarity calculations, and deliver personalized results—all while ensuring zero exposure of raw data.

---

### 🔁 Workflow Overview

1. **User inputs a movie interest vector**  
   The user is asked to rate or prioritize different genres (e.g. Action, Romance, Sci-Fi). For example:  
   ```
   [8, 2, 9] → represents user's preference intensity across three genres.
   ```

2. **Encryption on the agent side**  
   The agent (either Ollama or OpenAI based) uses TenSEAL to homomorphically encrypt the interest vector using the BFV scheme. The result is an encrypted tensor, unreadable even to the server.

3. **Encrypted similarity calculation on the MCP server**  
   - The MCP server has a collection of predefined movie profiles, each represented as a plaintext vector:
     ```python
     MOVIES = {
       "Inception":     [9, 1, 8],
       "The Notebook":  [1, 9, 2],
       "Interstellar":  [8, 2, 9],
       "The Godfather": [7, 5, 4]
     }
     ```
   - It performs **encrypted similarity calculations** between the encrypted user vector and each plaintext movie profile.
   - This similarity is computed using a **dot product** under encryption, without decrypting the user vector.

4. **Encrypted results are returned**  
   The server writes the encrypted similarity scores for all movies to a file, for example:
   ```
   data/interest_results
   ```

5. **Decryption on the user device**  
   The agent loads the encrypted results and decrypts them locally using the original context and keys. The decrypted scores represent how closely each movie matches the user's preferences.

6. **Optional: Rank and display results**  
   The agent can sort the scores and show the top movie recommendations based on similarity, all while ensuring the user's input and preferences were never visible to the server.

<img width="1026" alt="Terminal" src="https://github.com/user-attachments/assets/72fe8e53-fed7-4515-be19-774887a3a899" />



---

### 📦 Benefits

- ✅ **Zero Trust Required**: Server never sees user data  
- ✅ **Agent Agnostic**: Works with both on-device and cloud-based LLM agents  
- ✅ **Extendable**: Can support more complex user profiles or additional domains (like music, shopping, healthcare)  
- ✅ **Educational**: Demonstrates how homomorphic encryption works in a practical context  

---

## 👥 Contributing

Interested in building secure and intelligent systems with PETs? Whether it is extending agent logic, experimenting with new encrypted workflows, or refining the MCP layer, your contributions are welcome. Fork the repo and get started.
