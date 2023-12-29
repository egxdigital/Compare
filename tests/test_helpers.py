import random
from decimal import Decimal, ROUND_HALF_UP

from faker import Faker

from compare.helpers import decimal_quantize

def get_basic_command():
    fake = Faker()

    return [
        'price',
        '-c',
            f'name={fake.word()}',
            f'partA={random.uniform(10, 50):.2f}',
            f'partB={random.uniform(10, 50):.2f}',
            f'p={round(random.uniform(100, 150), 2)}',
            f'qt={random.randint(1, 10)}',
            f'desc={fake.sentence()}',
            f'priority={round(random.uniform(1, 10), 2)}',
        '-c',
            f'n={fake.word()}',
            f'partA={random.uniform(10, 50):.2f}',
            f'partB={random.uniform(10, 50):.2f}',
            f'dist={random.uniform(10, 50):.2f}',
            f't={round(random.uniform(100, 500), 2)}',
            f'wt={round(random.uniform(100, 500), 2)}',
        '-c',
            f'name={fake.word()}',
            f'desc={fake.word()}',
            f'partA={random.uniform(10, 50):.2f}',
            f'partB={random.uniform(10, 50):.2f}',
            f'sp={round(random.uniform(100, 500), 2)}'
    ]

def get_typical_command_and_price_comparison_result():
    command = get_basic_command()
    result = [
        {
            'name': command[2].split('=')[1],
            'total_price': sum([
                Decimal(command[3].split('=')[1]),
                Decimal(command[4].split('=')[1]),
            ]),            
            'description': command[7].split('=')[1],
        },
        {
            'name': command[10].split('=')[1],
            'total_price': sum([
                Decimal(command[11].split('=')[1]),
                Decimal(command[12].split('=')[1]),
            ]),            
            'description': 'N/A',
        },
        {
            'name': command[17].split('=')[1],
            'total_price': sum([
                Decimal(command[19].split('=')[1]),
                Decimal(command[20].split('=')[1]),
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
                Decimal(payload[0]['motherboard']),
                Decimal(payload[0]['memory']),
                Decimal(payload[0]['cpu']),
                Decimal(payload[0]['gpu']),
            ]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        },
        {
            'name': payload[1]['name'],
            'description': payload[1]['description'],
            'total_price': sum([
                Decimal(payload[1]['motherboard']),
                Decimal(payload[1]['memory']),
                Decimal(payload[1]['cpu']),
                Decimal(payload[1]['gpu']),
            ]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        },
        {
            'name': payload[2]['name'],
            'description': payload[2]['description'],
            'total_price': sum([
                Decimal(payload[2]['memory']),
                Decimal(payload[2]['ssd1']),
                Decimal(payload[2]['ssd2']),
                Decimal(payload[2]['ssd3']),
            ]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        }
    ]

    return payload, sorted(result_payload, key=lambda x: x["total_price"])

def get_typical_command_and_payload():
    basic_command = get_basic_command()

    basic_payload = [
        {'name': basic_command[2].split('=')[1], 
         'partA': Decimal(basic_command[3].split('=')[1]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
         'partB': Decimal(basic_command[4].split('=')[1]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), 
         'price': float(basic_command[5].split('=')[1]),
         'quantity': float(basic_command[6].split('=')[1]), 
         'description': basic_command[7].split('=')[1],
         'priority': float(basic_command[8].split('=')[1])},

        {'name': basic_command[10].split('=')[1], 
         'partA': Decimal(basic_command[11].split('=')[1]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
         'partB': Decimal(basic_command[12].split('=')[1]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), 
         'distance': float(basic_command[13].split('=')[1]),
         'time': float(basic_command[14].split('=')[1]), 
         'weight': float(basic_command[15].split('=')[1])},

        {'name': basic_command[17].split('=')[1], 
         'description': basic_command[18].split('=')[1],
         'partA': Decimal(basic_command[19].split('=')[1]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), 
         'partB': Decimal(basic_command[20].split('=')[1]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
         'speed': float(basic_command[21].split('=')[1])},
    ]

    return basic_command, basic_payload

if __name__ == '__main__':
    from pprint import pprint
    # Example usage:
    #basic_command, basic_payload = get_typical_command_and_payload()
    #pprint(basic_command)
    #pprint(basic_payload)
    payload, result = get_typical_payload_and_price_comparison_result()
    pprint(result)
    #command, result = get_typical_command_and_price_comparison_result()
    #pprint(command)
    #pprint(result)