import hashlib
import time


class Block:
    def __init__(self, index, proofNo, prevHash, data, timestamp=None):
        self.index = index
        self.proofNo = proofNo
        self.prevHash = prevHash
        self.data = data
        self.timestamp = timestamp or time.time()

    @property
    def calculateHash(self):
        blockOfString = "{}{}{}{}{}".format(
            self.index, self.proofNo, self.prevHash, self.data, self.timestamp)

        return hashlib.sha256(blockOfString.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(
            self.index, self.proofNo, self.prevHash, self.data, self.timestamp)
