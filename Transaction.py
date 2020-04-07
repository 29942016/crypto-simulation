from datetime import datetime

class Transaction:
    def __init__(self, r, s, a):
        self.Recipient = r
        self.Sender = s
        self.Amount = a
    def __str__(self):
        return "[{t}] from {s} to {r} of amount {a}".format(t=self.Timestamp, s=self.Sender, r=self.Recipient, a=self.Amount)

    Recipient = "N/A"
    Sender = "N/A"
    Amount = 0
    Timestamp = datetime.now()