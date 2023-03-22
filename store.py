from abstract_storage import AbstractStorage

class Store(AbstractStorage):
    def __init__(self, items:dict[str, int], capacity:int=100):
        self.__items = items
        self.__capacity = capacity
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> bool:
        if self.get_free_space() < amount:
            print(f"Недостаточно места на складе, можем принять не более {self.get_free_space()} единиц (попытка добавить {amount} едииниц)\n")
            return False

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

        return True

    def remove(self, name: str, amount: int) -> bool:
        if name not in self.__items:
            print(f"Товара {name} нет на складе\n")
            return False

        if amount > self.__items[name]:
            print(f"На складе недостаточно товара {name}, всего на складе {self.__items[name]} единиц, а запрос на {amount} единиц\n")
            return False

        self.__items[name] -= amount

        if self.__items[name] == 0:
            self.__items.pop(name)

        return True

    def get_used_space(self):
        return sum(value for value in self.__items.values())

    def get_free_space(self):
        return self.__capacity - self.get_used_space()

    def unique_items_count(self):
        return len(self.__items)

    def get_items(self):
        return self.__items
