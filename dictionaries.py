my_set = {1, 3, 5}

my_dict = {'name': 'Jose', 'age': 90, 'Grades': [13, 45, 66, 90]}

another_dict  = {1: 15, 2: 75, 3: 150}

lottery_player= {
    'name': 'Rolf',
    'numbers': (13, 45, 66, 23, 22)
}

universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]

sum(lottery_player['numbers'])

lottery_player['name'] = 'John'

#  this we can't do cause lottery_player 'numbers' : {()} is a tuple which are immutable
lottery_player['numbers'][0] = 50


student = {'name': 'Jose', 'school': 'computing', 'grade': [66, 77, 88]}
