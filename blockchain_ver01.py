# [参考](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass
 
    def new_transaction(self):
        # Adds a New transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hashes a Block 
        pass

    @property
    def last_block(self):
        # Return the last Block in the chain
        pass

    class Blockchain(object):
        ...
        def new_transaction(self, sender, recipient, amount):
            """
            Creates a new transaction to go into the next mined Block
            :param sender: <str> Address of the Sender
            :param recipient: <str> Address of the Recipient
            :param amount: <int> Amount
            :return: <int> The index of the Block that will hold this transaction
            """

            self.current_transactions.append({
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            })

            return self.last_block['index']+ 1

import hashlib
import json
from time import time
from typing_extensions import Litera

from flask.json import jsonify
from flask.wrappers import Response


class Blockchain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash:(Optional)<str>Hash of previous Block
        :return:<dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaciton to go into the next mined block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <str> Amount
        :return:<int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1


    @property
    def last_block(self):
        return self.chain[-1]

    
    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        # we must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes 
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        

    from hashlib import sha256
    x = 5
    y = 0 #We don't know what y should be yet...
    while sha256(f'{x*y}'.encode()).hexdigest()[-1]!= "0":
        y += 1
        print(f'The solusion is y = {y}')

import hashlib
import json

from time import time
from uuid import uuid4


class Blockchain(object):
    ...

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
        - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
        - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask


class Blockchain(object):
    ...



# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
Blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"


@app.route('/chain/', methods=['GET'])
def full_chain():
    response = {
        'chain': Blockchain.chain,
        'length': len(Blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__math__':
    app.run(host='0.0.0.0', port=5000)


{
    "sender": "my address",
    "recipient": "someone else's address",
    "amount": 5
}


import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

...


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()


    # Check that the requird field are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing Values', 400

    
    # Create a new Transaction
    index = Blockchain.new_tarnsaction(values['sender'], values['recipient'],values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201
