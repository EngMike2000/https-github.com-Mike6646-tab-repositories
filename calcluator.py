from colorama import Fore, Style


def generate_feet():
    data_range = {}
    starter = 1
    range_list = []
    feet = 0.25
    
    while starter < 100:
        list_full = False
        while list_full == False:
            range_list.append(starter)
            starter += 1
            
            if len(range_list) == 3:
                list_full = True
                data_range[tuple(range_list)]= feet
                feet += 0.25
                range_list = []
                
    return data_range

data_range = generate_feet()
MEASUREMENT_LIST = []


# #get input of measurement and return value of price
# #i want to get the cost of a glass if it is one of the list
def get_squareFeet(measurement1, measurement2):
 
    measurement1 = int(input('Enter height:  '))
    measurement2 = int(input('Enter width:  '))
    MEASUREMENT_LIST.append((measurement1, measurement2))
    sizes=[measurement1, measurement2]
    price1, price2 = 0, 0
    
    for size in sizes:
        for data in data_range:
            if size in data:
                if size == measurement1:
                    # print('found price 1' + )
                    price1 = data_range[data]
                elif size == measurement2:
                    price2 = data_range[data]
            
    totalFeet = price1*price2
    print(f'{price1} * {price2} = {totalFeet}') 

    return totalFeet



# get_squarefeet(14, 10)

# store the cost of each glass and get the total cost
def prices():
    prices = {
        '3mm': 70,
        '4mm': 90,
        '1 Way Blue': 110,
        'Mirror 3mm': 120,
        'Mirror 4mm': 180 
    }

    return prices

# get the price and squarefeet and multiply --- squarefeet * 
def total_price(prices_, total_squareFeet):
    
    print('\n')
    number = 1
    for item in prices():
        print(f'{number}: {item}') 
        number += 1
    
    
    choice = 0
    
    try:
        choice = input('please select an option: ')
    except IndexError as e:
        choice = input('please an available option: ')
        
    choice = int(choice) - 1
    # number chosen * total feet
    # change type of prices to list for indexing(-1)
    glass_list = list(prices_)
    

    price_key = glass_list[choice]
    glass_price = prices_[price_key]
    print(f'\n{price_key} is {glass_price} per square foot')
    
    
    pieces = input('How many Pieces?:  ')
    total_price = (total_squareFeet * glass_price) * int(pieces)
    print(f'Total price for {price_key} {total_squareFeet}is ~ {total_price}')
    
    return total_price, pieces




# The `total_price(price, feet)` function is calculating the total cost of glass based on the selected
# type of glass and the total square feet obtained from the `get_squareFeet` function.


total = 0
while True:
    feet = get_squareFeet(11, 13)
    price = prices()
    total += total_price(price, feet)[0]
    
    print(total)


