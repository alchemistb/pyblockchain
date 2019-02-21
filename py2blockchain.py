# Let's Build the Tiniest Blockchain (50 lines)
# Location: https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b

import hashlib as hasher
import time
import datetime as date

# The Genesis Block
# Create a class for all of blocks to abide by
# Index - It's position in the blockchain 
# Previous Hash - the hash of the block that came before the current block
# Timestamp - the time the block was created
# Data - the information (e.g. transactions) that the block carries
# Hash - the hash of the block itself


class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()

  # Hashing Blocks
  # 1) Hash with hasher.sha256() 
  # 2) Convert all of the block information into one large string.

  def hash_block(self):
      sha = hasher.sha256()
      sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
      return sha.hexdigest()


# The First or Genesis Block
def create_genesis_block():
  return Block(0, date.datetime.now(), "Genesis Block", "0")


# Create the next block
def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Hey! I'm block " + str(this_index)
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)


# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]


# How many blocks should we add to the chain after the genesis block
num_of_blocks_to_add = 20


# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!
  print "Block #{} has been added to the blockchain!".format(block_to_add.index)
  print "Timestamp: {}".format(block_to_add.timestamp)
  print "Data: {}".format(block_to_add.data)
  print "Hash: {}\n".format(block_to_add.hash)
