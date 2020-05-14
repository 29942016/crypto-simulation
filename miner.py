import os
from Transaction import Transaction
from Block import Block
from datetime import datetime
from hashlib import sha256
import pickle
import time

# Reference to the transaction + blockchain file
_Transactions = 'transactions.pkl'
_BlockChain = 'chain.bc'

# Stores the latest information globally
_TotalTransactions = 0
_CurrentBlock = 0
_CurrentHash = 0


def main():
    os.system('clear')

    # Checks to see if the blockchain file (*.bc)
    # contains any hashes. If no then create the
    # first block and save its hash to the file.
    InitializeBlockChain()

    # Loop continously looking for new transactions in
    # the transactions file, if found then find a valid
    # nonce hash and save it to the blockchain file.
    while True:
        print('Total Transactions: {t}'.format(t=_TotalTransactions))
        if HasNewTransaction():
            print('\nFound new transaction.')
            HandleNewTransactions()
            time.sleep(2)
        else:
            print('\nWaiting for new transactions...')
            time.sleep(2)
        os.system('clear')


# Checks if the transaction file contains
# any new transactions.
def HasNewTransaction():
    global _TotalTransactions
    global _Transactions
    data = []

    with open(_Transactions, 'rb') as fd:
        try:
            while True:
                data.append(pickle.load(fd))
        except EOFError:
            pass

    if _TotalTransactions <= len(data) - 1:
        return True
    else:
        return False

# Given a collection of hashes or a single
# hash save it to the blockchain file.


def UpdateBlockChain(hash):
    global _BlockChain
    print(hash)
    with open(_BlockChain, "ab+") as fp:
        if isinstance(hash, list):
            for h in hash:
                pickle.dump(h, fp)
        else:
            pickle.dump(hash, fp)


# Read the block chain file, loading all
# hashes into a collection in memory,
# and returned as the result.
def ReadBlockChain():
    global _BlockChain
    data = []

    with open(_BlockChain, 'rb') as fd:
        try:
            while True:
                data.append(pickle.load(fd))
        except EOFError:
            pass

    return data

# Read the transaction file, loading all
# exchanges into a collection in memory,
# and returned as the result.


def ReadTransactions():
    global _Transactions
    data = []

    with open(_Transactions, 'rb') as fd:
        try:
            while True:
                data.append(pickle.load(fd))
        except EOFError:
            pass

    return data

# Run once on launch, if the blockchain file
# is empty then  create a dummy hash, otherwise
# load all the existing hashes into applications
# memory.


def InitializeBlockChain():
    data = ReadBlockChain()
    if len(data) == 0:
        global _CurrentBlock
        _CurrentBlock = Block(0, "first block", Hash256(
            "first block"), datetime.now())
        print("No blockchain data, creating first block [{h}].".format(
            h=_CurrentBlock.PreviousHash))
        UpdateBlockChain(_CurrentBlock.PreviousHash)
    else:
        global _CurrentHash
        global _TotalTransactions

        _CurrentHash = data[-1]
        _TotalTransactions = len(data) - 1

        # print("Blockchain already initialized, latest hash is [{h}].".format(h=_CurrentHash))
        # print("[TODO]")


# If we find new transactions in the transaction
# file, then we create corresponding block chain
# hashes and save them to the blockchain file.
def HandleNewTransactions():
    global _TotalTransactions
    transactions = ReadTransactions()
    blocks = ReadBlockChain()
    newBlocks = []

    while _TotalTransactions < len(transactions):
        newBlock = Block(
            _TotalTransactions, transactions[_TotalTransactions], blocks[_TotalTransactions - 1], datetime.now())
        validHash = GenerateValidNonce(newBlock)
        blocks.append(validHash)
        newBlocks.append(validHash)
        _TotalTransactions += 1

    print("> Writing {c} new blocks to file".format(c=len(newBlocks)))
    UpdateBlockChain(newBlocks)


# Attempts to generate a valid nonce within 50k
# attempts. Validity is determined based on if the
# hash in binary form contains 14 0s.
def GenerateValidNonce(block):
    pattern = "00000000000000"
    nonce = 0
    currentBlockHash = hash(block)
    isValid = False

    while(isValid == False):
        blockHash = Hash256("{d}{n}".format(d=currentBlockHash, n=nonce))
        # print("iteration: {i} - {h}".format(i=nonce, h=blockHash))

        if (pattern in bin(int(blockHash, 16)) or nonce >= 50000):
            # print("Valid nonce found: {n} - {h}".format(n=nonce, h=blockHash))
            return blockHash
        else:
            nonce += 1

# Uses the hashlib library to call sha256 on the given
# data, and returns the hexidecimal hash.


def Hash256(data):
    _hashed = sha256(data.encode('utf-8'))
    return _hashed.hexdigest()


main()
