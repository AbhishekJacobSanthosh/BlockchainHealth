import json
import hashlib
import time

BLOCKCHAIN_FILE = "blockchain.json"

def load_blockchain():
    """Load blockchain from file or create a genesis block if empty."""
    try:
        with open(BLOCKCHAIN_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        genesis_block = [{"index": 0, "previous_hash": "0" * 64, "transactions": ["Genesis Block"]}]
        save_blockchain(genesis_block)
        return genesis_block

def save_blockchain(blockchain):
    """Save blockchain to file."""
    with open(BLOCKCHAIN_FILE, "w") as file:
        json.dump(blockchain, file, indent=4)

def create_block(previous_hash, transactions):
    """Create a new block in the blockchain."""
    blockchain = load_blockchain()
    new_block = {
        "index": len(blockchain),
        "timestamp": time.time(),
        "previous_hash": previous_hash,
        "transactions": transactions,
        "hash": hashlib.sha256(str(transactions).encode()).hexdigest()
    }
    blockchain.append(new_block)
    save_blockchain(blockchain)
    return new_block
