import pandas as pd

def printReceipt( name,  contact):
    file = open('reciept.txt', "a")
    purchases = pd.read_excel('purchaese.xlsx')
    total = 0
    for x in purchases.Price:
        total+= x
    file.write('*'*50)

    file.write("\nName: "+ str(name))
    file.write("\nContact: "+ str(contact)+"\n")


    file.write('*'*50)
    file.write("\n"+ str(purchases) + "\n")

    file.write('='*50)

    file.write("\n" + " "*30 +"Total\n")
    file.write(" "*30+str(total)+"\n")

    file.write('='*50)




    file.write("\nThank you for shopping!!\n")
    file.write('*'*50)

def main():
    print("Let's take your details for receipt:")
    name = str(input("Name: "))
    contact = int(input("Contact: "))
    printReceipt(name, contact)
    print(" Get receipt.txt file in directory")

if __name__=="__main__":
    main()