# Import dependencies
import subprocess
import sys
import json
import os
from dotenv import load_dotenv
from bit.wallet import PrivateKeyTestnet, NetworkAPI
from web3 import Account, Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
from constants import *

# Connect to local POA network moneylegos
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv('mnemonic')

# Connection Status to ETH node
print(f"Connected to Ethereum node {'http://127.0.0.1:8545'}: {w3.isConnected()}")
print(f"ChainId : {w3.eth.chainId}")

# Derives wallet information, returning a json output.
def derive_wallets(mnemonic, coin):
    
    command = './derive -g --mnemonic=\'' + mnemonic + '\' --coin=' + coin + ' --numderive=3 --cols=path,address,privkey,pubkey --format=json'
    
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    
    output, err = p.communicate()
    p_status = p.wait()
    
    keys = json.loads(output)
    
    return keys

# Function that converts privkey strings from derive_wallets to account object.
def priv_key_to_account(coin, priv_key):
    
    if coin == BTCTESTNET:
        account = PrivateKeyTestnet(priv_key)
    
    elif coin == ETH:
        account = Account.privateKeyToAccount(priv_key)
    
    return account

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, to, amount):
    
    if coin == BTCTESTNET:
        txinfo = PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, 'btc')], fee=1)
    
    elif coin == ETH:
        wei_amount = int(amount*1000000000000000000)
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": to, "value": wei_amount}
        )
        txinfo = {'from': account.address,
                  'to': to,
                  'value': w3.toWei(int(wei_amount),'wei'),
                  'gasPrice': w3.eth.gasPrice,
                  'gas': gasEstimate,
                  'nonce': w3.eth.getTransactionCount(account.address),
                  'chainId': 707
                 }
    return txinfo

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, to, amount):
    
    tx = create_tx(coin, account, to, amount)
    
    if coin == BTCTESTNET:
        signed = account.sign_transaction(tx)
        send = NetworkAPI.broadcast_tx_testnet(signed)
        print(f"{amount} tBTC sent from : {account.address} to : {to}")

    elif coin == ETH:
        signed = account.sign_transaction(tx)
        send = w3.eth.sendRawTransaction(signed.rawTransaction)
        print(f'{w3.fromWei(amount, "ether")} eth sent from : {account.address} to : {to}') 
        print(f'Signed transaction : {signed.rawTransaction.hex()}')
        print(f'Signed transaction hash : {signed.hash.hex()}')
    
    return send

def main():
    while True:
        user_command = input(f'What would you like to do? Commands: press enter to send transaction or type in {"quit"} ')
        
        if user_command == 'quit':
            return('program terminated')
        
        coin = input('coin: btc-test or eth ')
        child_index = input('Index of child key: pick 0, 1, or 2 ')
        to = input('send to address: ')
        amount = float(input('amount to send: '))
        
        # Dictionary object to store the output from `derive_wallets'
        coin_derive = derive_wallets(mnemonic, coin)
        
        # Obtains privkey from derive_wallets dictionary object
        priv_key = coin_derive[int(child_index)]['privkey']
        
        # Converts privkey to account
        account = priv_key_to_account(coin, priv_key)
        
        send_tx(coin, account, to, amount)
        
    main()

main()


