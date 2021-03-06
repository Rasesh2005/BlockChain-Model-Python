"""
Try Different Thing in this file to get understanding of how it works
"""
from blockChain import BlockChain
from transaction import Transaction
from ecdsa import SigningKey

def to_string(key,isPublic):
    if isPublic:
        return key.to_pem()[len(b"-----BEGIN PUBLIC KEY-----\n"):-len(b"\n-----END PUBLIC KEY-----\n")].decode()
    return key.to_pem()[len(b"-----BEGIN EC PRIVATE KEY-----\n"):-len(b"\n-----END EC PRIVATE KEY-----\n")].decode()


def to_pem(key_str,isPublic):
    if isPublic:
        return b"-----BEGIN PUBLIC KEY-----\n"+key_str.encode()+b"\n-----END PUBLIC KEY-----\n"
    return b"-----BEGIN EC PRIVATE KEY-----\n"+key_str.encode()+b"\n-----END EC PRIVATE KEY-----\n"

privateKey=SigningKey.generate()
publicKey=privateKey.verifying_key
print(privateKey.to_pem())
print(publicKey.to_pem())
print("Private Key: ",to_string(privateKey,False))
print("Public Key: ",to_string(publicKey,True))
signature=privateKey.sign("message".encode('utf-8'))
assert publicKey.verify(signature,"message".encode('utf-8'))
signing_keypair=(privateKey,publicKey)
# Creating a BlockChain
bitcoin=BlockChain()
'''
Making A Block and mining It
'''
# block=Block([Transaction("add1","add2","5")])
# print("Mining Block 1")
# bitcoin.addBlock(block)
# block=Block([Transaction("add2","add1","5")])
# print("Mining Block 2")
# bitcoin.addBlock(block)

## Trying To Change Information On BlockChain
# if len(bitcoin.chain[1].transactions):
# bitcoin.chain[1].transactions[0].amount=100

# Even If We Recalculate its hash we will need to correct all further hashes or next blocks...
# bitcoin.chain[1].hash=bitcoin.chain[1].generateHash()



# If Data is tampered return False


# print(bitcoin)
tx=Transaction(publicKey,'add2',100)
tx.sign(signing_keypair)
bitcoin.addTransaction(tx,public_key=publicKey)
tx=Transaction(publicKey,'add3',200)
tx.sign(signing_keypair)
bitcoin.addTransaction(tx,public_key=publicKey)


print("Mining Pending Transactions")
# address add3 starts mining to get reward of 100 bitcoin
# bitcoin.minePendingTransactions("add3")
# the user with wallet ID {publicKey} will mine transactions which contains the reward transaction of add3
bitcoin.minePendingTransactions(publicKey)

print("Balance Of User add3:",bitcoin.getBalanceOfAddress(publicKey))
print("IS BlockChain Valid??",bitcoin.isChainValid(publicKey))
