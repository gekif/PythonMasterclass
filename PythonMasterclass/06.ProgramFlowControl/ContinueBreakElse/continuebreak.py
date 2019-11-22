shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

# for item in shopping_list:
#     if item == 'spam':
#         print('I am ignoring ' + item)
#         continue
#
#     print("Buy " + item)


meal = ['item', 'bacon', 'beans', 'sausages']

nastyFoodItem = ''

for item in meal:
    if item == 'spam':
        nastyFoodItem = item
        break

if nastyFoodItem == 'spam':
    print('Can\'t i have anything without spam in it')
else:
    print("I'll have a plate of that, then, please")