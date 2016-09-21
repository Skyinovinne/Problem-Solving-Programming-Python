##PROBLEM: Mark is stuck on Mars and needs to figure out how long he can
##         survive eating rations and potatoes.
##
##ALGORITHM:
##    1. Ask user about survival supplies
##    2. Calculate ration survival data
##    3. Find survival data on potatoes
##    4. Display survival data summary

print('The Martian Survival\n')

ration = float(input('How many meal packs do you have? '))
consumption = float(input('How many calories per day will you consume? '))
farmland = float(input('How many square meters of soil will you plant? '))

print('\nCalculating Survival\n')

rationDays = ration * 2000 / consumption
print('You will survive', rationDays, 'days on NASA ration packs.\n')

soil = farmland / 10
print('You will need', soil, 'cubic meters of soil')

water = soil * 40
print('The soil needs', water, 'liters of water')

potatoKg = 0.006 * rationDays * farmland
print('You can grow', potatoKg, 'kg of potatoes before rations run out')

potatoDays = 700 * potatoKg / consumption
print('Crops will extend your life by', potatoDays, 'days')

totalDays = rationDays + potatoDays
print('This plan gives you a total of', totalDays, 'days of food\n')

print('Good luck Mark')

