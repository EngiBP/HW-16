#В проекте «Дом питомца» добавим новую услугу — электронный кошелек. Необходимо создать класс «Клиент»,
#который будет содержать данные о клиентах и их финансовых операциях. О клиенте известна следующая информация: имя, фамилия, город, баланс.

#Далее сделайте вывод о клиентах в консоль в формате: «Иван Петров. Москва. Баланс: 50 руб.»


class Client:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance
    def data_сlient(self):
        return f'Client: {self.first_name} {self.last_name}. {self.city}. Баланс: {self.balance} руб.'


client_1 = Client('Иван', 'Петров', 'Москва', 50)

print(client_1.data_сlient())