from BlockChain import BlockChain
from Block import Block

blockchain = BlockChain()

print("***Mining coin about to start***")
print(blockchain.chain)

# coin 1
lastBlock = blockchain.latestBlock
lastProofNo = lastBlock.proofNo
proofNo = blockchain.proofOfWork(lastProofNo)

blockchain.newData(
    sender="0",  # it implies that this node has created a new block
    recipient="Quincy Larson",  # let's send Quincy some coins!
    # creating a new block (or identifying the proof number) is awarded with 1
    quantity=1,
)

lastHash = lastBlock.calculateHash
block = blockchain.constructBlock(proofNo, lastHash)

# coin 2
lastBlock = blockchain.latestBlock
lastProofNo = lastBlock.proofNo
proofNo = blockchain.proofOfWork(lastProofNo)

blockchain.newData(
    sender="0",  # it implies that this node has created a new block
    recipient="Quincy Larson",  # let's send Quincy some coins!
    # creating a new block (or identifying the proof number) is awarded with 1
    quantity=1,
)

lastHash = lastBlock.calculateHash
block = blockchain.constructBlock(proofNo, lastHash)

print("***Mining coin has been successful***")
print(blockchain.chain)

exit = False

while not exit:
    print("e) Exit\na) Add one coin")
    answer = input("What do you wanna do ?: ").lower()

    if answer == "e":
        exit = True
    elif answer == "a":
        print("coin + 1")
