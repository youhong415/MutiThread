# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:30:52 2020

@author: bbjac
"""

from threading import Thread
import time


class Dog():
    def __init__(self,Name):
        self.Name = Name
        self.Height = 60
        self.Weight = 20
    
    def Bark(self):print("bark!bark!bark!")
    def Set_Name(self,Name):self.Name = Name
    def Print_Name(self):print(self.Name)
    def Get_Name(self):return self.Name
    def Print_Weight(self):print(self.Name+" Weight:"+str(self.Weight))
    def Get_Weight(self):return self.Weight
    def Print_Height(self):print(self.Name+" Height:"+str(self.Height))
    def Get_Height(self):return self.Height


class HealthCare(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.Dog = []
    
    def Take_Care(self,Dog):
        self.Dog.append(Dog)
    
    def Feed(self,Name):
        for dog in self.Dog:
            if dog.Name==Name : dog.Weight+=1
    
    def Feed(self):
        for dog in self.Dog:
            dog.Weight+=1

    def run(self):
        i=0
        while i<50:
            self.Feed()
            time.sleep(0.5)
            i+=1
        

Dog1 = Dog('來福')
Dog2 = Dog('招財')

HealthCare_ = HealthCare()
HealthCare_.Take_Care(Dog1)
HealthCare_.Take_Care(Dog2)

HealthCare_.start()

i=0
while i<50: 
    Dog1.Print_Weight()
    Dog2.Print_Weight()
    time.sleep(1)
    i+=1
    
HealthCare_.join()

print("Done!")    


