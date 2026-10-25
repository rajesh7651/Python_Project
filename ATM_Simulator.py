balance=10000
correct_pin=1234
attempts=0
deposit=0
withdraw=0


while attempts<3:
    user_pin=int(input("Enter the pin:"))
    if user_pin==correct_pin:
        print("Login Successful")

        print("=====ATM Menu=====\n"
              "1. For Balance\n"
               "2. For Deposit\n"
               "3. For Withdraw\n"
               "4. For Exit")
        while True:
            user=int(input("Select the option that you want: "))
      
            if user==1:
                print(" Current Balance:",balance)
            elif user==2:
                deposit=int(input("Enter the deposit amount:"))
                if deposit>0:
                 balance+=deposit
                 print("New Balance:",balance)
                else:
                   print("Invalid deposit amount")
            elif user==3:
                withdraw=int(input("Enter the withdraw amount:"))
                if 0<withdraw<=balance:
                 balance-=withdraw
                 print("Available Balance:",balance)
                else:
                     print("Insufficient Balance or Invalid amount")
            elif user==4:
               print("======Receipt======\n"
                     f"Deposit Amount: {deposit}\n"
                     f"Withdraw Amount: {withdraw}\n"
                     f"Available Balance: {balance}\n"
                     "Thank You")
               break
            else:
               print("Invalid input")
               
        break  
       
    else:
       attempts+=1
       print("Invalid Pin")
       print(f"You have {3-attempts} attempts left.")
       if attempts==3:
         print("Your card is blocked.")
               
               
               
            
