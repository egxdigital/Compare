"""Compare

This module contains the main function definitions for the Compare program.
"""
from compare.config import *
from compare.helpers import *

class Compare():
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

    def __init__(self, parser, options):
        self.valid_commands = {
            'price': self._run_price_comparison
        }

        self.valid_flags = [
            'components'
        ]

        self.valid_attribute_types = self.__class__.valid_attribute_types

        self.parser = parser
        self.options = options
        self.command = ''

        self.payload = []
        self.result_payload = []
        self._validate_command()
        self._validate_and_load_attributes()
        self.valid_commands[self.command]()

    def __repr__(self):
        return (
            f'command: {self.command}\n'
            f'options: {self.options}\n'
            f'payload: {self.payload}\n'
            f'resultP: {self.result_payload}\n'
        )
    
    def __str__(self):
        return (
            f"compare {self.command} for {len(self.options['components'])} components"
        )

    def _validate_command(self):
        if self.options['commands'][0] not in self.valid_commands:
            self.parser.error('bad command!')
        self.command=self.options['commands'][0]

    def _validate_and_load_attributes(self):
        for component in self.options['components']:
            component_dict = {}
            for attribute_string in component:
                attr_name, attr_value = attribute_string.split('=')
                full_attr_name = self.__handle_alias_or_partial_attr_name(attr_name)
                attr_type = self.valid_attribute_types.get(full_attr_name)

                if attr_type:
                    interpreted_value = self.__interpret_attribute(attr_value, attr_type)
                    component_dict[full_attr_name] = interpreted_value
                else:
                    component_dict[full_attr_name] = float(attr_value)

            self.payload.append(component_dict)
    
    def __interpret_attribute(self, attr_value, attr_type):
        if attr_type == 'string':
            return str(attr_value)
        elif attr_type == 'integer':
            return int(attr_value)
        elif attr_type == 'float':
            return float(attr_value)
        else:
            return attr_value
    
    def __handle_alias_or_partial_attr_name(self, attr_name:str) -> str:
        alias_mapping = {
            'qty': 'quantity',
            'wt': 'weight'
        }
        
        for alias, full_name in alias_mapping.items():
            if alias.startswith(attr_name):
                return full_name
        
        for full_name in self.valid_attribute_types:
            if full_name.startswith(attr_name):
                return full_name
        
        return attr_name
    
    @classmethod
    def compare_by_price(cls, payload):
        result = []
        for index, component in enumerate(payload):
            total_price = sum(value for key, value in component.items() if key not in Compare.valid_attribute_types)
            result.append({
                "name": component.get("name") or f"Component {index+1}",
                "description": component.get("description") or "N/A",
                "total_price": total_price
                })
        return sorted(result, key=lambda x: x["total_price"])

    def _run_price_comparison(self):
        self.result_payload = self.compare_by_price(self.payload)
        return self.result_payload