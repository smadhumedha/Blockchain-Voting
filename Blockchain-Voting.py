import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, '0', int(time.time()), 'Genesis Block', 'genesis_hash')
        self.chain.append(genesis_block)

    def add_block(self, data):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = int(time.time())
        previous_hash = previous_block.hash
        hash = self.calculate_hash(index, previous_hash, timestamp, data)
        new_block = Block(index, previous_hash, timestamp, data, hash)
        self.chain.append(new_block)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = f'{index}{previous_hash}{timestamp}{data}'.encode()
        return hashlib.sha256(value).hexdigest()

class VotingApp:
    def __init__(self):
        self.blockchain = Blockchain()
        self.voted_voters = set()

    def cast_vote(self, voter_id, candidate):
        if voter_id not in self.voted_voters:
            self.voted_voters.add(voter_id)
            data = f"Vote: {candidate} by {voter_id}"
            self.blockchain.add_block(data)
            print(f"[✓] Vote cast for {candidate} by {voter_id}")
            return True
        else:
            print(f"[!] Voter '{voter_id}' has already voted.")
            return False

    def get_vote_count(self, candidate):
        count = 0
        for block in self.blockchain.chain:
            if f"Vote: {candidate}" in block.data:
                count += 1
        return count

    def show_blockchain(self):
        print("\n--- Blockchain ---")
        for block in self.blockchain.chain:
            print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}")
        print("------------------\n")

# Main interactive menu
def main():
    app = VotingApp()

    while True:
        print("\n==== Voting App Menu ====")
        print("1. Cast Vote")
        print("2. Show Vote Count")
        print("3. Show Blockchain")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            voter_id = input("Enter your Voter ID: ")
            candidate = input("Enter candidate name: ")
            app.cast_vote(voter_id, candidate)

        elif choice == '2':
            candidate = input("Enter candidate name to check vote count: ")
            count = app.get_vote_count(candidate)
            print(f"[*] Total votes for {candidate}: {count}")

        elif choice == '3':
            app.show_blockchain()

        elif choice == '4':
            print("Exiting Voting App. Goodbye!")
            break

        else:
            print("[!] Invalid choice. Try again.")

if __name__ == "__main__":
    main()
