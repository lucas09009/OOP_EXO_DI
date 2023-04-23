class Cat():
    def __init__(self, name, cat_age):
        self.name = name
        self.age = cat_age
        
        

chat1 = Cat("puppy", 2)
chat2 = Cat("Rio", 3)
chat3 = Cat("Jamy", 4)


liste = [chat1, chat2, chat3]

def chat_plus_vieux():
    max = 0
    for item in liste:
        if max < item.age:
            max = item.age
    return item
cat = chat_plus_vieux()
print(cat.name,"est le chat le plus âgé, son âge est:",cat.age,"ans")




class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    
    def bark(self):
        print("{} goes woof!".format(self.name))
        
        
    def jump(self,x):
        print(self.name,"jumps",x,"cm de hauteur,",x,"est la hauteur")
        
        
davids_dog = Dog("Rex", 50)
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump(5)  



sarahs_dog = Dog("Teacup", 20)
sarahs_dog.bark()
sarahs_dog.jump(3)


liste = [davids_dog, sarahs_dog]
max = 0
for item in liste:
    if item.height > max:
        max = item.height
print("le chien le plus gros est:",item.name)



class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
        
    def sing_me_a_song(self):
        for item in self.lyrics:
            print("\n",item,"\n")
            
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()



class Zoo():
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        
        
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            
            
    def get_animals(self):
        for item in self.animals:
            print(item)
            
            
    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)
        print(self.animals)
        
        
    def sort_animals(self):
        mon_dictionnaire = {}
        for item in self.animals:
            première_lettre = item[0]
            
            if première_lettre not in mon_dictionnaire:
                mon_dictionnaire[première_lettre] = [item]
            
            else:
                mon_dictionnaire[première_lettre].append(item)
        i = 1
        diction = {}
        for item in mon_dictionnaire.values():
            diction[i] = item
            i += 1
        print(diction)
        return mon_dictionnaire
    
    def  get_groups(self):
        mon_dictionnaire = self.sort_animals
        for item in mon_dictionnaire:
            print(item)
            
    
ramat_gan_safari = Zoo("abalo")
ramat_gan_safari.add_animal('lion')
ramat_gan_safari.add_animal('chimpanze')
ramat_gan_safari.add_animal('leopard')
ramat_gan_safari.add_animal('lièvre')
ramat_gan_safari.add_animal('guepard')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("lion")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()