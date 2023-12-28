from pprint import pprint
from faker import Faker
import random

def get_basic_command():
    fake = Faker()

    return [
        'price',
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

def get_typical_command_and_price_comparison_result():
    command = get_basic_command()
    result = [
        {
            'name': command[2].split('=')[1],
            'total_price': sum([
                float(command[3].split('=')[1]),
                float(command[4].split('=')[1]),
            ]),            
            'description': command[7].split('=')[1],
        },
        {
            'name': command[10].split('=')[1],
            'total_price': sum([
                float(command[11].split('=')[1]),
                float(command[12].split('=')[1]),
            ]),            
            'description': 'N/A',
        },
        {
            'name': command[17].split('=')[1],
            'total_price': sum([
                float(command[19].split('=')[1]),
                float(command[20].split('=')[1]),
            ]),
            'description': command[18].split('=')[1],
        }
    ]
    return command, sorted(result, key=lambda x: x['total_price'])
    
def get_typical_payload_and_price_comparison_result():
    fake = Faker()

    payload = [
        {
            'name': 'Server Workstation #1',
            'description': "High performance workstation for running VM's",
            'motherboard': 340.99,
            'memory': 149.99,
            'cpu': 120.42,
            'gpu': 299.99,
            'priority': 0.5,
            'weight': 5.0
        },
        {
            'name': 'Server Workstation #2',
            'description': "High performance workstation for running VM's",
            'motherboard': 299.99,
            'memory': 149.99,
            'cpu': 120.42,
            'gpu': 312.99,
            'priority': 0.5,
            'weight': 7.0
        },
        {
            'name': 'Raid Setup',
            'description': "Extend existing computer's space and upgrade other parts",
            'memory': 100.24,
            'ssd1': 49.99,
            'ssd2': 49.99,
            'ssd3': 49.99,
            'priority': 1,
            'weight': 4.0
        }
    ]

    result_payload = [
        {
            'name': payload[0]['name'],
            'description': payload[0]['description'],
            'total_price': sum([
                payload[0]['motherboard'],
                payload[0]['memory'],
                payload[0]['cpu'],
                payload[0]['gpu'],
            ])
        },
        {
            'name': payload[1]['name'],
            'description': payload[1]['description'],
            'total_price': sum([
                payload[1]['motherboard'],
                payload[1]['memory'],
                payload[1]['cpu'],
                payload[1]['gpu'],
            ])
        },
        {
            'name': payload[2]['name'],
            'description': payload[2]['description'],
            'total_price': sum([
                payload[2]['memory'],
                payload[2]['ssd1'],
                payload[2]['ssd2'],
                payload[2]['ssd3'],
            ])
        }
    ]

    return payload, sorted(result_payload, key=lambda x: x["total_price"])

def get_typical_command_and_payload():
    basic_command = get_basic_command()

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
    #basic_command, basic_payload = get_typical_command_and_payload()
    #pprint(basic_command)
    #pprint(basic_payload)
    #payload, result = get_typical_payload_and_price_comparison_result()
    #pprint(result)
    command, result = get_typical_command_and_price_comparison_result()
    pprint(command)
    pprint(result)