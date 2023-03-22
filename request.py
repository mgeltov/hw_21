from abstract_storage import AbstractStorage

class Request:
    def __init__(self, request: str, storages: dict[str, AbstractStorage]):
        request_list = request.lower().split(' ')

        if len(request_list) != 7:
            print('Некорректный формат')
            return None

        self.amount = int(request_list[1])
        self.prod = request_list[2]
        self.deliver_to = request_list[4]
        self.deliver_from = request_list[6]
