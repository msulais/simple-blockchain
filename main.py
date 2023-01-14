import hashlib
import json



class CoinBlock:
  def __init__(self, prevBlockHash, transaction):
    self.prevBlockHash = prevBlockHash
    self.transaction = transaction

    self.data = {
      'transaction': self.transaction,
      'previousBlockHash': self.prevBlockHash
    }
    self.hash = hashlib.sha256(json.dumps(self.data).encode()).hexdigest()



class BlockChain:
  def __init__(self):
    self.chain = []
    self.initialize()

  def initialize(self):
    genesis = CoinBlock('0', 'Genesis')
    self.chain.append(genesis)

  def add(self, transaction):
    newBlock = CoinBlock(self.lastBlock.hash, transaction)
    self.chain.append(newBlock)

  @property
  def length(self):
    return len(self.chain)

  @property
  def lastBlock(self):
    return self.chain[-1]



if __name__ == "__main__":
  blockChain = BlockChain()

  t1 = { 'user': 'A', 'coins': 190 }
  t2 = { 'user': 'B', 'coins': 78213 }
  t3 = { 'user': 'C', 'coins': 15 }
  t4 = { 'user': 'D', 'coins': 9122 }

  blockChain.add(t1)
  blockChain.add(t2)
  blockChain.add(t3)
  blockChain.add(t4)

  for block in blockChain.chain:
    print(block.data)