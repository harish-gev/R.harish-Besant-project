import datetime
x=datetime.datetime.now()
print(x)

print("welcome to BCA ATM")
print("insert your ATM cord")
bca_bank_balance=40500
pin=12345

#user_input=(input("What Bank you want:" )).lower().strip()
#1th
#if user_input=="" or user_input=="indian overseas bank":
print("1.show balance")
print("2.withdraw a amount")
print("3.deposite")
user=(input("Enter your choice:")).lower().strip()
if user=="1" or user=="show balance":
       print(f"your current  balance RS.{bca_bank_balance}")
elif user=="2" or user=="withdraw a amount":
          withdraw=int(input("Enter your amount:"))
          if withdraw <=40500:
             pin=(input("Enter your pin no:")).lower().strip()
             if pin==pin:
                  print("withdraw sucessflly")
                  current_balance=withdraw-bca_bank_balance
                  print(f"your current balance is  RS.{current_balance}")
             else:
                  print("Woring pin No") 
          else:
            print("bank balance low")
            print("input valed amount")
elif user=="3" or user=="deposite":        
         deposite=int(input("enter your amount :"))
         total=bca_bank_balance+deposite
         print("deposited succesfilly")
         print(f"your current balance is.{total}")
 
else:
  print("invaled spling or system error")
