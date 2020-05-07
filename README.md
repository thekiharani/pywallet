# Minimal virtual wallent implementation with Python
The application comes bundled with virtual environment `wallet_env` which contains all the dependencies. This allows a developer to run with with less hustle. Additionally, it comes with a `requirements.txt` file with all the dependencies, which allow the dev to create a new virtual environment with all the dependencies or install the dependencies in their global python (Not recommeded).

## Getting started
### Using the `wallet_env` environment
- Clone the repo either using SSH: `git clone git@github.com:thekiharani/pywallet.git` OR using HTTPS: `git clone https://github.com/thekiharani/pywallet.git`
- Change the dir: `cd pywallet`
- Activate the virtual environment: `source wallet_env/bin/activate`
- Run the app: `python run.py`
The app should now be running on dev server: [Localhost port:5000](http://127.0.0.1:5000/)

### Installing the dependencies from `requirements.txt`
This assumes that the developer is conversant with Python and virtual environments
- Create and activate a virtual environment
- Clone the repo either using SSH: `git clone git@github.com:thekiharani/pywallet.git` OR using HTTPS: `git clone https://github.com/thekiharani/pywallet.git`
- Change the dir: `cd pywallet`
- Install the dependencies from `requirements.txt` file: `pip install -r requirements.txt`
- Run the app: `python run.py`
The app should now be running on dev server: [Localhost port:5000](http://127.0.0.1:5000/)

## What the app does so far
- User registration with hashed password
- User login and logout
- Users can send and receive money from their virtual wallets
- Users can only transact if they are authenticated. The wallet route is protected
- User can see their balance and transaction history. The transaction history is devided into *Money Sent* and *Money Received* sections

## What can be improved
- Password reset and recovery
- Email and SMS notifications
- Real-time web notification and balance update when someone receive money