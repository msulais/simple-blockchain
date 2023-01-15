import jsSHA from "jssha";

class Transaction {
  constructor(user, coins){
    this.user = user;
    this.coins = coins;
  }

  get data(){
    return { user: this.user, coins: this.coins };
  }
}

class Block {
  constructor(prevBlockHash, transaction){
    this.prevBlockHash = prevBlockHash;
    this.transaction = transaction;
    this.data = { transaction: transaction.data, prevBlockHash };
    this.hash = new jsSHA("SHA-256", "TEXT")
      .update(JSON.stringify(this.data))
      .getHash("HEX");
  }
}

class BlockChain {
  constructor(){
    this.chain = [new Block('0', new Transaction('-', 0))];
  }

  add(transaction){
    let newBlock = new Block(this.lastBlock.hash, transaction);
    this.chain.push(newBlock);
  }

  get lastBlock(){
    return this.chain[this.chain.length - 1];
  }
}

let blockChain = new BlockChain();

let t1 = new Transaction('A', 190);
let t2 = new Transaction('B', 78213);
let t3 = new Transaction('C', 15);
let t4 = new Transaction('D', 9122);

blockChain.add(t1);
blockChain.add(t2);
blockChain.add(t3);
blockChain.add(t4);

for (let block of blockChain.chain){
  console.log(block.hash);
  console.log(block.data);
  console.log();
}