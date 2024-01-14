import random
from decimal import Decimal, ROUND_HALF_UP

from faker import Faker

valid_attribute_types = {
    'name': 'string',
    'description': 'string',
    'dimensions': 'string',
    'price': 'float',
    'weight': 'float',
    'quantity': 'float',            
    'speed': 'float',
    'distance': 'float',
    'time': 'float',
    'priority': 'float'
}

def get_typical_command():
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

def get_typical_payload():
    return [
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

def get_typical_payload_with_total_price():
    payload = get_typical_payload()
    for component in payload:
        total_price = 0
        for key, value in component.items():
            if key not in valid_attribute_types:
                total_price += Decimal(value).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        component['total_price'] = total_price
    return payload

def get_typical_payload_with_weights_and_score_comparison_result():
    payload = get_typical_payload_with_total_price()
    
    weights = {
        'total_price': -0.1,
        'weight': -0.3,
        'priority': 0.6
    }
    
    result = [
        {
            'name': 'Server Workstation #1',
            'description': "High performance workstation for running VM's",
            'motherboard': 340.99,
            'memory': 149.99,
            'cpu': 120.42,
            'gpu': 299.99,
            'total_price': Decimal('340.99') +Decimal('149.99') + Decimal('120.42') + Decimal('299.99'),
            'priority': 0.5,
            'weight': 5.0,
            'score_by': ['total_price', 'weight', 'priority'], 
            'score': Decimal('-92.34'),
            'transformed_score': Decimal('0.00')
        },
        {
            'name': 'Server Workstation #2',
            'description': "High performance workstation for running VM's",
            'motherboard': 299.99,
            'memory': 149.99,
            'cpu': 120.42,
            'gpu': 312.99,
            'total_price': Decimal('299.99') +Decimal('149.99') + Decimal('120.42') + Decimal('312.99'),
            'priority': 0.5,
            'weight': 7.0,
            'score_by': ['total_price', 'weight', 'priority'],
            'score': Decimal('-90.14'),
            'transformed_score': Decimal('3.30')
        },
        {
            'name': 'Raid Setup',
            'description': "Extend existing computer's space and upgrade other parts",
            'memory': 100.24,
            'ssd1': 49.99,
            'ssd2': 49.99,
            'ssd3': 49.99,
            'total_price': Decimal('100.24') + Decimal('49.99') + Decimal('49.99') + Decimal('49.99'),
            'priority': 1,
            'weight': 4.0,
            'score_by': ['total_price', 'weight', 'priority'],
            'score': Decimal('-25.62'),
            'transformed_score': Decimal('100.00'),
        }
    ]

    return payload, weights, result[::-1]

def get_typical_payload_and_price_comparison_result():
    payload = get_typical_payload()

    result_payload = [
        {
            'name': payload[0]['name'],
            'description': payload[0]['description'],
            'motherboard': payload[0]['motherboard'],
            'memory': payload[0]['memory'],
            'cpu': payload[0]['cpu'],
            'gpu': payload[0]['gpu'],
            'priority': payload[0]['priority'],
            'weight': payload[0]['weight'],
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
            'motherboard': payload[1]['motherboard'],
            'memory': payload[1]['memory'],
            'cpu': payload[1]['cpu'],
            'gpu': payload[1]['gpu'],
            'priority': payload[1]['priority'],
            'weight': payload[1]['weight'],
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
            'memory': payload[2]['memory'],
            'ssd1': payload[2]['ssd1'],
            'ssd2': payload[2]['ssd2'],
            'ssd3': payload[2]['ssd3'],
            'priority': payload[2]['priority'],
            'weight': payload[2]['weight'],
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
    basic_command = get_typical_command()

    part_list = [
        {
            'partA': Decimal(basic_command[3].split('=')[1]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
            'partB': Decimal(basic_command[4].split('=')[1]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        },
        {
            'partA': Decimal(basic_command[11].split('=')[1]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
            'partB': Decimal(basic_command[12].split('=')[1]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), 
        },
        {
            'partA': Decimal(basic_command[19].split('=')[1]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), 
            'partB': Decimal(basic_command[20].split('=')[1]).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        }
    ]

    basic_payload = [
        {'name': basic_command[2].split('=')[1], 
         'partA': part_list[0]['partA'],
         'partB': part_list[0]['partB'],
         'price': float(basic_command[5].split('=')[1]),
         'total_price': sum([
            part_list[0]['partA'],
            part_list[0]['partB'],
         ]),
         'quantity': float(basic_command[6].split('=')[1]), 
         'description': basic_command[7].split('=')[1],
         'priority': float(basic_command[8].split('=')[1])},

        {'name': basic_command[10].split('=')[1], 
         'partA': part_list[1]['partA'],
         'partB': part_list[1]['partB'],
         'total_price': sum([
             part_list[1]['partA'],
             part_list[1]['partB'],
         ]),
         'distance': float(basic_command[13].split('=')[1]),
         'time': float(basic_command[14].split('=')[1]), 
         'weight': float(basic_command[15].split('=')[1])},

        {'name': basic_command[17].split('=')[1], 
         'description': basic_command[18].split('=')[1],
         'partA': part_list[2]['partA'],
         'partB': part_list[2]['partB'],
         'total_price': sum([
            part_list[2]['partA'],
            part_list[2]['partB'],
         ]),
         'speed': float(basic_command[21].split('=')[1])},
    ]

    return basic_command, basic_payload

if __name__ == '__main__':
    from pprint import pprint
    # Example usage:
    #basic_command, basic_payload = get_typical_command_and_payload()
    #pprint(basic_command)
    #pprint(basic_payload)
    #payload, result = get_typical_payload_and_price_comparison_result()
    #pprint(result)