import os
from Transaction import Transaction
from datetime import datetime
import pickle

def main():
    _StartNewTransaction = 'Y'
    while _StartNewTransaction == 'Y':
        _StartNewTransaction = raw_input('Create new transaction？ (y/n) ').upper()
        if _StartNewTransaction == 'Y':
            _Transaction = CreateTransaction()
            SaveTransaction(_Transaction)
    else:
        print "Exiting application..."

def DisplayTransactions():
    _Path = 'transactions.pkl'
    data = []
    with open(_Path, 'rb') as fd:
        try:
            while True:
                data.append(pickle.load(fd))
        except EOFError:
            pass


def CreateTransaction():
    _Recipient = raw_input('Enter recipient: ')
    _Sender = raw_input('Enter sender: ')
    _Amount = raw_input('Enter amount: ')
    _Timestamp = datetime.now()
    _tBlock = Transaction(_Recipient, _Sender, _Amount)
    print "[{t}] from {s} to {r} of amount ${a}".format(t=_Timestamp, s=_Sender, r=_Recipient, a=_Amount)
    return _tBlock

def SaveTransaction(transaction):
    _Path = "transactions.pkl"
    with open(_Path, 'a+') as fp:
        pickle.dump(transaction, fp)


main()