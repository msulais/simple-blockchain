from hashlib import sha256
from json import dumps

class Transaction:
  def __init__(self, user, coins):
    self.user = user
    self.coins = coins

  @property
  def data(self):
    return { 'user': self.user, 'coins': self.coins }

class Block:
  def __init__(self, prevBlockHash, transaction):
    self.prevBlockHash = prevBlockHash
    self.transaction = transaction
    self.data = { 'transaction': self.transaction.data, 'prevBlockHash': self.prevBlockHash }
    self.hash = sha256(dumps(self.data).encode()).hexdigest()

class BlockChain:
  def __init__(self):
    self.chain = [Block('0', Transaction('-', 0))]

  def add(self, transaction):
    newBlock = Block(self.lastBlock.hash, transaction)
    self.chain.append(newBlock)

  @property
  def lastBlock(self):
    return self.chain[-1]

if __name__ == "__main__":
  blockChain = BlockChain()

  t1 = Transaction('A', 190)
  t2 = Transaction('B', 78213)
  t3 = Transaction('C', 15)
  t4 = Transaction('D', 9122)

  blockChain.add(t1)
  blockChain.add(t2)
  blockChain.add(t3)
  blockChain.add(t4)

  for block in blockChain.chain:
    print(block.hash)
    print(block.data)
    print()