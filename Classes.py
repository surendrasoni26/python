class restaurant:
    def __init__(self, name, cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print('name of the restaurant is ' + self.name)
        print('cuisine_type offered by restaurant is ' + self.cuisine_type)

    def open_restaurant(self):
        print(self.name + ' is open now')


Restaurant=restaurant('Jaika', 'Indian')
Restaurant.describe_restaurant()
Restaurant.open_restaurant()
