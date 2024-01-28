class Recipe():
    def __init__(self, dish, item, time) -> None:
        self.dish = dish
        self.item = item
        self.time = time
    def content(self):
        print("The " + self.dish + " has " + self.item +  
               " and takes " + str(self.time) + " minutes" )
        
pizza =  Recipe('pizza', ['cheese', 'bread', 'tomato'], 45)
pasta = Recipe('pasta', ['penne', 'sauce'], 55)

print(pizza.item)
print(pasta.item)

print(pizza.content)