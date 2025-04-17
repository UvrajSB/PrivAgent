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

## 🩺 Example Use Case

> **You say:** "Can you check if my heart rate has been stable in the last 5 days?"

Behind the scenes:
1. Your heart rate readings are encrypted.
2. The encrypted vector is sent to the **MCP server**.
3. The server computes average and trend analysis **on the encrypted data**.
4. It sends back an encrypted result.
5. The agent decrypts it and replies:

> *"Your average heart rate is 87 bpm, and it appears stable over the past 5 days."*

---

## 🔐 Key Features

- ✅ **On-device agent with LLM reasoning**
- ✅ **Encryption and decryption using homomorphic encryption (CKKS via TenSEAL)**
- ✅ **MCP server that performs computations without access to raw data**
- ✅ **Streamlit-based user interface**
- ✅ **Privacy-preserving by design**

---

## 🌐 Vision

This prototype is a step toward building **confidential AI systems**, where sensitive data can be intelligently analyzed without ever being exposed. The collaboration between on-device agents and an encrypted computation server (**MCP**) shows how we can move toward **trustless, privacy-first AI architectures** in healthcare and beyond.
