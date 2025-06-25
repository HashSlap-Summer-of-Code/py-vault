#!/usr/bin/env python3



import sys
from bitcoinlib.wallets import Wallet as BtcWallet
from eth_account import Account

def generate_bitcoin_wallet():
    wallet = BtcWallet.create(name='MyBTCWallet', keys='create', witness_type='segwit', db_uri=':memory:')
    key = wallet.get_key()
    print("=== Bitcoin Wallet ===")
    print(f"Address     : {key.address}")
    print(f"Private Key : {key.wif}")

def generate_ethereum_wallet():
    acct = Account.create()
    print("=== Ethereum Wallet ===")
    print(f"Address     : {acct.address}")
    print(f"Private Key : {acct.key.hex()}")

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["bitcoin", "ethereum"]:
        print("Usage: python wallet-generator.py [bitcoin|ethereum]")
        return

    if sys.argv[1] == "bitcoin":
        generate_bitcoin_wallet()
    else:
        generate_ethereum_wallet()

if __name__ == "__main__":
    main()
