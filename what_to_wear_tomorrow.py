print('What is the weather forecast for tomorrow?')
temp=int(input('Temperature: '))
rain=input('Will it rain (yes/no): ')
if temp>20 and rain=='no':
    print('Wear jeans and a T-shirt')
elif temp>20 and rain=='yes':
    print("Wear jeans and a T-shirt\nDon't forget your umbrella!")
elif temp<=20 and temp>10 and rain=='no':
    print('Wear jeans and a T-shirt\nTake a jacket too!')
elif temp<=20 and temp>10 and rain=='yes':
    print("Wear jeans and a T-shirt\nTake a jacket too!\nDon't forget your umbrella!")
elif temp<=10 and temp>5 and rain=='no':
    print('Wear jeans and a T-shirt\nI recommend something warm and a coat')
elif temp<=10 and temp>5 and rain=='yes':
    print("Wear jeans and a T-shirt\nI recommend something warm and a coat\nDon't forget your umbrella!")
elif temp<=5 and rain=='no':
    print('Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually\nI think gloves are in order')
elif temp<=5 and rain=='yes':
    print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually\nI think gloves are in order\nDon't forget your umbrella!")