import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(str(self.index).encode() + str(self.timestamp).encode() + str(self.data).encode() + str(self.previous_hash).encode()).hexdigest()

def create_genesis_block():
    return Block(0, time.time(), "Genesis Block", "0")

if __name__ == "__main__":
    blockchain = [create_genesis_block()]
    print("Genesis Block has been created:")
    print("Index: ", blockchain[0].index)
    print("Timestamp: ", blockchain[0].timestamp)
    print("Data: ", blockchain[0].data)
    print("Previous Hash: ", blockchain[0].previous_hash)
    print("Hash: ", blockchain[0].hash)
