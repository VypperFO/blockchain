import hashlib
from Block import Block


class BlockChain:
    def __init__(self):
        self.chain = []  # the blockchain made of blocks
        self.currentData = []  # all completed transactions in the blockchain
        self.nodes = set()
        self.constructGenesis()  # contructs the initial block

    # Construct the first block
    def constructGenesis(self):
        self.constructBlock(proofNo=0, prevHash=0)

    # Block constructor
    def constructBlock(self, proofNo, prevHash):
        block = Block(
            index=len(self.chain),
            proofNo=proofNo,
            prevHash=prevHash,
            data=self.currentData)

        self.currentData = []

        # Adds block to the blockchain
        self.chain.append(block)
        return block

    @staticmethod
    def checkValidity(block, prevBlock):
        if (prevBlock.index + 1 != block.index):
            return False
        elif (prevBlock.calculateHash != block.prevHash):
            return False
        elif not BlockChain.verifyingProof(block.proofNo, prevBlock.proofNo):
            return False
        elif block.timestamp <= prevBlock.timestamp:
            return False

        return True

    def newData(self, sender, recipient, quantity):
        self.currentData.append({
            'sender': sender,
            'recipient': recipient,
            'quantity': quantity
        })
        return True

    @staticmethod
    def proofOfWork(lastProof):
        '''this simple algorithm identifies a number f' such that hash(ff') contain 4 leading zeroes
         f is the previous f'
         f' is the new proof
        '''
        proofNo = 0
        while BlockChain.verifyingProof(proofNo, lastProof) is False:
            proofNo += 1

        return proofNo

    @staticmethod
    def verifyingProof(lastProof, proof):
        # verifying the proof: does hash(last_proof, proof) contain 4 leading zeroes?

        guess = f'{lastProof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def latestBlock(self):
        # returns the last block in the chain
        return self.chain[-1]

    def blockMining(self, detailsMiner):
        self.newData(
            sender=0,  # implies this node has created a new block
            receiver=detailsMiner,
            # creating a new block (or identifying the proof number) is awarded 1 (coin)
            quantity=1,
        )

        # latest block
        lastBlock = self.latestBlock

        lastProofNo = lastBlock.proofNo
        proofNo = self.proofOfWork(lastProofNo)

        lastHash = lastBlock.calculateHash
        block = self.constructBlock(proofNo, lastHash)

        return vars(block)

    def createNode(self, adress):
        self.nodes.add(adress)
        return True

    @staticmethod
    def obtainBlockObject(blockData):
        # obtains block object from the block data

        return Block(
            blockData['index'],
            blockData['proofNo'],
            blockData['prevHash'],
            blockData['data'],
            timestamp=blockData['timestamp'])
