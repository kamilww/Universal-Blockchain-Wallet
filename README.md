# Universal-Blockchain-Wallet
BTCTESTNET and ETH test wallet using hd-wallet-derive

## Dependencies
PHP (needed to install hd-wallet-derive)

https://www.php.net

hd-wallet-derive

https://github.com/dan-da/hd-wallet-derive

moneylegos Proof of Authority Geth testnet

https://github.com/kamilww/moneylegos

bit

https://ofek.dev/bit/

web3

https://github.com/ethereum/web3.py

## Installation
1. Install PHP, bit, and web3

2. Set up and launch Geth testnet "moneylegos", which is available in github package

3. Github package contains hd-wallet-derive. cd into the hd-wallet-derive
  
4. Use the following commands to install hd-wallet-derive
    
    curl https://getcomposer.org/installer -o installer.php
    
    php installer.php
    
    php composer.phar install
    
5. Create a symlink so you could call hd-walet-derive using './derive' in the source code
    
    Mac: Run the following command: ln -s hd-wallet-derive/hd-wallet-derive.php derive
    
    PC: Open up Git-Bash as an administrator (right-click on Git-Bash in the start menu). Within bash, run the command export MSYS=winsymlinks:nativestrict
        
        Run the following command: ln -s hd-wallet-derive/hd-wallet-derive.php derive

6. cd back into the main folder, and create a .env file with a valid mnemonic phrase. You could use the following to generate a random mnemonic: ./derive -g --gen-words=12 

## Derive Wallet
Use the command 'python wallet.py' to launch CLI interface and follow the CLI prompts:
<img width="916" alt="Screen Shot 2021-08-12 at 8 00 16 PM" src="https://user-images.githubusercontent.com/40152804/129284707-62f6312a-95bb-41c3-b2f6-b03fe83c352d.png">

BTCTESTNET Transaction Confirmation:
<img width="1540" alt="Screen Shot 2021-08-12 at 8 08 41 PM" src="https://user-images.githubusercontent.com/40152804/129285192-e180cc77-134c-4c30-aba5-1652299b6a73.png">

ETH Transaction Confirmation:
<img width="1331" alt="Screen Shot 2021-08-12 at 8 10 25 PM" src="https://user-images.githubusercontent.com/40152804/129285311-c4bf059e-0386-4068-b12f-d9411c527827.png">


