from datetime import datetime

# Class for block objects.
# Holds reference to a transaction's
# data and the previous blocks hash.

# Includes a self defined hash function
# in order to make the Block objects hashable.


class Block:
    def __init__(self, i, d, h, t):
        self.Index = i
        self.Data = d
        self.PreviousHash = h
        self.Nonce = ''
        self.Timestamp = t

    def __str__(self):
        return "[{i}] | Previous Hash: [{h}] Data: [{d}] Nonce [{n}] ".format(i=self.Index, h=self.PreviousHash, d=self.Data, n=self.Nonce)

    def __hash__(self):
        return abs(hash("{ph},{a},{r},{s}".format(ph=self.PreviousHash, a=self.Data.Amount, r=self.Data.Recipient, s=self.Data.Sender)))

    Index = -1
    Data = "N/A"
    PreviousHash = "N/A"
    Nonce = "N/A"
    Timestamp = datetime.now()
