class Person:
    def __init__(self, privateKey, publicKey, coins):
        self.privateKey = privateKey
        self.publicKey = publicKey
        self.coins = coins
        self.info = "Person info: " + " Private key: " + str(self.privateKey) + " Public Key: " + str(self.publicKey) + " Coins: " + str(self.coins)

class Transaction:
    def __init__(self, p1PubKey, hashPrevTx, p0Sign, coins, id):
        self.p1PubKey = p1PubKey
        self.hashPrevTx = hashPrevTx
        self.p0Sign = p0Sign    # p0's private key used to hash information verifiable by its public key
        self.coins = coins
        self.id = id
        self.info = "Transaction info: " + " Person 1 public key: " + str(self.p1PubKey) + " Hash of previous transaction: " + str(self.hashPrevTx) + " Person 0 signature: " + str(self.p0Sign) + " Coins transfered: " + str(self.coins) + "Transaction ID: " + str(self.id)
# Run a function to complete coin transfer here? E.g:
# ray.coins += tx50.coins
# kal.coins -= tx50.coins

# Convert to hex when certain hash function is functional
def hash(n):
    return n*9876+7

kal = Person(1000, 1/1000, 100)
ray = Person(1/50, 50, 20)

tx50 = Transaction(ray.publicKey, 2345, hash(kal.privateKey), 15, 50)
tx51 = Transaction(kal.publicKey, hash(tx50.id), hash(ray.privateKey), 2, tx50.id+1)

# print("Transaction 51, hash of transaction 50: " + str(tx51.hashPrevTx))
print(kal.info)
print(tx51.info)

# Next:
# Get transaction to apply changes to wallets
