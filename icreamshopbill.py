def Bill(price,quantity):
    total = (item_nu*quantity)
    print("Your bill = ",total," Rs")


print(" Welcome to icey-Hub ")
print(" MENU : \n 1. Chocolate  70 Rs \n 2. Butter Scotoch  50 Rs \n 3. Vanila  50 Rs \n 4. Stawberry  60 Rs \n 5. Pista  70 Rs \n 6. Manogo Price  50 Rs \n 7. Rajwada  70 Rs \n 8. Cheese  60 Rs \n 9. Tuti Frutti  70 Rs \n 10. Pineapple 50 Rs \n 11. Blackcurrant  60 Rs \n 12. Apple  50 Rs \n 13. Almond Joy  50 Rs \n 14. Cookies and Cream  60 Rs \n 15. Faluda  80 Rs")

state= "start"

if state == "start":
    print("Started")
    userinput = input("Start the Billing? y/n")
    if userinput == "y":
        state = "item"
    else:
        state = "start"
while(state=="item"):
    if state == "item":
        item_nu=int( input(print("Select item from thier number  =  ")))
        state="qty"
    if state == "qty":
        quantity = int(input(print(" Enter the Quantity  = ")))
        state="more"
    if state == "more":
        extra = input(print("Do you want to do another item? y/n"))
        if extra == "y":
            state = "item"
        if extra == "n":
            state = "bill" 
if state == "bill":
    if item_nu == 1:
        Bill(70,quantity)
    if item_nu == 2 :
        Bill(50,quantity)
    if item_nu ==3 :
        Bill(50,quantity)
    if item_nu == 4 :
       Bill(60,quantity)
    if item_nu ==5 :
       Bill(70,quantity)
    if item_nu ==6 :
       Bill(50,quantity)
    if item_nu == 7:
       Bill(70,quantity)
    if item_nu ==8 :
       Bill(60,quantity)    
    if item_nu == 9:
       Bill(70,quantity)
    if item_nu == 10: 
       Bill(50,quantity)
    if item_nu == 11:
        Bill(60,quantity)
    if item_nu ==12 :
         Bill(50,quantity)
    if item_nu ==13 :
        Bill(50,quantity)
    if item_nu ==14 :
        Bill(60,quantity)
    if item_nu == 15:
        Bill(80,quantity)    



     

