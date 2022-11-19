import random
import time

class bot:
    Names = ['Mabel','Mackenzie','Mia','Jaden','Jeffery','Jesus','Joseph Jostar','Juan','Horace','Hunter','George','Gordon','Carlos','Connor','Cody','clown Joker','rap rocker','Rayan Gosling']
    def __init__(self,name=Names[random.randint(0,19)],creampie=random.randint(0,20000),points=random.randint(4,30)):
        self.name = name
        self.creampie = creampie
        self.points = points
    def show(self):
        print('Name: ',self.name,'\n' 'Money: ',self.creampie, '\n' 'Points: ',self.points)


class user:
    def __init__(self, creampie=random.randint(-1000,1000), name='Unknow', gender='Unknow',points=0):
        self.creampie = creampie
        self.name = name
        self.gender = gender
        self.points = points
    def show(self):
        print('Name:',self.name, '\n' 'Gender:',self.gender, '\n''Creampie count:',self.creampie)

def download(n):
    for i in range(101):
        dw = str(i)+ '%'
        print(dw, end='')
        print('\r', end='')
        k = random.uniform(0.02,0.3)//n
        time.sleep(k)
    



count = int(input("введите количество игроков: "))
bots = []
for i in range(count):
    bots.append(bot())


my_name = str(input('Введите ваше имя: '))
my_creampie = int(input('Введите вашу денежку: '))
my_gender = str(input('Введите ваш пол (гендер): '))
me = user(my_creampie, my_name, my_gender)
me.show()

print('\n','Да начнется игра, и пусть удача всегда будет с вами')
time.sleep(2)



#Раздача
print('\n','Происходит раздача карт','\n')
download(1)



#Начало игры
print("Ваш статус","\n")
me.show()
download(4)




