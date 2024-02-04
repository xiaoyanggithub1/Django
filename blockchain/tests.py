import hashlib
import json
from time import time
import concurrent.futures


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # 创建创世区块
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None, block=None):
        block = {
            'id': len(self.chain) + 1,
            'student_id': '12345',  # Example  student  ID
            'time_stamp': time(),
            'data': 'Sample  data',  # Example  data
            'data_hash': self.hash('Sample  data'),  # Example  hash  of  data
            'trade': 'Sample  trade',  # Example  trade  information
            'pre_hash': previous_hash or self.hash(self.chain[-1]),
            'self_hash': self.hash(block),  # Hash  of  the  entire  block
        }
        # Add the block to the chain
        self.chain.append(block)
        # Reset the current transactions
        self.current_transactions = []
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['id'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            proof = 0
            future = executor.submit(self.valid_proof, last_proof, proof)
            while not future.result():
                proof += 1
                future = executor.submit(self.valid_proof, last_proof, proof)
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# 创建区块链实例
blockchain = Blockchain()

# 添加一笔交易
blockchain.new_transaction("Alice", "Bob", 10)

# 更新区块链
last_block = blockchain.last_block
last_proof = last_block["proof"]
proof = blockchain.proof_of_work(last_proof)

# 添加新区块
block = blockchain.new_block(proof)

# 查询区块链
print(blockchain.chain)

# 智能合约
class SmartContract(Blockchain):
    def __init__(self):
        super().__init__()

    def validate_transaction(self, sender, recipient, amount):
        if sender == "Genesis" and recipient == "Alice":
            return False

# 创建智能合约实例
smart_contract = SmartContract()
# 验证交易
print(smart_contract.validate_transaction("Genesis", "Alice", 100))
