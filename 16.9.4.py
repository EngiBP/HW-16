#Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов. Вам необходимо написать программу,
# которая позволит составить список гостей. В класс «Клиент» добавьте метод, который будет возвращать информацию
# только об имени, фамилии и городе клиента.

#Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.


class Client:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def privacy_data_сlient(self):
        return f'Client: {self.first_name} {self.last_name}. {self.city}. Баланс: {self.balance} руб.'

    def data_clients(self):
        return f'Client: {self.first_name} {self.last_name}. {self.city}.'


client_1 = Client('Иван', 'Петров', 'Москва', 50)
client_2 = Client('Петр', 'Сидоров', 'Кемерово', 1000)
client_3 = Client('Тимофей', 'Иванов', 'Новосибирск', 0)


сlients_list = [client_1, client_2, client_3]

for сlient in сlients_list:
    print(сlient.data_clients())