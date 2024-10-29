#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.set_brand(brand)
        self.set_size(size)

    def get_brand(self):
        return self._brand    
        
    def set_brand(self,brand):
        self._brand=brand

    def get_size(self):
        return self._size 

    def set_size(self,size):
        if isinstance(size,int):
            self._size=size
        else:
            print("size must be an integer")  

    def cobble(self,):
        self.condition="New"
        print("Your shoe is as good as new!")
        return "The shoe has been repaired."
           
        

    brand=property(get_brand,set_brand)
    size=property(get_size,set_size)    

adida=Shoe("adida",45)  
    
  