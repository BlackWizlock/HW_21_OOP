from exeptions import InvalidRequest, BaseError, InvalidStorageName
from prog.courier import Courier
from prog.request import Request
from prog.shop import Shop
from prog.store import Store

store = Store(items={
        "печенька": 25,
        "собачка" : 25,
        "елка"    : 25
})

shop = Shop(items={
        "печенька": 2,
        "собачка" : 2,
        "елка"    : 2
})

storages = {
        "магазин": shop,
        "склад"  : store
}


def main():
    print("Добрый день!")
    while True:
        for storage_name in storages:
            print(f"Сейчас в {storage_name}: \n {storages[storage_name].get_items()}")
        user_input = input(
                "Введите запрос в формате \'Доставить 3 печенька из склад в магазин\'\n"
                "Введите \'stop\' или \'стоп\', если хотите закончить\n"
        )
        if user_input.lower() in ("stop", "стоп"):
            break
        try:
            request = Request(request=user_input, storages=storages)
        except (InvalidRequest, InvalidStorageName) as error:
            print(error.message)
            continue

        courier = Courier(
                request=request,
                storages=storages,
        )

        try:
            courier.move()
        except BaseError as error:
            print(error.message)
            courier.cancel()


if __name__ == '__main__':
    main()
