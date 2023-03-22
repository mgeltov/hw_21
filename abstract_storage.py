from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    def __init__(self, items:dict[str, int], capacity: int):
        self.items = items
        self.capacity = capacity

    @abstractmethod
    def add(self, name: str, amount: int):
        pass

    @abstractmethod
    def remove(self, name: str, amount: int):
        pass

    @abstractmethod
    def get_used_space(self):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def unique_items_count(self):
        pass

    @abstractmethod
    def get_items(self):
        pass
