
cars = ['bmw','audi','toyota']
for car in cars:
    if (car == 'bmw'):
        print(car.upper())
    else:
        print(car.title()+","+car.lower())
    print(car.lower() == 'audi')
