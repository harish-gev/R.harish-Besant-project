
import mysql.connector

mydb= mysql.connector.connect(
    host= "localhost",
    user_input= "root",
    passwd= "(17516*17516)"
)
print("Holiday traveles")

print("**TOP 10 TORIEST PLACES IN TAMIL NADU")
print("1.Rameshwaram ")
print("2.Yercardu")
print("3.Kodaikanal")
print("4.Ootu")
print("5.Auroville")
print("6.Hogenkkal")
print("7.mahabaliburam")
print("8.kanyakumari ")
print("9.coimbatore")
print("10.mudumali national park")

def rameshwaram ():
    print("popular Ramashwaram packages")
    print("1.Rameswaram,kanyakumari")   
    print("2.madurai,rameswaram,kanyakumari")
    print("3.Thanjuvar,Rameswaram,Munnar,Ootu")
def yercardu():
    print(" popular Yercardu packages")
    print("1.Yercadu ")
    #print("")
def kodaikanal():
    print("pacages:")
    print("1. Kodaikanal")
    print("2.Kodaikanal,mysour,ooty")
    print("3.Kodaikanal,munnor")
def ooty():
    print("pacages:")
    print("1.ooty")
def Auroville():    
    print("pacages:")
    print("2N/3D")
    print("1.singl pacage")
    
def Hogenkkal():
    print("avalable pacages")
    print("1.Hogenkkal,yercadu")
    print("2.Hogenkkal")
    print("3.Hogenkkal,yelagiri")


def mahabaliburam():
    print("popular pacage")
    print("1.chenni,mahabaliburam,pondichary,tanjoremadurai")
    print("2.chenni,mahabaliburam,pondichary,valankanni,")
    print("3.chenni,mahabaliburam,pondichary,")

def kanyakumari():
    
    print("popular pacages")
    print("1.maduri,rameswaram,kanyakumari")
    print("2.rameswaram,kunyakumari")

def coimbatore():
    print("popular pacages")
    print("only 1 pacage avalble ")
    print("1.coimbator")


def mudumali_national_park():

    print("popular pacages")
    print("only 1 pacage avalble ")    
    print("1.mudumali national park")    

user_input=(input("chose your tour place :")).lower().strip()



if user_input=="1" or user_input== "rameshwaram" :
    rameshwaram() 
    user=input("chouse your pacage:").lower().strip()

    if user=="1" or user==rameshwaram and user=="kanyakumari":
        print("2N/3D")
        print("60000")
        print(f"your total{user_input} tour bill Rs.6000")
    elif user=="2" or user=="madurai,rameswaram,kanyakumari":
        print("3N/4D")
        print("10,000")
        print(f"your total {user_input} bill Rs.10,000")    
    elif user=="3" or user=="Thanjuvar,Rameswaram,Munnar,Ootu":
        print("6N/7D")
        print("25000")
        print(f"your total {user_input} bill Rs.25,000")
    else:
        print("invaled or splling error")      
elif user_input=="2" or user_input== "yercardu":
    yercardu()
    user_input_yercardu=input("chouse your pacage:").lower().strip()

    if user_input_yercardu=="1"or user_input_yercardu=="yercardu":
        print("2N/3D")
        print(f"your total {user_input_yercardu} bill is RS.6,0000")
    else:
        print("invaled or splling error")   

elif user_input=="3" or user_input=="kodaikanal":
    kodaikanal()
    user_input_kodaikana=input("chouse your pacage:").lower().strip()

    if user_input_kodaikana=="1" or user_input_kodaikana=="Kodaikanal":
        print("2N/3D")
        
        print(f"your total {user_input_kodaikana} Tour bill is Rs.7,000")
    elif user_input_kodaikana=="2" or user_input_kodaikana=="Kodaikanal,mysour,ooty":
        print("4N/5D")
        print(f"your total {user_input_kodaikana} tour bill Rs.8,000")  
            
    elif user_input_kodaikana=="3" or user_input_kodaikana=="Kodaikanal,munnar":
        print("4N/5D")
        print("10,000")
        print(f"your total {user_input_kodaikana} bill is Rs.10,000")
    else:
        print("invaled or splling error")   
elif user_input=="4" or user_input== "ooty":
    ooty()
    print("2N/3D")
    print("your tottal bill is RS.5,500")

elif user_input=="5" or user_input=="Auroville":
    Auroville()
    print("2N/3D")
    print("your tottal Auroville tour bill  RS.4000")

elif user_input=="6" or user_input=="Hogenkkal":
    Hogenkkal()
    user_input=input("chouse your pacage:").lower().strip()

    if user_input=="1" or user_input==" Hogenkkal,yercadu":
        print("2N/3D")
        print(f"your total {user_input} tour bill is Rs.7000")
    elif user_input=="2" or user_input==  Hogenkkal:
        print("1N/2D")
        print(f"your total {user_input} tour bill is Rs.3000")
    elif user_input=="3"   or user_input=="Hogenkkal,yelagri":
        print("2N/3D")
        print(f"your total {user_input} tour bill Rs.10,000")
      
    else:
        print("invaled or splling error")    
elif user_input=="7"or  mahabaliburam:
    mahabaliburam()
    user_input=input("enter your choice:").lower().strip()

    if user_input=="1" or user_input=="chenni,mahabaliburam,pondichary,tanjoremadurai":
        print("7N/8D")
    
        print(f"your tottal {user_input} tour  bill Rs.20,000 ")
    elif user_input=="2" or user_input=="chenni,mahabaliburam,pondichary,valangani":
         print("6N/8D")
         print(f"your toyal {user_input} tour bill Rs.15,000")
    elif user_input=="3" or user_input=="chenni,mahabaliburam,pondichary,tanjoremadurai":
        print("3N/4D")
        print("your total {user_input} tour bill Rs.8,000")
    else:
        print("invaled or splling error")   
elif user_input=="8" or user_input==" kanyakumari":
    kanyakumari()
    user_input=input("enter your choice:").lower().strip()

    if user_input=="1" or user_input=="maduri,rameswaram,kanyakumari":
        print("3N/4D")
        print(f"your total {user_input} tour bill Rs.10,000")
    elif  user_input=="2" or user_input==",rameswaram,kanyakumari":
        print("2N/3D")
        print(f"your total {user_input} tour  bill Rs.6,000 ")
    else:
        print("invaled or splling error")      

elif user_input=="9" or user_input=="coimbatore" :
    coimbatore()
    user_input=input("enter your choice:").lower().strip()

    if user_input=="1" or user_input=="coimbatore":
        print("2D/3N")
        print(f"your tottal  bill RS.5,000")
    else:
        print("invaled or splling error")    
elif user_input=="10" or user_input== "mudumali_national_park":
    mudumali_national_park()
    user_input=input("enter your choice:").lower().strip()

    if user_input=="1" or user_input=="mudumali national park":
        print(f"your tottal mudumali national park bill is Rs.12,500")
    else:
        print("invaled or splling error")   
        

else:
    print("your input is incoract (or) not avalable")













