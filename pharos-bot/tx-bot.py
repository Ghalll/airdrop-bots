import os
import time
import random
from web3 import Web3
from web3.exceptions import TransactionNotFound
from dotenv import load_dotenv

load_dotenv()

web3 = Web3(Web3.HTTPProvider(os.getenv('RPC_URL')))
private_key = os.getenv('PRIVATE_KEY')
account = web3.eth.account.from_key(private_key)

target_address = [
    "0x428e60934c0321badb0c1fbb4b35990e5ad1b61d",
    "0xfd69b50de31b9d411e12930e063eef63193698f7",
    "0xbdb0eb73376f55bc025332b1b5678fb0ef2736ef",
    "0xd17512b7ec12880bd94eca9d774089ff89805f02",
    "0xfe1bedc2e23f70c7115e70dfc1eace83884502f0",
    "0xf1415aca56141385d375a13e9ed71dcd9f60cd3e",
    "0x3541423f25a1ca5c98fdbcf478405d3f0aad1164",
    "0xf7dec0ed9282e4a9112031acb6ab1f6d3ee78840",
    "0xf2e30da419441358a6cbebf7976c3e34e7e315d4",
    "0xeeaeee18de4f328c1072a9423923c9ba3945e42c",
    "0xd69f40639b40afee4fe8a82eb1e5e8c4636005c5",
    "0xa480ec209488ea4670ecd5eab383b6f138647279",
    "0xe68a04f4abd52427043c198d4813597d6c874669",
    "0xf44440d6654a4fc52e3d697e03260cd2230da44a",
    "0xe1b7d54079246456de3b4e8f2ada9df8898e948f",
    "0xf3cd9a47afff96883851db4c65f6496bc4cc1996",
    "0xb3ca49fe7befcb905bf43b772c90eb493ad2e64b",
    "0x85307365e61a1808e014521fb8176c7a344ce24b",
    "0xfd01579be0632bcd3f0f3efa116889e0d69c360c",
    "0xb80b680d4c0abc9810a4241fec71435fe2b47ba4",
    "0xeb782627d3922f05b902f4938978541d4ec327ae",
    "0xfbab928f972ff1744a1b957478495808f1f28358",
    "0xf67fc70fbc4fba418735987d090560a5c6d115d0",
    "0xeffc739387962c0d8d1f53a8289d5153b4e658d0",
    "0xf6f04c02392d385c2ec2cca162ae0679adbf3525",
    "0xf844e6a46a1d89d33a01b67ff207c36eaae2a903",
    "0x512a2773572e9127223e80a2ec9c9015067c4937",
    "0xcdad6a900f15189a187689187aa6607b8566ac13",
    "0xceb56789f838451a58c3ea494fef5c7795060bab"
]

def send_tx(to_address, amount, retries=3):
  for attempt in range(1, retries + 1):
    try:
      nonce = web3.eth.get_transaction_count(account.address)
      tx = {
        'nonce' : nonce,
        'to' : to_address,
        'value' : web3.to_wei(amount, 'pharos'),
        'gas' : 21000, 
        'gasprice' : web3.to_wei('2', 'gwei'),
        'chainId' : web3.eth.chain_id
      }
      signed_tx = web3.eth.account.sign_transaction(tx, private_key)
      tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
      receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
      return receipt.transactionHash.hex()
    except (ValueError, TransactionNotFound) as e:
      print(f"Attempt {attempt} failed: {e}")
      if attempt == retries:
          raise e
      time.sleep(5)


def main():
  amount = float(os.getenv('SEND_AMOUNT'))
  num_tx = int(os.getenv('NUM_TX'))
  delay = int(os.getenv('DELAY_SECONDS'))

  balance = web3.eth.get_balance(account.address)
  print(f"Wallet: {account.address} | Balance: {web3.from_wei(balance, 'pharos')} PHRS")
  if balance < web3.to_wei(amount * num_tx * 1.1, 'ether'):
      print("Balance tidak cukup! Claim dari faucet: https://testnet.pharosnetwork.xyz/")
      return
  
  for i in range(num_tx):
    to_address = random.choice(target_address)
    try:
        tx_hash = send_tx(to_address, amount)
        print(f"Tx {i+1}/{num_tx} dikirim ke {to_address[:6]}... | Hash: {tx_hash}")
        print(f"Cek di: https://sepolia.etherscan.io/tx/{tx_hash}")
    except Exception as e:
       print(f"Tx {i+1} gagal: {e}")
    time.sleep(delay)

if __name__ == "__main__":
   main()
      
