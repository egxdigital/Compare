from pprint import pprint
from faker import Faker
import random

def get_random_command_and_payload():
    fake = Faker()

    basic_command = [
        'prices', 
        '-c', 
            f'name={fake.word()}', 
            f'partA={round(random.uniform(10, 50), 2)}', 
            f'partB={round(random.uniform(10, 50), 2)}',
            f'p={round(random.uniform(100, 150), 2)}',
            f'qt={random.randint(1, 10)}', 
            f'desc={fake.sentence()}',
            f'priority={round(random.uniform(1, 10), 2)}',
        '-c', 
            f'n={fake.word()}',
            f'partA={round(random.uniform(10, 50), 2)}',
            f'partB={round(random.uniform(10, 50), 2)}',
            f'dist={round(random.uniform(10, 50), 2)}',
            f't={round(random.uniform(100, 500), 2)}',
            f'wt={round(random.uniform(100, 500), 2)}',
        '-c', 
            f'name={fake.word()}',
            f'desc={fake.word()}', 
            f'partA={round(random.uniform(10, 50), 2)}',
            f'partB={round(random.uniform(10, 50), 2)}',
            f'sp={round(random.uniform(100, 500), 2)}'
    ]

    basic_payload = [
        {'name': basic_command[2].split('=')[1], 
         'partA': float(basic_command[3].split('=')[1]),
         'partB': float(basic_command[4].split('=')[1]), 
         'price': float(basic_command[5].split('=')[1]),
         'quantity': float(basic_command[6].split('=')[1]), 
         'description': basic_command[7].split('=')[1],
         'priority': float(basic_command[8].split('=')[1])},

        {'name': basic_command[10].split('=')[1], 
         'partA': float(basic_command[11].split('=')[1]),
         'partB': float(basic_command[12].split('=')[1]), 
         'distance': float(basic_command[13].split('=')[1]),
         'time': float(basic_command[14].split('=')[1]), 
         'weight': float(basic_command[15].split('=')[1])},

        {'name': basic_command[17].split('=')[1], 
         'description': basic_command[18].split('=')[1],
         'partA': float(basic_command[19].split('=')[1]), 
         'partB': float(basic_command[20].split('=')[1]),
         'speed': float(basic_command[21].split('=')[1])},
    ]

    return basic_command, basic_payload

if __name__ == '__main__':
    # Example usage:
    basic_command, basic_payload = get_random_command_and_payload()
    pprint(basic_command)
    pprint(basic_payload)