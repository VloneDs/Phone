class phone:

    def __init__(self, number, model = 'неизвестен', weight = 'неизвестно') -> None: #получаем значения, если его нету, то есть значение  по умолчанию
        self.number = number
        self.model = model 
        self.weight = weight
    
    def print_data(self) -> str: # выводит информацию
        return f'Телефон {self.model}, номер {self.number}, вес {self.weight} ' # Вес чего? Бананов??
    
    def recive_call(self, name): # выводит информацию 
        self.name = name
        print(f'Звонит {self.name} на {self.number}')

    def get_number(self): #возвращает номер телефона
        return self.number
    
a = phone('+79157776989', 'Xiaomi redmi pro', '170')
a.recive_call('Vlone') 
print(a.print_data())
print(a.get_number())
print(' ')

b = phone('+99106669889','Iphone X')
b.recive_call('Sayori') 
print(b.print_data())
print(b.get_number())
print(' ')

c = phone('+79109992233')
c.recive_call('Qwerez')
print(c.print_data())
print(c.get_number())