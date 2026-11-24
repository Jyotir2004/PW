class Bankaccount:
      def __init__(self):
         self.pin=" "
         self.balance=" "
         self.menu()

      def menu(self):
            while True:
                  user_input=input("1.press 1 for entering the pin\n"
                                    "2.press 2 for deposit\n"
                                    "3.press 3 for withdraw\n"
                                    "4.press 4 for check balance \n"
                                    "5.press 5 for exit\n"
                                    "entering your choice"
                                    )

                  if user_input=="1":
                        print("enter the pin")
                        self.create_pin()

                  elif user_input=="2":
                        print("deposit")
                        self.deposit()

                  elif user_input=="3":
                        print("withdraw")
                        self.withdraw()

                  elif user_input=="4":
                        print("check balance")
                        self.balance()

                  elif user_input=="5":
                        print("exit")
                        break

                  else:
                        print("invalid input")



      def create_pin(self):
            self.pin=int(input("enter the pin"))
            print("pin created")
                  
      def deposit(self):
            temp=int(input("enter the pin:"))
            if temp==self.pin:
                  amount=int(int(input("enter the amount:")))
                  self.balance+=amount
                  print("amount deposited")
      

      def withdraw(self):
            temp=int(input("enter the pin:"))
            if temp==self.pin:
                  amount=int(input("enter the amount:"))
                  if amount<self.balance:
                        self.balance-=amount
                        print("withdrawing balance")


      def balance(self):
            temp=int(input("enter the pin:"))
            if temp==self.pin:
                  print("balance:",self.balance)


      

                  


                  

