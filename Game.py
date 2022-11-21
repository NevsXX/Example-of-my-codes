import random
import time
import turtle

#боты
class bot:
    Names = ['Mabel','Mackenzie','Mia','Jaden','Jeffery','Jesus','Joseph Jostar','Juan','Horace','Hunter','George','Gordon','Carlos','Connor','Cody','clown Joker','rap rocker','Rayan Gosling']
    def __init__(self,name=Names[random.randint(0,19)],creampie=random.randint(0,20000),points=random.randint(4,30)):
        self.name = name
        self.creampie = creampie
        self.points = points
    def show(self):
        print('Name:',self.name,'\n' 'Money:',self.creampie, '\n' 'Points:',self.points)

#Главный игрок
class user:
    def __init__(self, creampie=random.randint(-1000,1000), name='Unknow', gender='Unknow',points=0):
        self.creampie = creampie
        self.name = name
        self.gender = gender
        self.points = int(points)
        '''self.points = []'''

    def show(self):
        print('Name:',self.name, '\n' 'Gender:',self.gender, '\n''Creampie count:',self.creampie,'\n''Points:',self.points)

def take_card():
    print("Function Up worlking")
    """#self.points + random.randint(6,12)
     #print('Карта была взята. Проверте свой')
    self.points.append(random.randint(6,12))"""  
    
#Функция изображения загрузки
def download(n):
    for i in range(101):
        dw = str(i)+ '%'
        print(dw, end='')
        print('\r', end='')
        k = random.uniform(0.02,0.3)/n
        time.sleep(k)

'''def take_card():
    user.points()
'''

#Приветствие игры
print('Добро пожаловать в игру 21','\n')
time.sleep(3)

#Заполнение класса пользователя и создание ботов
count = int(input("введите количество игроков: "))
window = turtle.Screen()
bots = []
for i in range(count):
    bots.append(bot())
my_name = str(input('Введите ваше имя: '))
my_creampie = int(input('Введите вашу денежку: '))
my_gender = str(input('Введите ваш пол (гендер): '))
me = user(my_creampie, my_name, my_gender)
me.show()
"""time.sleep(3)"""
print('\n','Сбор данных','\n')
#download(1)


#Начало игры
print("Ваш статус","\n")
me.show()
"""download(4)"""
print('\n','Take the card - press key Up')
window.onkey(take_card,"Up") 