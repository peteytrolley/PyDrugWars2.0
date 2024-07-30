#! python3
# PyDrugWars2-0 - Remake of classic Dope/Drug Wars game with python

import random
from tkinter import *


def market():
    coke_price = random.randint(300, 1250)
    heroin_price = random.randint(450, 2000)
    weed_price = random.randint(20, 165)
    xany_price = random.randint(3, 45)
    shroom_price = random.randint(10, 95)
    lsd_price = random.randint(75, 245)
    crack_price = random.randint(120, 595)
    hash_price = random.randint(95, 325)

    prices = {'cocaine': coke_price, 'heroin': heroin_price, 'weed': weed_price, 'xany': xany_price,
              'shroom': shroom_price, 'lsd': lsd_price, 'crack': crack_price, 'hashish': hash_price}
    return prices


PRICES = market()

INVENTORY = {'cocaine': 0, 'heroin': 0, 'weed': 0, 'xany': 0,
             'shroom': 0, 'lsd': 0, 'crack': 0, 'hashish': 0}
WALLET = 500

DAY = 30


def change_day(DAY, PRICES):
    DAY -= 1
    if DAY < 0:
        T3.delete('1.0', END)
        T2.delete('1.0', END)
        T.delete('1.0', END)
        T.insert(INSERT, 'GAME OVER')
        if WALLET >= 1000000:
            T.insert(INSERT, f' - YOU WIN\nMoney earned: ${WALLET:,.2f}')
        else:
            T.insert(INSERT, f' - YOU LOSE!\nMoney earned: ${WALLET:,.2f}')
    elif DAY >= 0:
        T4.delete('1.0', END)
        T4.insert(INSERT, str(DAY))
    PRICES = market()
    T2.delete('1.0', END)
    T3.delete('1.0', END)
    T2.insert(INSERT, '***MARKET PRICES***\n')
    mugged()
    for price in PRICES:
        T2.insert(INSERT, f"{price} ${PRICES[price]}\n")
    if PRICES['cocaine'] < 325:
        T3.insert(INSERT, 'A huge coke shipment just landed.\nPrices are bottoming out!')
    elif PRICES['cocaine'] > 1220:
        T3.insert(INSERT, 'DEA seized a HUGE coke shipment.\nPrices are through the roof!')
    elif PRICES['heroin'] < 490:
        T3.insert(INSERT, 'New heroin supplier around town.\nHeroin prices are way down!')
    elif PRICES['heroin'] > 1910:
        T3.insert(INSERT, 'New anti-heroin law was passed.\nPeople panicking, prices up!')
    elif PRICES['weed'] < 27:
        T3.insert(INSERT, 'Giant shipment of weed from Cali\njust arrived. Prices are low!')
    elif PRICES['weed'] > 152:
        T3.insert(INSERT, 'A huge grow operation was raided.\nWeed prices are astronomical!')
    elif PRICES['xany'] < 7:
        T3.insert(INSERT, 'Big shipment of pills from Mexico\njust in. Prices are super low!')
    elif PRICES['xany'] > 39:
        T3.insert(INSERT, 'Illegal pharmacy just shut down. \nPill prices are outrageous!')
    elif PRICES['shroom'] < 18:
        T3.insert(INSERT, "Shrooms are flooding the market!\n Get 'em while prices are low!")
    elif PRICES['shroom'] > 85:
        T3.insert(INSERT, 'DEA got to the shroom farm.\nShroom prices are high!')
    elif PRICES['lsd'] < 85:
        T3.insert(INSERT, 'New budget LSD is on the\nmarket. Prices are down!')
    elif PRICES['lsd'] > 232:
        T3.insert(INSERT, 'The Chemist got busted!\nLSD prices are crazy high!')
    elif PRICES['crack'] < 137:
        T3.insert(INSERT, 'Lots of new cooks in town\nCrack prices are way low!')
    elif PRICES['crack'] > 550:
        T3.insert(INSERT, 'Local police are busting\ncrack dealers. Prices up!')
    elif PRICES['hashish'] < 109:
        T3.insert(INSERT, 'The Morroccan connect is in\ntown. Hash prices are low!')
    elif PRICES['hashish'] > 305:
        T3.insert(INSERT, 'Giant hash seizure in the\nport. Hash prices are spiking!')


def get_amount():
    amount = amountVar.get()
    if amount == 0:
        T3.insert(INSERT, "Input an amount\n")
    return amount


def get_drug():
    for selected in drugList.curselection():
        drug = drugList.get(selected)
        return drug


def mugged(WALLET):
    mugger = random.randint(1, 28)
    if mugger == 2 or mugger == 10:
        T.delete('1.0', END)
        T3.delete('1.0', END)
        WALLET -= (WALLET/2)
        T3.insert(INSERT, 'You got mugged!\nLucky for your prison wallet ;)\n')
        T.insert(INSERT, 'INVENTORY:\n')
        for drug in INVENTORY:
            T.insert(INSERT, f"{INVENTORY[drug]} {drug} \n")
        T.insert(INSERT, f"You have ${WALLET:,.2f}\n")


def busted(WALLET):
    cops = random.randint(1, 28)
    if cops == 2 or cops == 10:
        T.delete('1.0', END)
        T3.delete('1.0', END)
        WALLET -= (WALLET/3)
        T3.insert(INSERT, "Busted by the COPS!\nA little bribe helped...")
        T.insert(INSERT, 'INVENTORY:\n')
        for drug in INVENTORY:
            T.insert(INSERT, f"{INVENTORY[drug]} {drug} \n")
        T.insert(INSERT, f"You have ${WALLET:,.2f}\n")


def drug_cost():
    global WALLET
    global INVENTORY
    global PRICES
    drug = get_drug()
    units = get_amount()
    T2.insert(INSERT, '***MARKET PRICES***\n')
    for price in PRICES:
        T2.insert(INSERT, f"{price} ${PRICES[price]}\n")
    drugCost = PRICES[drug] * units
    if not BSList.curselection():
        T3.insert(INSERT, "Select Buy or Sell\n")
    for selected in BSList.curselection():
        BSList.get(selected)
        if selected == 1 and units > INVENTORY[drug]:
            T3.insert(INSERT, "You ain't got the drugs!\n")
            drugCost = 0
            T.insert(INSERT, 'INVENTORY:\n')
            for drug in INVENTORY:
                T.insert(INSERT, f"{INVENTORY[drug]} {drug} \n")
            T.insert(INSERT, f"You have ${WALLET:,.2f}\n")
        elif selected == 0 and WALLET < drugCost:
            T3.insert(INSERT, "Not enough cash! Dealer is angry >:|\n")
            T.insert(INSERT, 'INVENTORY:\n')
            for drug in INVENTORY:
                T.insert(INSERT, f"{INVENTORY[drug]} {drug} \n")
            T.insert(INSERT, f"You have ${WALLET:,.2f}\n")
        elif selected == 0 and WALLET >= drugCost:
            WALLET -= drugCost
            INVENTORY[drug] += units
            T.insert(INSERT, 'INVENTORY:\n')
            for drug in INVENTORY:
                T.insert(INSERT, f"{INVENTORY[drug]} {drug} \n")
            T.insert(INSERT, f"You have ${WALLET:,.2f}\n")
        elif selected == 1:
            WALLET += drugCost
            INVENTORY[drug] -= units
            T.insert(INSERT, 'INVENTORY:\n')
            for drug in INVENTORY:
                T.insert(INSERT, f"{INVENTORY[drug]} {drug} \n")
            T.insert(INSERT, f"You have ${WALLET:,.2f}\n")



def main():
    T.delete('1.0', END)
    T3.delete('1.0', END)
    try:
        drug_cost()
        busted()
    except KeyError:
        T3.insert(INSERT, 'Choose a drug\n')
    T2.delete('1.0', END)
    T2.insert(INSERT, '***MARKET PRICES***\n')
    for price in PRICES:
        T2.insert(INSERT, f"{price} ${PRICES[price]}\n")


root = Tk()
root.title('PyDrugWars 2.0')
root.geometry('550x600')

f1 = Frame(root)
f1.grid(row=0, column=0)

f2 = Frame(root)
f2.grid(row=1, column=0)

f3 = Frame(root)
f3.grid(row=1, column=1)

f4 = Frame(root)
f4.grid(row=0, column=3)

T2 = Text(root, fg='lightgreen', bg='black', height=9, width=24)
T2.grid(row=0, column=1, sticky='w')
T2.insert(INSERT, '***MARKET PRICES***\n')
for price in PRICES:
    T2.insert(INSERT, f"{price} ${PRICES[price]}\n")

T = Text(f3, fg='yellow', bg='black', font='arial', height=12, width=32)
T.grid(row=1, column=0)

T3 = Text(f3, fg='lightgreen', bg='black', font='arial', height=2, width=32)
T3.grid(row=0, column=0)

dayLabel = Label(f4, text='Days left:')
dayLabel.grid(row=0, column=0)

T4 = Text(f4, fg='red', bg='black', font='arial', height=1, width=3)
T4.grid(row=1, column=0)

amountVar = IntVar()
drugAmount = Entry(root, textvariable=amountVar, font=('calibre', 10, 'normal'), width=15)
drugAmount.grid(row=3, column=0)

amountLabel = Label(root, text='Quantity of drugs to buy:')
amountLabel.grid(row=2, column=0)

cityLabel = Label(f1, text='Change city:')
cityLabel.grid(row=0, column=0)

drugList = Listbox(f2, selectmode='single', exportselection=0, height=8, width=15, bg='black', fg='yellow')
for item in INVENTORY:
    drugList.insert(END, item)
drugList.grid(row=1, column=0, padx=20)

drugLabel = Label(f2, text='Pick your drug...')
drugLabel.grid(row=0, column=0)

BSLabel = Label(f2, text='Buy/Sell?      ')
BSLabel.grid(row=2, column=0)

BSList = Listbox(f2, selectmode='single', exportselection=0, height=2, width=6, bg='black', fg='yellow', font='arial')
BSList.insert(1, '--Buy--')
BSList.insert(2, '--Sell--')
BSList.grid(row=3, column=0, padx=20, sticky='w')

startbtn = Button(root, command=main, text='Complete Transaction', bg='grey', fg='green')
startbtn.grid(row=4, column=0)

citybtn1 = Button(f1, command=change_day, text='Miami')
citybtn1.grid(row=1, column=0, sticky='w')

citybtn2 = Button(f1, command=change_day, text='Houston')
citybtn2.grid(row=2, column=0, sticky='w')

citybtn3 = Button(f1, command=change_day, text='New York')
citybtn3.grid(row=3, column=0, sticky='w')

citybtn4 = Button(f1, command=change_day, text='Los Angeles')
citybtn4.grid(row=4, column=0, sticky='w')

citybtn5 = Button(f1, command=change_day, text='Chicago')
citybtn5.grid(row=5, column=0, sticky='w')

citybtn6 = Button(f1, command=change_day, text='Vancouver')
citybtn6.grid(row=6, column=0, sticky='w')

top = Toplevel(root)
top.geometry("750x250")
top.title("Welcome to PyDrugWars 2.0")
Label(top, text="""You will begin with $500. The goal is to make $1,000,000 before 30 days\n
passes. Watch out for muggers and cops!""", font='arial').place(x=50, y=80)
top.wm_transient(root)

root.mainloop()

# TODO: DISPLAY CITY, Clear all windows after 30 days has passed (should display GAME OVER and WINNER or LOSER)
