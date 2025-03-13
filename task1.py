import doctest

if __name__ == '__main__':


class Elements:
    def __init__(self, mass: float, group: int, number: int, element_type: str = 'Metall'):

    # >>> elements = Elements(51.9, 6, 4)
    self._mass = None
    self._group = None
    self._number = None
    self._element_type = 'Metall'
    self.mass = mass
    self.group = group
    self.number = number

    @property
    def mass(self) -> float:
        return self._mass

    @mass.setter
    def mass(self, mass: float) -> None:
        if not isinstance(mass, int):
            raise TypeError('Масса должна быть типа float')
        if mass <= 0:
            raise ValueError('Масса не может быть меньше 0')
        self._mass = mass

    @property
    def group(self) -> int:
        return self._group

    @group.setter
    def group(self, group: int) -> None:
        if not isinstance(group, int):
            raise TypeError('Группа должна быть типа int')
        if group <= 0:
            raise ValueError('Группа не может быть меньше 0')
        self._group = group

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, number: int) -> None:
        if not isinstance(number, int):
            raise TypeError('Номер должен быть типа int')
        if number <= 0:
            raise ValueError('Номер не может быть меньше 0')
        self._number = number

    def mass(self) -> float:
        >> > elements = Elements(51.9, 6, 4)
        >> > mass = elements.mass()

    def group(self) -> int:
        >> > elements = Elements(51.9, 6, 4)
        >> > group = elements.group()

    def characteristic(self) -> str:
        elements = Elements(51.9, 6, 4)
        characteristic = elements.characteristic()
        return f""" Элемент:
        массой = {self._mass},  номер элемента = {self.number}
        Относится к группе {self.group}
        """

    def __str__(self):
        return f""" Элемент:
        Масса: {self._mass};
        Номер элемента: {self._number};
        Тип элемента: {self.element_type}"""

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._mass!r}, {self.group!r}, {self.element_type})'


class Vanadium(Elements):
    def __init__(self, mass: float, element_type: str = 'Metall'):
        if not isinstance(mass, float):
            raise TypeError('Масса должна быть типа float')

    if not isinstance(element_type, str):
        raise TypeError('Тип элемента должен быть типа str')
    super().__init__(mass, 'Ванадий', element_type)

    def characteristic(self):
        return f"""{super().characteristic()}
        Элемент:
        массой = {self.mass}, номер элемента = 
        Относится к группе:
        """


