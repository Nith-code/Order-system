list_of_drink = {1 :'Ice latte',2 :'Green tea',3 :'Black coffee',4 : 'Cappucino', 5 : 'American', 6 : 'Thai tea'}
for i in list_of_drink:
    print(list_of_drink[i])
order = input('What do you want to order? ')
if order == list_of_drink[i]:
    print('your order is', order)