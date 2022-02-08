from pymongo import MongoClient
client = MongoClient("mongodb+srv://sixteenx:Donik16@cluster0.fusww.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
db = client['BankAccount']
collection_user = db['user_info']
collection_transaction = db['transaction_info']
# my_dict = {
#     'name': 'John',
#     'surname': 'Brown',
#     'card number': '1223344',
#     'pin-code': '1991',
#     'card balance': '300000'
# }
# my_dict2 = {
#     'name': 'Adin',
#     'surname': 'Ross',
#     'card number': '9988767',
#     'pin-code': '11222',
#     'card balance': '500000'
# }
# my_dict3 = {
#     'name': 'Emma',
#     'surname': 'Luis',
#     'card number': '3334455',
#     'pin-code': '1641',
#     'card balance': '180000'
# }
# my_list = [{my_dict, my_dict2, my_dict3}]
# collection_user.insert_many(my_list)
from datetime import datetime
class account:
    def __init__(self):
            print('Добро пожаловать в банкомат академии!')
            int(input('Чтобы приступить введите цифру "1": '))
            self.name = str(input('Введите имя:'))
            self.surname = str(input('Введите свою фамилию:'))

    def user_info(self):
        user_list = {
            # 'name': [],
            # 'surname': [],
            # 'card number': [],
            # 'pin-code': [],
            # 'balance': []
        }
        card_number = int(input('Введите номер карты:'))
        pin_code = int(input('Введите пин-код:'))
        balance = int(input('Ваш баланс:'))
        # user_list['name'].append(self.name)
        # user_list['surname'].append(self.surname)
        # user_list['card number'].append(card_number)
        # user_list['pin-code'].append(pin_code)
        # user_list['balance'].append(balance)
        user_list['name'] = self.name
        user_list['surname'] = self.surname
        user_list['card_number'] = card_number
        user_list['pin_code'] = pin_code
        user_list['balance'] = balance
        collection_user.insert_one(user_list)

    def transaction_info(self):
        transaction_list = {
            # 'name': [],
            # 'surname': [],
            # 'transaction amount': [],
            # 'date': []
        }
        amount = int(input('Введите сумму транкзации:'))
        current_date = datetime.now().date()
        # transaction_list['name'].append(self.name)
        # transaction_list['surname'].append(self.surname)
        # transaction_list['transaction amount'].append(amount)
        # transaction_list['date'].append(current_date)
        transaction_list['name'] = self.name
        transaction_list['surname'] = self.surname
        transaction_list['transaction amount'] = amount
        transaction_list['date'] = str(current_date)
        collection_transaction.insert_one(transaction_list)


s = account()
s.user_info()
s.transaction_info()

# 2_TASK
# from pymongo import MongoClient
client = MongoClient("mongodb+srv://sixteenx:Donik16@cluster0.fusww.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
db = client['online_shop']
collection_product_info = db['product_info']
collection_user_info = db['user_info']







#
# my_dict = {
#     'product_name': 'T-shirt',
#     'quantity': '520'
#  }
# my_dict2 = {
#     'product_name': 'Jacket',
#     'quantity': '200'
#  }
# my_dict3 = {
#     'product_name': 'Jeans',
#     'quantity': '340'
#  }
# my_dict4 = {
#     'product_name': 'Shorts',
#     'quantity': '130'
# }
# my_list = [my_dict, my_dict2, my_dict3, my_dict4]
# collection_product_info.insert_many(my_list)
class OnlineShop:
    def __init__(self):
        print('Добро пожаловать в онлайн магазин Академии!')
        self.post = False
        self.is_login = False
        self.balance = 0
        # my_dict = {
        #     'name': 'John',
        #     'surname': 'Woods',
        #     'login': 'johnwoods@gmail.com',
        #     'password': 'john22',
        #     'card balance': self.balance
        # }
        # my_dict2 = {
        #     'name': 'Adin',
        #     'surname': 'Ross',
        #     'login': 'adin@gmail.com',
        #     'password': 'adin11222',
        #     'card balance': self.balance
        # }
        # my_dict3 = {
        #     'name': 'Emma',
        #     'surname': 'Good',
        #     'login': 'emma213@gmail.com',
        #     'password': 'emmag1641',
        #     'card balance': self.balance
        # }
        # my_dict4 = {
        #     'name': 'James',
        #     'surname': 'Osborn',
        #     'login': 'JamesOsborn@gmail.com',
        #     'password': 'james0220',
        #     'card balance': self.balance,
        #     'post': 'admin'
        # }
        # collection_user_info.insert_one(my_dict)
        # collection_user_info.insert_one(my_dict2)
        # collection_user_info.insert_one(my_dict3)
        # collection_user_info.insert_one(my_dict4)

    def user_info(self):
        choice = 1
        while choice != 0:
            print('1- Войти в существующий аккаунт')
            print('2- Зарегистрироваться в сети ')
            choice = int(input('1, либо 2:'))
            if choice == 1:
                print('введите логин и пароль:')
                find_login = input('Введите логин:')
                user_finder = collection_user_info.find_one({'login': find_login})
                if user_finder is not None:
                    self.is_login = True
                    print('Здравствуйте,', user_finder['name'])
                    s.user_functions()
                    if user_finder['post'] == 'admin':
                        self.post = True
                        s.admin_functions()
            elif choice == 2:
                user_list = {

                }
                name = str(input('Введите имя:'))
                surname = str(input('Введите фамилию:'))
                login = input('Ваш логин:')
                password = input('Придумайте пароль:')
                if "123" in password:
                    print("Простой!")

                elif len(password) < 8:
                    print("Короткий!")

                else:
                    print("Введите пароль повторно")
                    password2 = input()

                    if password2 == password:
                        print("OK")

                    else:
                        print("Различаются!")
                balance = 0
                user_list['name'] = name
                user_list['surname'] = surname
                user_list['login'] = login
                user_list['password'] = password
                user_list['balance'] = balance
                user_list['post'] = 'user'
                collection_user_info.insert_one(user_list)

    def admin_functions(self):
        print('Вы вошли как админ')
        print('Выберите функцию:''\n 1- Удалить пользователя', '2- Обновить данные пользователя', '3- Обновить данные '
                                                                                        'товара')
        choice = int(input('Выберите функцию:'))
        while choice != 0:
            if choice == 1:
                user_list = {

}
                name = str(input('Введите имя:'))
                surname = str(input('Введите фамилию:'))
                login = input('Ваш логин:')
                password = input('Придумайте пароль:')
                balance = int(input('Пополнить баланс:'))
                card = int(input('Номер карты:'))
                user_list['name'] = name
                user_list['surname'] = surname
                user_list['login'] = login
                user_list['password'] = password
                user_list['balance'] = balance
                user_list['card'] = card
                user_list['post'] = 'user'
                collection_user_info.insert_one(user_list)
            elif choice == 2:
                find_login = input('Введите логин пользователя которого хотите изменить:')
                user_finder = collection_user_info.find_one({'login': find_login})
                if user_finder is not None:
                    self.is_login = True
                    print(user_finder)
                    print('name- поменять имя', '\nsurname- поменять фамилию''\nbalance- пополнить баланс')
                    key = input('Выберите поле которое хотите изменить:')
                    current = input('Настоящее значение:')
                    admin_change = input('Значение на кторое вы хотите поменять:')
                    myquery = {key: current}
                    new_value = {'$set': {key: admin_change}}
                    collection_user_info.update_one(myquery, new_value)
            elif choice == 3:
                print('Товары:', 'T-shirt,', 'Jacket,', 'Jeans,', 'Shorts')
                product_name = input('Название товара который хотите обновить:')
                product_finder = collection_product_info.find_one({'product_name': product_name})
                print(product_finder)
                print('product_name- обновить название товара', 'quantity- обновить количесвто товара')
                key = input('Выберите поле которое хотите изменить:')
                current = input('Настоящее значение:')
                admin_change = input('Значение на кторое вы хотите поменять:')
                myquery = {key: current}
                new_value = {'$set': {key: admin_change}}
                collection_product_info.update_one(myquery, new_value)
    def user_functions(self):
        print('Вы вошли как пользователь!')
        print('Нажмите <1> чтобы приобрести товар.' '\nНажмите <2> чтобы пополнить баланс')
        choice = int(input('1, либо 2'))
        while choice != 0:
            if choice == 1:
                print('Товары:', 'T-shirt,', 'Jacket,', 'Jeans,', 'Shorts')
                key = input('Выберите товар который хотите приобрести:')
                collection_product_info.find_one({'product_name': key})
                amount = int(input('Количество:'))
                current_quantity = collection_product_info.find_one({'product_name': key})
                quantity = current_quantity['quantity']
                print(type(quantity), quantity)
                result = quantity - amount
                newvalues = {"$set": {'quantity': result}}
                collection_product_info.update_one(current_quantity, newvalues)
            elif choice == 2:
                card = int(input('Введите номер карты:'))
                amount = int(input('Пополнить на:'))
                current_amount = collection_user_info.find_one({'card_number': card})
                deposit = current_amount['card_balance']
                # print(type(deposit), deposit)
                result = deposit + amount
                new_values = {'$set': {'card_balance': result}}
                collection_user_info.update_one(current_amount, new_values)
                s.user_functions()


s = OnlineShop()
s.user_info()