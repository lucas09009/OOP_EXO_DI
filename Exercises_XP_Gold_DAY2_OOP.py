from math import * 
class Circle():
    def __init__(self, rayon=1.0):
        self.rayon = rayon
    
    
    def Périmètre(self):
        print("Le périmètre est:", 2*self.rayon*pi)
        
        
    def Aire(self):
        print("L'aire du cercle est:",self.rayon**2*pi)
        
        
    def Définition_Géométrique(self):
        print("Un cercle est l'ensemble de tous les points équidistants d'un point fixe O.")
        
        
cercle = Circle(2)
cercle.Périmètre()
cercle.Aire()
cercle.Définition_Géométrique()

import random
class  MyList():
    def __init__(self, liste_de_lettres):
        self.liste_de_lettres = liste_de_lettres
        
        
    def Inversion_de_listes(self):
        return list(reversed(self.liste_de_lettres))
    
    
    def Liste_triée(self):
        return sorted(self.liste_de_lettres)

    
    def Générer_deuxième_liste(self):
        i = 0
        list2 = []
        while len(list2)<=8:
            nombre = random.randint(0, 100)
            list2.append(nombre)

        return list2
      
    
    
liste = MyList(["a", "c", "b", "d", "e", "f", "g", "h", "i"])
print(liste.Inversion_de_listes())
print(liste.Liste_triée())
print(liste.Générer_deuxième_liste())



class MenuManager():
    def __init__(self):
        self.menu = [
                    {"Nom":"Soup",
                      "Prix": 10,
                      "Niveau d'épices":"B",
                      "Indice de Gluten":False
                    },
                     
                    {
                      "Nom": "Hamburger",
                      "Prix": 15,
                      "Niveau d'épices": "A",
                      "Indice de Gluten": True   
                    },
                     
                    {
                      "Nom":  "Salad",
                      "Prix": 18,
                      "Niveau d'épices": "A",
                      "Indice de Gluten": False
                    },
                    
                    {
                      "Nom":  "French Fries",
                      "Prix": 5,
                      "Niveau d'épices": "C",
                      "Indice de Gluten": False
                    },
                    
                    {
                      "Nom":  "Beef bourguignon",
                      "Prix": 25,
                      "Niveau d'épices": "B",
                      "Indice de Gluten": True
                    }]
   

    def add_item(self, name, price, spice, gluten):
        mon_dict = {}
        mon_dict["Nom"] = name
        mon_dict["Prix"] = price
        mon_dict["Niveau d'épices"] = spice
        mon_dict["Indice de Gluten"] = gluten
        self.menu.append(mon_dict)
        return self.menu
    
    
    def update_item(self, name, price, spice, gluten):
        liste_des_noms = []
        for item in self.menu:
            liste_des_noms.append(item["Nom"])
            
        if name not in liste_des_noms:
            print("\U0001F62D Le plat <<{}>> n'a pas été trouvée".format(name))
        
        else:
            item["Nom"] == name
            item["Prix"] = price
            item["Niveau d'épices"] = spice
            item["Indice de Gluten"] = gluten
            print("\U0001F600 Le plat <<{}>> a été mise à jour".format(name))
         
            
              

    def remove_item(self, name):
        liste_des_noms = []
        for item in self.menu:
            liste_des_noms.append(item["Nom"])
        if name not in liste_des_noms:
            print("\U0001F62D Le plat <<{}>> n'est pas sur le menu".format(name))  
        else:
            self.menu.remove(item)
            print("\U0001F600 Le plat <<{}>> à bien été supprimer".format(name))
           
a = MenuManager()
a.add_item("Banane_Plantin",12,"B",False)
a.update_item("Banane_Plantin",15,"A",True)     
a.remove_item("Banane_Plantin")
print(a.menu)