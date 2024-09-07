#Gaurab Baral, baralg1_Lab2
#This is the Customer Class
class Customer:
    def __init__(self, name: str, opening_balance: float, customer_type: str = "Bronze"): #This is the constructor
        self.name = name
        self.opening_balance = opening_balance
        self.customer_type = customer_type
        self.closing_balance = 0

    def calculateClosingBalance(self):              #this method calculates the closing balance
        self.closing_balance = 1.125 * self.opening_balance
        return self.closing_balance

    def setClosingBalance(self):#this method sets the closing balance
        self.closing_balance = self.calculateClosingBalance()

    def determineCustomerType(self):     #this method determines the type of customer based on the closing balance
        if self.closing_balance > 150000:
            self.customer_type = "Diamond"
        elif 100000 <= self.closing_balance <= 150000:
            self.customer_type = "Gold"
        elif 90000 <= self.closing_balance < 100000:
            self.customer_type = "Silver"

    def setCustomerType(self):      #this method sets the type of the customer
        self.determineCustomerType()

    def displayTabularInfo(self):   #this method displays the tabulated value with proper indentation
        print("{:<20} {:<15} {:>15.2f} {:>15.2f} {:>15.2f}".format(
            self.name, self.customer_type, self.opening_balance, (self.closing_balance - self.opening_balance),
            self.closing_balance))


while True: #this loop is to check if the number of customers is entered in integer or not
    try:
        total_customers = int(input("Enter the number of customers you have in this bank: "))
        if total_customers <=0:
            print("Re-Enter the number of customers in the bank")
            continue
        if((type(total_customers)) == int):
            break;
    except:
        print("Please re-enter with an integer value")
customers_list = []
for i in range(1,total_customers+1):
    name = input("Enter Customer%d's name: "%(i))
    while True: #this loop is to check if the value is integer or not and to check if it is more than $50 and less than $200000000
        try:
            opening_balance = float(input("Enter customer%.f's opening balance: "%(i)))
            if(opening_balance >= 50 and opening_balance <= 200000000):
                break;
            else:
                print("Re-enter a value with balance more than $50 and less than $200000000")
        except:
            print("Re-enter with a float value")


    customer = Customer(name,opening_balance)       #this creates the customer
    customer.setClosingBalance()
    customer.setCustomerType()
    customers_list.append(customer) #this has a list with Customer class data types

print("{:<20} {:<15} {:>15} {:>15} {:>15}".format("Customer Name","Customer Type","Opening($)","Interest($)","Closing($)"))
print("*************************************************************************************")
for cust in customers_list:                 #this is to print out all values of customers using the display tab
    cust.displayTabularInfo()


print("*************************************************************************************")

#output:
#Enter the number of customers you have in this bank: 6
#Enter Customer1's name: Victoria Adams
#Enter customer1's opening balance: 56798.67
#Enter Customer2's name: San Jonah
#Enter customer2's opening balance: 89763.69
#Enter Customer3's name: Kingsley James
#Enter customer3's opening balance: 897631.45
#Enter Customer4's name: Samuel Adams
#Enter customer4's opening balance: 7889.89
#Enter Customer5's name: Tom Hoyes
#Enter customer5's opening balance: 99098
#Enter Customer6's name: Tony Max
#Enter customer6's opening balance: 120000
#Customer Name        Customer Type        Opening($)     Interest($)      Closing($)
#*************************************************************************************
#Victoria Adams       Bronze                 56798.67         7099.83        63898.50
#San Jonah            Gold                   89763.69        11220.46       100984.15
#Kingsley James       Diamond               897631.45       112203.93      1009835.38
#Samuel Adams         Bronze                  7889.89          986.24         8876.13
#Tom Hoyes            Gold                   99098.00        12387.25       111485.25
#Tony Max             Gold                  120000.00        15000.00       135000.00
#*************************************************************************************