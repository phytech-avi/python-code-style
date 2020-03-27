
# С питона версии 3 не пишем слово object


class BaseModel():
    """ ? Комментарии для классов
    """

    def __init__(self, arg1: int, arg2: str):
        """? Комменатрии дял методов класса
        """

        # ? Когда использовать атрибуты, начинающиеся с __
        # ? И использовать ли их вообще?
        self.__private = "private"
        # Приватный атрибут. Начинается с _
        self._protected_attr = arg1
        # Публичный атрибут
        self.attr = arg2

    # Публичный метод
    def public_method(self, str_number: str) -> int:
        return int(str_number)

    def _protected_method(self, str_number: str) -> int:
        return int(str_number)

    # ? Использовать ли методы, начинающиеся с __?
    def __private_method(self, str_number: str) -> int:
        return int(str_number)


class Model(BaseModel):

    def __init__(self, arg1, arg2):
        super().__init__(arg1, arg2)
