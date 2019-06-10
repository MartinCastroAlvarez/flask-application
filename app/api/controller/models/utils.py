"""
Roman Numbers Converter.

Reference:
https://gist.github.com/riverrun/ac91218bb1678b857c12
"""

import typing


class Roman(int):
    """
    Roman number entity.
    """

    MAP = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        10: 'X',
        20: 'XX',
        30: 'XXX',
        40: 'XL',
        50: 'L',
        60: 'LX',
        70: 'LXX',
        80: 'LXXX',
        90: 'XC',
        100: 'C',
        200: 'CC',
        300: 'CCC',
        400: 'CD',
        500: 'D',
        600: 'DC',
        700: 'DCC',
        800: 'DCCC',
        900: 'CM',
        1000: 'M',
        2000: 'MM',
        3000: 'MMM'
    }

    def __new__(cls, number: int):
        """
        Class helper.
        @raises: ValueError.
        """
        if number > 3999:
            raise ValueError('Values over 3999 are not allowed:', number)
        return super().__new__(cls, number)

    def __init__(self, number: int) -> None:
        """
        Roman number constructor.
        """
        self.__arabic = number

    @property
    def arabic(self) -> int:
        """
        Arabic number getter.
        """
        return self.__arabic

    def get_roman(self) -> str:
        """
        Roman number getter.
        """
        return ''.join([
            self.MAP.get(num)
            for num in self
        ][::-1])

    def __iter__(self) -> typing.Generator:
        """
        Class iterator.
        """
        number = str(self.arabic)
        count = 1
        for digit in number[::-1]:
            if digit != '0':
                yield int(digit) * count
            count *= 10
