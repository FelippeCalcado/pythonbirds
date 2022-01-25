class Pessoa:
    species = 'Human'
    age = None

    def __init__(self, name, sex):
        self.sex = sex
        self.name = name

    def p_data(self):
        print(
            f'''
{self.name}
{self.age}
{self.species}
{self.sex}''')


class Elder(Pessoa):
    age = '>60'


class Adult(Pessoa):
    age = '18 to 59'


class Teenager(Pessoa):
    age = '13 to 17'


class Child(Pessoa):
    age = '0 to 12'



tilburi = Adult('Tilburi', 'Male')
chuck = Teenager('Chuck', 'Female')
gabo = Child('Gabo', 'Male')

tilburi.p_data()
chuck.p_data()
gabo.p_data()
