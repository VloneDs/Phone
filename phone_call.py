class phone:

    def __init__(self, number = 'неизвестен', model = 'неизвестен', weight = 'неизвестно') -> None: #получаем значения, если его нету, то есть значение  по умолчанию
        self.number = number
        self.model = model 
        self.weight = weight
    
    def __str__(self) -> str: # выводит информацию
        return f'Телефон {self.model}, номер {self.number}, вес: {self.weight} ' # Вес чего? Бананов??
    
    def recive_call(self, name): # выводит информацию 
        self.name = name
        print(f'Звонит {self.name} на {self.number}')

    def get_number(self): #возвращает номер телефона
        return f'Номер телефона {self.number}'
    
phone1 = phone('+79157776989', 'Xiaomi redmi pro', '170')
phone1.recive_call('Vlone') 
print(phone1)
print(phone1.get_number())
print(' ')

phone2 = phone('+99106669889','Iphone X')
phone2.recive_call('Sayori') 
print(phone2)
print(phone2.get_number())
print(' ')

phone3 = phone('+79109992233')
phone3.recive_call('Qwerez')
print(phone3)
print(phone3.get_number())
print(' ')

phone4 = phone()
phone4.recive_call('Zerta')
print(phone4)
print(phone4.get_number())