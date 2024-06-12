import pandas as pd

def printReceipt( name,  contact):

    purchases = pd.read_excel('purchaese.xlsx')
    total = 0
    for x in purchases.Price:
        total+= x
    print('*'*50)

    print("Name: "+ str(name))
    print("Contact: "+ str(contact))


    print('*'*50)
    print(purchases)

    print('='*50)

    print(" "*30+"Total")
    print(" "*30+str(total))

    print('='*50)




    print("Thank you for shopping!!")
    print('*'*50)

def main():
    print("Let's take your details for receipt:")
    name = str(input("Name: "))
    contact = int(input("Contact: "))
    printReceipt(name, contact)

if __name__=="__main__":
    main()