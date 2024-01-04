#slicing the list
car_models = ['audi', 'bmw', 'subaru', 'Tesla', 'Kia', 'Nissan']

friends_favorites = car_models[:-2]
car_models.append('fiat')
friends_favorites.append('toyota')

print(f"My favorite cars are {car_models}")
print(f"My friends favorite cars are {friends_favorites} ")



