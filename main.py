from store import Store
from shop import Shop
from request import Request


store = Store(
    items={
        "хлеб": 23,
        "масло": 25,
        "виноград":10,
        "сыр":20
    }
)

shop = Shop(
    items={
        "хлеб": 2,
        "масло":3,
        "яблоки":2,
        "сахар":1,
        "сыр":2
    }
)

storages = {
    "магазин": shop,
    "склад": store
}


while True:
    #Вывод состояния складов/магазинов
    for storage_unit in storages:
        print(f"{storage_unit}, товаров всего: {storages[storage_unit].get_items()}, свободно: {storages[storage_unit].get_free_space()}")

    #формирование запроса пользователем
    user_input = input(
        'Пример запроса: "Доставить 3 сахар на склад из магазин" или "перевезти 5 хлеб в магазин со склад"\n'
        'Для остановки операции набрать: "готово"\n'
    )

    if "готово" in user_input:
        break

    #обработка запроса
    request = Request(request=user_input, storages=storages)

    if storages[request.deliver_from].remove(request.prod, request.amount):
        print(f"Из {request.deliver_from} забрали {request.amount} {request.prod}")

        if storages[request.deliver_to].add(request.prod, request.amount):
            print(f"В {request.deliver_to} доставили {request.amount} {request.prod}")
        else:
            storages[request.deliver_from].add(request.prod, request.amount)
            print(f"В {request.deliver_from} вернули {request.amount} {request.prod}")
