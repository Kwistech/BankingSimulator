# BankingSimulator
Bank account simulator that can test banking practices over time

## Features ##

### Accounts ###

User can choose from three different account types:
  1. *Savings*
  2. *Chequings*
  3. *Tax Free*

*Savings* Account Details:
Interest Rate: 0.75%, Withdraws: 5, Amount Limit:  $250 000

*Chequings* Account Details:
Interest Rate: 0.50%, Withdraws: 20, Amount Limit: $1 000 000

*Tax Free* Acount Details:
Interest Rate: 2.50%, Withdraws: 1, Amount Limit:  $50 000

###### Note: The above account details are defaults; you can change them in accounts.py.

### Actions ###

User can do common banking actions such as:
+ Open an account
+ Close an account
+ Make deposits
+ Make withdraws
+ Save account

#### Simulation ####

User can simulate how much money an account will accrue over time. The user can choose what account they want to simulate, what interest calculation they want, and how long they want the simulation to run for.
```
Banking Simulation
-------------------
Which account do you want to simulate? 
What interest type [simple, compound]: 
How many months do you want to run the simulation? 
```

The result will look like the following:

```
Simple interest calculation:
A = $1003.12

Account: savings
Principle: $1000
Interest Rate: 0.75%
Months: 5

Press Enter to continue: 
```

## Program Split ##

**main.py** imports both **accounts.py** (contains the Account class) and **general_functions.py** (contains 'help' function and error checking function). 

**accounts.py** imports **interest_calcs.py** to calculate interest on user account.

For more info, check the [project's wiki](https://github.com/Kwistech/BankingSimulator/wiki) 
