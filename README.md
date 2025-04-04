# 🗳️ Decentralized Voting System using Blockchain (Python)

This project is a **simple prototype** of a decentralized voting system built using **Python** and **Blockchain principles**. It simulates how votes can be securely stored in a blockchain, ensuring **immutability, transparency, and tamper resistance**.

---

## 💡 How It Works

The system includes the following key components:

### 🔗 Blockchain
- Each **vote** is stored in a new block.
- Blocks contain: `Index`, `Previous Hash`, `Timestamp`, `Vote Data`, and `Current Hash`.
- Each block links to the previous one via cryptographic hashes (SHA-256), preserving integrity.

### 🧑‍💻 Voter Identity
- Voters are identified by unique **Voter IDs** (entered at runtime).
- The system prevents **double voting** by keeping track of who has already voted.

### 📦 Vote Storage
- Each vote is stored as a string:  
  `"Vote: <Candidate Name> by <Voter ID>"`

### 🛡️ Key Features
- Prevents multiple votes from the same voter
- Blockchain-backed vote recording
- Transparent and tamper-proof vote history
- Interactive **command-line interface**

---

## 🖥️ Script Flow

1. **Cast Vote**  
   Voter enters their ID and chooses a candidate.

2. **Show Vote Count**  
   Displays the number of votes a candidate has received.

3. **Show Blockchain**  
   Displays the full blockchain, including all recorded votes.

4. **Exit**  
   Ends the simulation.

---
