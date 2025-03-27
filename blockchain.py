import hashlib
import json
import time

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.transactions = transactions
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.balances = {}  # Store balances per user

    def create_genesis_block(self):
        return Block(0, "0", [{"message": "Genesis Block"}])

    def add_block(self):
        if not self.pending_transactions:
            return None
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), last_block.hash, self.pending_transactions)
        self.chain.append(new_block)
        self.pending_transactions = []  # Clear pending transactions
        return new_block

    def new_transaction(self, sender, recipient, details):
        transaction = {"sender": sender, "recipient": recipient, "details": details, "timestamp": time.ctime()}
        self.pending_transactions.append(transaction)

    def mine_block(self):
        if not self.pending_transactions:
            print("\n⚠️ No pending transactions to mine!\n")
            return None
        new_block = self.add_block()
        print(f"\n✅ New Block Mined! Index: {new_block.index}, Hash: {new_block.hash}\n")
        return new_block
    
    def display_blockchain(self):
        print("\n📜 Blockchain Data:\n")
        for block in self.chain:
            print(f"🔷 Block {block.index}: {block.transactions}\n")


    def get_balance(self, user):
        return self.balances.get(user, 0)

    def update_balance(self, user, amount):
        if user in self.balances:
            self.balances[user] += amount
        else:
            self.balances[user] = amount  # Initialize if not present

