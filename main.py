import os
from Transaction import Transaction
from datetime import datetime
import pickle


def main():
    _StartNewTransaction = 0
    while _StartNewTransaction != 3:
        print('=== Transaction Recording Client ===\n1) Create new transaction\n2) Display transaction history\n3) Exit')
        _StartNewTransaction = int(input('>> '))
        os.system('clear')
        if _StartNewTransaction == 1:
            _Transaction = CreateTransaction()
            SaveTransaction(_Transaction)
        elif _StartNewTransaction == 2:
            DisplayTransactions()
    else:
        print("Exiting application...")

# Reads all available transactions from the
# transaction file and attempts to convert them
# into transaction objects.


def DisplayTransactions():
    _Path = 'transactions.pkl'
    data = []
    with open(_Path, 'rb') as fd:
        try:
            while True:
                data.append(pickle.load(fd))
        except EOFError:
            pass
    print('\n=== START OF TRANSACTIONS ===')
    for transaction in data:
        print(transaction)
    print('=== END OF TRANSACTIONS ===\n')


# Generates a transaction object given a
# recipient, sender and amount. Then notifies
# the user.

def CreateTransaction():
    _Recipient = input('Enter recipient: ')
    _Sender = input('Enter sender: ')
    _Amount = input('Enter amount: ')
    _Timestamp = datetime.now()
    _tBlock = Transaction(_Recipient, _Sender, _Amount, _Timestamp)
    os.system('clear')
    print("=== TRANSACTION CREATED ===")
    print("[{t}] from {s} to {r} of amount ${a}".format(
        t=_Timestamp, s=_Sender, r=_Recipient, a=_Amount))

    print("\n")
    return _tBlock

# Given a transaction object, save
# it to the transaction file.


def SaveTransaction(transaction):
    _Path = "transactions.pkl"
    with open(_Path, "ab+") as fp:
        pickle.dump(transaction, fp)


main()
