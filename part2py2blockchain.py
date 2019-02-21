# Let's Build the Tiniest Blockchain Part 2
# Location: https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d 

import hashlib as hasher
import time
import datetime as date
import json
import urllib
from flask import Flask
from flask import request

node = Flask(__name__)

# Store the transaction that this node has in a list
this_nodes_transaction = []

# Add Nodes to the Blockchain Network
# Create an HTTP Server allowing post requests
# The Request Body will have From/To/Amount
@node.route('/txion', methods=['POST'])
def transaction():
  if request.method == 'POST':
    # On each new POST request, we extract the transaction data
    new_txion = request.get_json()
    # Then we add the transaction to our list
    this_nodes_transactions.append(new_txion)
    # Because the transaction was successfully submitted, 
    # we log it to our console
    print '***New Transaction***'
    print "FROM: {}".format(new_txion['from'])
    print "TO: {}".format(new_txion['to'])
    print "Amount: {}\n".format(new_txion['amount'])
    # Then we let the client know that it worked out successfully
    return "Transaction submission successful\n"

node.run()    


#.....blockchain
#.....Block class definition



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

  # Hashing_block Function 
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
 


miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"


# Proof of Work (POW) that a miner successfully 'mined' the last block
# This will lead to a miner getting a coin

def proof_of_work(last_proof):
  # Create a variable that will be used to find the next proof of work
  incrementor = last_proof + 1
  # Keep incrementing the incrementor 
  # till it's equal to a number divisible by 9
  # (9 was chosen, but this can be any number for any reason)
  # and the proof of work of the previouos block in the chain 
  while not(incrementor %9 == 0 and incremenator % last_proof == 0):
    incrementor += 1
  # Once that number is found,return it as a proof of work
  return incrementor

@node.route('/mine', methods =['GET'])
def mine():
  # Get the last proof of work
  last_block = blockchain[len(blockchain) - 1]
  last_proof = last_block.data['proof-of-work']
  # Find the POW for the current block being mined
  # Note: the program will hang here till a new POW is found!
  proof = proof_of_work(last_proof)
  # Once we find a valid proof of work,
  # we know we can mine a block.
  # Reward the miner by adding a transaction
  this_nodes_transactions.append(
    {"from":"network","to":miner_address, "amount":1})
  
  # Now gather data needed to create the new block

  new_block_data = {"proof-of-work":proof-of-work,
    "transactions":list(this_nodes_transactions)}
  
  new_block_index = last_block.index +1
  new_block_timestamp = this_timestamp = date.datetime.now()
  last_block_hast = last_block.hash

  # Empty transaction list
  this_nodes_transactions[:] = []

  # Create the new block!
  mined_block = Block(
    new_block_index,
    new_block_timestamp,
    new_block_data,
    last_block_hash
  )
  blockchain.append(mined_block)

  # Let the client know we mined a block
  return json.dumps({
      "index":new_block_index,
      "timestamp":str(new_block_timestamp),
      "data":new_block_data,
      "hash":last_block_hash
  }) + "\n"    




# Consesus Algorithim
# If a node's chain is different from another's (i.e.there is a conflict), then the longest chain in the network stays. All shorter chains will be deleted. 
# If there is no conflict between the chains in our network then we carry on.


@node.route('/blocks', methods = ['GET'])
def get_blocks():
  chain_to_send = blockchain
  # Convert our blocks into dictionaries to send as json objects later
  for block in chain_to_send:
    block_index = str(block.index)
    block_timestamp = str(block.timestamp)
    block_data = str(block.data)
    block_hash = block.hash
    block ={
      "index": block_indx,
      "timestamp": block_timestamp,
      "data": block_data,
      "hash": block_hash
   }
  # Send chain to whomever requested it
  chain_to_send = json.dumps(chain_to_send)
  return chain_to_send

def find_new_chains():
  # Get the blockchains of every other node
  other_chains = []
  for node_url in peer_nodes:
    # Get their chains using a GET request
    block = requests.get(node_url + "/blocks").content
    # Convert the JSON object to a dictionary
    blocks = json.loads(block)
    # Add it to the list
    other_chains.apped(block)
  return other_chains


def consensus():
  # Get blocks from other nodes
  other_chains = find_new_chains()
  # If our chain isn't longest, then store the longest chain
  longest_chain = blockchain
  for chain in other_chains:
    if len(longest_chain)< len(chain):
      longest_chain = chain
  # If the longest chains wasn't ours, then set our chain as longest
  blockchain = longest_chain















