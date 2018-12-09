class Human:
    def __init__(self, new_name):
        self._name = new_name
        print(f'Родился человек с именем {self._name}')
    def growing(self, years):
        print(f' {self._name} отмечает день рождения! Ему {years}! ')
    def eating(self):
        print(f' {self._name} ест')
    def sleeping(self):
        print(f' {self._name} спит')
    def working(self, years):
        if years > 18:
            print(f' {self._name} работает')
    def voting(self, years):
        if years >= 18 and years % 4 == 0:
            print(f'{self._name}, голосует за Президента')
    def relaxing(self):
        print(f'{self._name}, отдыхает')
    def diyng(self, n):
            print(f'{self._name}, откинулся, ему было {n}')
n = int(input('Введите возраст: '))
class Life:
    def life(self, human, years=0):
        while years != n:            
            human.growing(years)
            human.eating()
            human.sleeping()
            human.working(years)
            human.voting(years)
            human.relaxing()
            human.diyng(years)
            years += 1
petr = Human('Петр')
life_petr = Life()
life_petr.life(petr)

