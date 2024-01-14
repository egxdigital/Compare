from typing import List
from decimal import Decimal, ROUND_HALF_UP
from compare.helpers import shift_and_scale_transformation, decimal_quantize

def score_by_weights(payload: List[dict], weights: dict) -> List[dict]:
    result = []
    for component in payload:
        overall_score = 0
        
        for weighted_attr, weight in weights.items():
            scored_attr = component.get(weighted_attr)
            denominator = sum(abs(_) for _ in list(weights.values()))
            
            if denominator == 0:
                return
            else:
                w_normalized = weight / sum(abs(_) for _ in list(weights.values()))
                
                if scored_attr:
                    if weighted_attr in ['total_price', 'price']:
                        score = float(component[weighted_attr]) * w_normalized
                        overall_score += score
                    else:
                        overall_score += component[weighted_attr] * w_normalized

        result.append({
            **component,
            'score_by': list(weights.keys()),
            'score': decimal_quantize(overall_score),
            })
    
    transformed_result = shift_and_scale_transformation(result)

    return sorted(transformed_result, key=lambda x: x['score'], reverse=True)

if __name__ == '__main__':
    p = [
        {
            'name': 'Server Workstation #1',
            'description': "High performance workstation for running VM's",
            'motherboard': 340.99,
            'memory': 149.99,
            'cpu': 120.42,
            'gpu': 299.99,
            'price': sum([340.99, 149.99, 120.42, 299.99]),
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
            'price': sum([299.99, 149.99, 120.42, 312.99]),
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
            'price': sum([100.24, 49.99, 49.99, 49.99]),
            'priority': 1,
            'weight': 4.0
        }
    ]
    w = {
        'price': -0.1,
        'weight': -0.3,
        'priority': 0.6
    }
    result = score_by_weights(p, w)
    #transformed_result = shift_and_scale_transformation(result)

    for res in result:
        print(res['name'], res['score'], res['transformed_score'])