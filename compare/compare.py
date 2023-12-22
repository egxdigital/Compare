"""Compare

This module contains the main function definitions for the Compare program.
"""
from compare.config import *
from compare.helpers import *

class Compare():
    def __init__(self, parser, options):
        self.valid_commands = [
            'prices'
        ]

        self.valid_flags = [
            'components'
        ]

        self.parser = parser
        self.options = options
        self.command = ''

        self.validate_command()

    def __repr__(self):
        return (
            'command: {}\n'
            'options: {}\n'
        ).format(
            self.command,
            self.options
        )
    
    def __str__(self):
        return (
            'compare {} for {} components'
        ).format(
            self.command,
            len(self.options['components'])            
        )

    def validate_command(self):
        if self.options['commands'][0] not in self.valid_commands:
            self.parser.error('bad command!')
        self.command=self.options['commands'][0]

    def _parse_components(self):
        pass