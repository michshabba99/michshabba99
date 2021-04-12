
# Final Project
# creating an inventory system.

import os
import fileinput
import csv
# import pandas as pd

def menuDisplay():
    print('=============================')
    print('= Inventory Management Menu =')
    print('=============================')
    print('(1) Display Manufacturer List')
    print('(2) Display Price List')
    print('(3) Service DatesList')
    print('(4) Full Inentory')
    print('(5) Print Inventory Report')
    print('(99) Quit')
    CHOICE = int(input("Enter choice: "))
    menuSelection(CHOICE)

def menuSelection(CHOICE):
    if CHOICE == 1:
        displaymanufacturerlist()
    elif CHOICE == 2:
        displaypricelist()
    elif CHOICE == 3:
        ServiceDatesList()
    elif CHOICE == 4:
        FullInentory()
    elif CHOICE == 5:
        printInventory()
    elif CHOICE == 99:
        exit()

"""def addInventory():
    InventoryFile = open('Inventory.txt', 'a')
    print("Adding Inventory")
    print("================")
    item_description = input("Enter the name of the item: ")
    item_quantity = input("Enter the quantity of the item: ")
    InventoryFile.write(item_description + '\n')
    InventoryFile.write(item_quantity + '\n')
    InventoryFile.close()
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()"""
def displaymanufacturerlist():
    csvfile=open('ManufacturerList.csv','r', newline='')
    obj=csv.reader(csvfile)
    for row in obj:
        print (row)
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
        
def displaypricelist():
    csvfile=open('PriceList.csv','r', newline='')
    obj=csv.reader(csvfile)
    for row in obj:
        print (row)
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
        
def ServiceDatesList():
    csvfile=open('ServiceDatesList.csv ','r', newline='')
    obj=csv.reader(csvfile)
    for row in obj:
        print (row)
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def FullInentory():
    f = open('ManufacturerList.csv', 'r', newline='')
    fl = open('PriceList.csv', 'r', newline='')
    rd= csv.reader(fl)
    for rw in rd:
        reader = csv.reader(f)
        for row in reader:
            rcd=row.append(rw)
    print(rcd)
CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
if CHOICE == 98:
    menuDisplay()
else:
    exit()
    """data1 = pd.read_csv('ManufacturerList.csv')
    data2 = pd.read_csv('PriceList.csv')
    # using merge function by setting how='right'
    output3 = pd.merge(data1, data2,
                       on=data1[0],
                       how=data2[0])
    # displaying result
    print(output3)"""
''' manufacturerlistfile = open('ManufacturerList.csv', 'r')       
    product_result = {record[0]: record for record in csv.reader(manufacturerlistfile)}

    infile = open('PriceList.csv', 'r')
    outfile = open('FullInventory.csv', 'w')
    readerr = csv.reader(infile)
    writerr = csv.writer(outfile, readerr.row)
    #writer.writeheader()
    for item in reader:
        record = product_result.get(item[0], None)
        if record:
            item[1] = record[5]  # ???
            """item[] = record[' CostPrice']"""
        else:
            item[1] = None
            item[0] = None
            writerr.writerow(item)
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()'''
f = open('ManufacturerList.csv', 'r', newline='')
fl = open('PriceList.csv', 'r', newline='')
rd= csv.reader(fl)
for rw in rd:
    reader = csv.reader(f)
    for row in reader:
        rcd=row.append(rw)
print(rcd)
CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
if CHOICE == 98:
    menuDisplay()
else:
    exit()

def printFullInventory():
    InventoryFile = open('ManufacturerList.csv', 'r')
    item_description = InventoryFile.readline()
    print('Current Inventory')
    print('-----------------')
    while item_description != '':
        item_quantity = InventoryFile.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        print('Item:     ', item_description)
        print('Quantity: ', item_quantity)
        print('----------')
        item_description = InventoryFile.readline()
    InventoryFile.close()

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()


def removeInventory():
    print("Removing Inventory")
    print("==================")
    item_description = input("Enter the item name to remove from inventory: ")

    file = fileinput.input('Inventory.txt', inplace=True)

    for line in file:
         if item_description in line:
             for i in range(1):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    item_description
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def updateInventory():
    print("Updating Inventory")
    print("==================")
    item_description = input('Enter the item to update: ')
    item_quantity = int(input("Enter the updated quantity. Enter - for less: "))

    with open('Inventory.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('Inventory.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if item_description in line:
            for b in file[i+1:i+2]:
                value = int(b)
                change = value + (item_quantity)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('Inventory.txt', 'w') as f:
        for line in filedata:
            f.write(line)
                                            
                
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def searchInventory():
    print('Searching Inventory')
    print('===================')
    item_description = input('Enter the name of the item: ')
    
    f = open('Inventory.txt', 'r')
    search = f.readlines()
    f.close
    for i, line in enumerate(search):
        if item_description in line:
            for b in search[i:i+1]:
                print('Item:     ', b, end='')
            for c in search[i+1:i+2]:
                print('Quantity: ', c, end='')
                print('----------')
        
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
        
def printInventory():
    InventoryFile = open('Inventory.txt', 'r')
    item_description = InventoryFile.readline()
    print('Current Inventory')
    print('-----------------')
    while item_description != '':
        item_quantity = InventoryFile.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        print('Item:     ', item_description)
        print('Quantity: ', item_quantity)
        print('----------')
        item_description = InventoryFile.readline()
    InventoryFile.close()

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

menuDisplay()
