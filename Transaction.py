from datetime import datetime

class Transaction:
    def __init__(self, r, s, a):
        self.Recipient = r
        self.Sender = s
        self.Amount = a

    Recipient = "N/A"
    Sender = "N/A"
    Amount = 0
    Timestamp = datetime.now()