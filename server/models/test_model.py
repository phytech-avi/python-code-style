"""Defined Database models
"""


# С питона версии 3 не пишем слово object
class BaseModel:
    """ Комментарии для классов
    """

    def __init__(self, arg1: int, arg2: str):
        """Комменатрии дял методов класса
        """
        self.__private = "private"
        self._protected_attr = arg1
        self.attr = arg2

    def public_method(self, str_number: str) -> int:
        return int(str_number)

    def _protected_method(self, str_number: str) -> int:
        return int(str_number)

    def __private_method(self, str_number: str) -> int:
        return int(str_number)


class Model(BaseModel):

    def __init__(self, arg1, arg2):
        super().__init__(arg1, arg2)
