mor="1.morning tiffen menu"
lun="2.lunch menu"
den="3.dinner menu"
des=("4.desert menus")
print(mor)
print(lun)
print(den)
u_in=input("enter your choice:").lower().strip()
if u_in=="1" or u_in=="morning tiffen menu":

    tiffen_menus=["1.idly","2.pongal","3.porri","4.dhosa","5.methu vadai"]
    for i in tiffen_menus:
        print(i)
    idly_amount=7
    pongal_amount=15
    porri_amount=30
    dhosa_amount=15
    methu_vadai_amount=7
    masal_vadai_amount=7
    tiffen_menus.append("masal vadai")
    
    user_input=input("what food you want:").lower().strip()
    if user_input in tiffen_menus:
        print(f"yes your {user_input} is avalable")

        how_many=int(input(f"how many {user_input} you want:"))

    if user_input=="1" or user_input=="idly":
        how_many=int(input(f"how many {user_input} you want:"))
        total=idly_amount *how_many
        print(f"your total bill is Rs.{total}")

    elif user_input=="2"or user_input=="pongal":
        how_many=int(input(f"how many {user_input} you want:"))
        total=pongal_amount*how_many
        print(f"total bill is RS.{total}")

    elif user_input=="3"or user_input=="porri":
        how_many=int(input(f"how many {user_input} you want:"))
        total=porri_amount*how_many
        print(f"your total bill is RS.{total}")

    elif user_input=="4" or user_input=="dhosa":
        how_many=int(input(f"how many {user_input} you want:"))
        total=dhosa_amount*how_many
        print(f"your total bill is RS.{total}")
    
    elif user_input=="5" or user_input=="methu vadai":
        how_many=int(input(f"how many{user_input}you want:"))   
        total=masal_vadai_amount*how_many
        print(f"your total bill is RS.{total}") 
    else:
        print("your oder is  not avalable (or) in correct splling")        

elif  u_in=="2"or u_in=="lunch menu":

    print("aftroon lunches")
    lunch_menus=["1.biriyani","2.full meals","3.chicken rice","4.chile chcken","5.noodles","6.mutton biriyani"]
    for i in lunch_menus:
        print(i)
    
    biriyani=120
    full_meals=100
    chicken_rice=100
    chilly_chicken=90
    noodles=120
    mutton_biriyani=150

    input_lunch=(input("what lunch you want:")).lower().strip()

    if input_lunch in lunch_menus:
        print(f"your order{input_lunch}is avalable")
        
        how_many_lunch=(input(f"how many {input_lunch}you want:"))
        
        
    if input_lunch=="1" or input_lunch=="biriyani":
        how_many_lunch=int(input(f"how many {input_lunch} you want"))
        
        total=how_many_lunch*biriyani
        print(f"yor total bill is RS.{total}")

    elif input_lunch=="2" or input_lunch=="full meals":
        how_many_lunch=int(input(f"how many {input_lunch} you want:"))
        total=how_many_lunch*full_meals
        print(f"your total bill is RS.{total}")
       
    elif input_lunch=="3"or input_lunch=="chicken rice":
        how_many_lunch=(input(f"how many {input_lunch} you want:"))
        total=how_many_lunch*chicken_rice
        print(f"your total bill is RS.{total}")  
       
    elif input_lunch=="4" or input_lunch=="chilly_chiken":
        how_many_lunch=(input(f"how many {input_lunch} you want:"))
        total=input_lunch*chilly_chicken
        print(f"your total bill is RS.{total}")
       
    elif input_lunch=="noodles":             
        how_many_lunch=(input(f"how many {input_lunch} you want:"))
        total=how_many_lunch*noodles
        print(f"your total bill is RS.{total}")
       
    elif input_lunch=="5" or input_lunch=="mutton biriyani":  
        how_many_lunch=(input(f"how many {input_lunch} you want:"))
        total=input_lunch*input_lunch
        print(f"your total bill is Rs.{total}") 
    else:
      print("your is not avalable (or) incorrect spelling")
elif u_in=="3" or u_in=="dinner menu":

    dinner_menus=["1.dhosa","2.chiken rice ","3.chilly chiken","4.grill full","5.half grill",]
    for i in dinner_menus:
        print(i)
    dhosa_amount=15    
    chicken_rice=100
    chilly_chiken=90
    full_grill=350
    dhosa_amount=15
    half_grill=170
    porrato_set=30    
    mutton_chuka=80
    
    user_input=input("what food you want:").lower().strip()
    if user_input in dinner_menus:
        print(f"yes your{user_input}is avalable")

        how_many=int(input(f"how many {user_input} you want:"))
    if user_input=="1" or user_input=="dhosa":
        how_many_lunch=(input(f"{user_input}you want:"))
        total=how_many_lunch*dhosa_amount
        print(f"your total bill is Rs.{total}")

    elif user_input=="2" or user_input=="chicken rice":
        how_many_lunch=int(input(f"how many {user_input} you want:"))
        total=how_many_lunch*chicken_rice
        print(f"total bill is RS.{total}")
    
    elif user_input=="3" or user_input=="chily chiken":
        how_many_lunch=int(input(f"how many {user_input} you want:"))
        total=how_many_lunch*chilly_chiken
        print(f"yoyr total bill is RS.{total}")

    elif user_input=="4" or user_input=="full grill":
        
        how_many_lunch=(input(f"how many {user_input} you want:"))
        total=full_grill*how_many_lunch
        print(f"your total bill is RS.{total}")
    
    elif user_input=="5" or user_input=="half grill":
        how_many_lunch=(input(f"how many {user_input} you want:"))
        total=how_many_lunch*half_grill
        print(f"your total bill is RS.{total}")



else:
     print("your oder is  not avalable (or) in correct splling")       
     
     
     
     
     
