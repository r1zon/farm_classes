class Animals:
    satiety = 'no'
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def feed(self):
        self.satiety = 'yes'
    def __gt__(self, other):
        return self.weight > other.weight


class MilkingAnimals(Animals):
    milk = 'full'
    def milking(self):
        self.milk = 'empty'

class EggsAnimals(Animals):
    eggs = 'full'
    def pick_eggs(self):
        self.eggs = 0

class CutAnimals(Animals):
    wool = 'overgrow'
    def cut(self):
        self.wool = 'bald'

class Goose(EggsAnimals):
    voice = 'Honk!'
    def makevoice(self):
        print(self.name + ' говорит : ' + self.voice)

class Cow(MilkingAnimals):
    voice = 'Moo!'
    def makevoice(self):
        print(self.name + ' говорит : ' + self.voice)

class Sheep(CutAnimals):
    voice = 'Baa!'
    def makevoice(self):
        print(self.name + ' говорит : ' + self.voice)

class Chicken(EggsAnimals):
    voice = 'Cluck!'
    def makevoice(self):
        print(self.name + ' говорит : ' + self.voice)

class Goat(MilkingAnimals):
    voice = 'Baa!'
    def makevoice(self):
        print(self.name + ' говорит : ' + self.voice)

class Duck(EggsAnimals):
    voice = 'Quack!'
    def makevoice(self):
        print(self.name + ' говорит : ' + self.voice)

pet1 = Goose('Серый', 2.5)
pet2 = Goose('Белый', 3.0)
pet3 = Cow('Манька', 400.0)
pet4 = Sheep('Барашек', 100.0)
pet5 = Sheep('Кудрявый', 120.0)
pet6 = Chicken('Ко-Ко', 3.0)
pet7 = Chicken('Кукареку', 2.8)
pet8 = Goat('Рога', 60.0)
pet9 = Goat('Копыта', 80.0)
pet10 = Duck('Кряква', 1.0)

animals = [pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9, pet10]
egg_animals = [pet1, pet2, pet6, pet7, pet10]
cut_animals = [pet4, pet5]
milk_animals = [pet3, pet8, pet9]

def main():
    print('Приветствуем на ферме Дядюшки Джо! Ферма богата разными животными: это гуси "Серый" и "Белый", корова "Манька", овцы "Барашек" и "Кудрявый", куры "Ко-Ко" и "Кукареку", '
    'козы "Рога" и "Копыта" и утка "Кряква". \nТолько сегодня вы можете стать настоящим фермером и поухаживать за животными.')
    while True:
        to_do = input('Вам доступны несколько функций:\n'
                      'f - покормить животных\n'
                      'm - подоить корову и коз\n'
                      'c - постричь овец\n'
                      'e - собрать яйца у кур, уток и гусей\n'
                      'v - послушать как разговаривают животные на ферме\n'
                      'w - измерить вес всех животных и найти самое тяжело животное\n' 
                      'q - выйти из программы\n')
        if to_do == 'f':
            feeding()
        elif to_do == 'm':
            milking()
        elif to_do == 'c':
            cutting()
        elif to_do == 'e':
            egg_putting()
        elif to_do == 'v':
            voices()
        elif to_do == 'w':
            weights()
        elif to_do == 'q':
            break

def feeding():
    for pet in animals:
        pet.feed()
        print(f'{pet.name} накормлен? {pet.satiety}')
        print(f'{pet.name} покормлен!\n')

def milking():
    for pet in milk_animals:
        pet.milking()
        print(f'Запас молока у {pet.name} - {pet.milk}')
        print(f'{pet.name} подоена!\n')

def cutting():
    for pet in cut_animals:
        pet.cut()
        print(f'Какая стрижка у {pet.name}? {pet.wool}')
        print(f'{pet.name} подстрижен!\n')

def egg_putting():
    for pet in egg_animals:
        pet.pick_eggs()
        print(f'Сколько яиц осталось у {pet.name}? {pet.eggs}')
        print(f'Яйца у {pet.name} собраны!')

def voices():
    for pet in animals:
        pet.makevoice()
    print()

def weights():
    yes_no = input(f'Хотите оставить вес животных по умолчанию или хотите внести корректировки? если да - введите yes, если нет - no: ')
    if yes_no == 'yes':
        for pet in animals:
            pet.weight = float(input(f'Введите вес {pet.name} в кг: '))
    all_weight = 0
    for pet in animals:
        all_weight += pet.weight
    print(f'Общий вес всех животных -  {all_weight} кг.')
    print(f'Наибольший вес у {max(animals).name} - {max(animals).weight} кг.\n')

main()

