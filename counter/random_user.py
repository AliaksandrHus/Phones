import random


def get_random():

    name = random.choice(['Петя', 'Вася', 'Даша', 'Саня', 'Катя', 'Таня']) \
           + ' ' + random.choice(['Шмыг', 'Клык', 'Март', 'Крот', 'Смог', 'Корд'])

    phone = '+37529' + str(random.randint(0, 9999999))

    return [name, phone]

