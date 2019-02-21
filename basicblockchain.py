# Building a Simple,Local,Python Blockchain-Part 1
# Location: http://blockxchain.org/2017/06/04/simple-local-python-blockchain-pt1/

import hashlib
import time


# The Genesis Block
# Create a class for all of blocks to abide by
# Index - It's position in the blockchain 
# Previous Hash - the hash of the block that came before the current block
# Timestamp - the time the block was created
# Data - the information (e.g. transactions) that the block carries
# Hash - the hash of the block itself

class Block:
  def __init__(self, index, previousHash, timestamp, data, currentHash):
    self.index = index
    self.previousHash = previousHash
    self.timestamp = timestamp
    self.data = data
    self.currentHash = currentHash

# The First or Genesis Block
def getGenesisBlock():
  return Block(0, '0', '1496518102.896031', "My very first block :)", '0q23nfa0se8fhPH234hnjldapjfasdfansdf23')

blockchain = [getGenesisBlock()]
print '***GENESIS BLOCK****'
print blockchain
print '\n'

# Hashing Blocks
# 1) Convert all of the block information into one large string.
# 2) Then encode it.
# 3) Finally hash it with hashlib.sha256().

def calculateHash(index, previousHash, timestamp, data):
  value = str(index) + str(previousHash) + str(timestamp) + str(data)
  sha = hashlib.sha256(value.encode('utf-8'))
  return str(sha.hexdigest())

print '******CalculateHash******'
print calculateHash
print '\n'

def calculateHashForBlock(block):
  return calculateHash(block.index, block.previousHash, block.timestamp, block.data)

#Creating New Blocks
# A function to add blocks to the blockchain by retrieving the latest blocks

def getLatestBlock():
  return blockchain[len(blockchain)-1]

print 'getlatestBlock'
print getLatestBlock
print '\n'

def generateNextBlock(blockData):
  previousBlock = getLatestBlock()
  nextIndex = previousBlock.index + 1
  nextTimestamp = time.time()
  nextHash = calculateHash(nextIndex, previousBlock.currentHash, nextTimestamp, blockData)
  return Block(nextIndex, previousBlock.currentHash, nextTimestamp, nextHash)


# Validating the blocks are legit

# First check to see if two blocks are the same

def isSameBlock(block1, block2):
  if block1.index != block2.index:
    return False
  elif block1.previousHash != block2.previousHash:
    return False
  elif block1.timestamp != block2.timestamp:
    return False
  elif block1.data != block2.data:
    return False
  elif block1.currentHash != block2.currentHash:
    return False
  return True

# Now write a function that takes the previous block and the new block as inputs. It determines if the block is valid based on hashes and indices matching up:

def isValidNewBlock(newBlock, previousBlock):
  if previousBlock.index + 1 != newBlock.index:
    print('Indices Do Not Match Up')
    return False
  elif previousBlock.currentHash != newBlock.previousHash:
    print("Previous hash does not match")
    return False
  elif calculateHashForBlock(newBlock) != newBlock.hash:
    print("Hash is invalid")
    return False
  return True


# Now, check the validity of an entire chain by iterating over the entire list in a FOR loop:

def isValidChain(bcToValidate):
  if not isSameBlock(bcToValidate[0], getGenesisBlock()):
    print('Genesis Block Incorrect')
    return False

  tempBlocks = [bcToValidate[0]] 
  for i in range(1, len(bcToValidate)):
    if isValidNewBlock(bcToValidate[i], tempBlocks[i-1]):
      tempBlocks.append(bcToValidate[i])
    else:
      return False
  return True


  
