#Exception handling function to get  valid name as input
def username():
    while True:
        try:
            user=str(input("Please enter your name:"))
            if user.isalpha() == True:
                break
            else:
                print('Enter a valid name')
        except ValueError:
            print('Enter a valid name')
    return user

#Exception handling function to get a valid input for quantity
def quantity():
    while True:
        try:
            quant=int(input("Quantity: "))
            if quant >= 0:
                break
            else:
                print('Invalid. Enter a valid input')
        except ValueError:
            print('Invalid. Enter a valid input')
    return quant

#Exception handling function to get a valid available item name
def iteminput():
    while True:
        try:
            item=str(input("Add item from the items available to the basket: ")).lower()
            if item.lower() in ['apples','milk','bread','soup']:
                break
            else:
                print('Enter a valid available item name')
        except ValueError:
            print('Enter a valid available item name')
    return item

#Exception handling function to get only y/n
def yesorno():
    while True:
        try:
            choice=str(input("Please choose Y/N: "))
            if choice.lower() in ['y','n']:
                break
            else:
                print('Invalid input. Please choose Y/N')
        except ValueError:
            print('Invalid input. Please choose Y/N')
    return choice

#Welcome message
user_name=username()
welcome_display = f"Welcome to the store. Have a great shopping {user_name}"
display_length = len(welcome_display)
print("#"*display_length)
print(welcome_display)
print("#"*display_length)

#initializing required dictionaries for the program
item_dict = {}
shopping_dict = {}

#Reading data from the input file and storing as a list
file = open("items_available.txt")
first_line=file.readline() #To move the cursor to the end of the header
available_items = file.readlines()
file.close()

#Taking values form the list and storing it in a dictionary
print("\nList of items available in the store today along with their unit price\n")

for item in available_items:
    item_groceryname = item.split()[0]
    item_unitprice = item.split()[1]
    item_units = item.split()[2]
    print(f"{item_groceryname} - £{item_unitprice} {item_units}")
    item_dict.update({item_groceryname:float(item_unitprice)})
    
print("\n"+"#"*5+" Special offers as follows "+"#"*5+"\n")
print("Apples have a 10% discount off their normal price this week")
print("Buy 2 tins of soup and get a loaf of bread for half price\n")
print("#"*37)

print("\nDo you wish to continue? ")
continue_shopping = yesorno()
#continue_shopping=yesorno(proceed_shop)

while continue_shopping.lower() == 'y':
    add_item = iteminput()
    if add_item.title() in item_dict:
        
        if add_item.lower() in shopping_dict:
            qty=quantity()      
            qty=shopping_dict[add_item.lower()]['quantity']+qty
        else:
            qty=quantity()
        
        if add_item.lower() == 'soup' and qty >=2:
            shopping_dict.update({add_item:{"quantity":qty,"subtotal":item_dict[add_item.title()]*qty}})
            print(f"You are eligible to get {qty//2} loaf of bread at half price.")
            global bread
            print("Do you wish to add it to the cart? (Y/N)")
            bread=yesorno()
            if bread.lower() == 'y':
                add_item='bread'
                qty=qty//2
                shopping_dict.update({add_item:{"quantity":qty,"subtotal":item_dict[add_item.title()]*qty}})
            else:
                shopping_dict
        else:
            shopping_dict.update({add_item:{"quantity":qty,"subtotal":item_dict[add_item.title()]*qty}})
    else:
        print("Unable to add an unavailable item")
    print("Do you wish to add more items to the cart? ")
    continue_shopping=yesorno()
else:
    print("\n")
    print("\n"+"#"*5+" Invoice "+"#"*5+"\n")
    print("\n")
    print("Item                 Quantity         SubTotal")
    sub_total=0
    total=0
    offers=0
    for key in shopping_dict:
        if key.lower() == 'apples':
            print(f"{key} (offer)                 {shopping_dict[key]['quantity']}              £{(format(shopping_dict[key]['subtotal'],'.2f'))}")
            sub_total=(shopping_dict[key]['subtotal'])+sub_total
            offers = (shopping_dict[key]['quantity']*1.00)-(shopping_dict[key]['quantity']*.90)+offers

        elif key.lower() == 'bread' and shopping_dict['soup']['quantity'] >= 2:
            print(f"{key}  (offer)                {shopping_dict[key]['quantity']}              £{(format(shopping_dict[key]['subtotal'],'.2f'))}")
            sub_total=(shopping_dict[key]['subtotal'])+sub_total
            offers = ((shopping_dict['soup']['quantity']//2)*.40)+offers

        else:
            print(f"{key}                         {shopping_dict[key]['quantity']}             £{(format(shopping_dict[key]['subtotal'],'.2f'))}")
            sub_total=shopping_dict[key]['subtotal']+sub_total
            total = sub_total-offers
    
    print("\n")
    print("\n")
    print(f"Sub Total: £{(format(sub_total,'.2f'))}")
    print(f"Offers   : £{(format(offers,'.2f'))}")
    print(f"Total    : £{(format(sub_total-offers,'.2f'))}")
    print("\n")
    print("\n"+"#"*5+" Thank you "+"#"*5+"\n")
    print("\n")
    print(f"Hope to see you back soon {user_name}!")
    