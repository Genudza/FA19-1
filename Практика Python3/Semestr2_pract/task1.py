"""
Вычислить сумму N членов ряда, заданного в Приложении 1, согласно номеру варианта.
1. Вывести рекуррентную формулу для расчета очередного слагаемого, а также определить начальные значения для слагаемого и суммы.
2. Разработать блок-схему алгоритма.
3. На языке Python реализовать разработанный алгоритм.
Значения x задаются по вводу с клавиатуры.
Если введённое значение не удовлетворяет заданному ограничению,
вывести в командное окно соответствующее сообщение и повторить ввод.
4. Произвести расчёты для нескольких значений N 
(5≤N≤10)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
"""
from math import pi

class Main:
    def __init__(self):
        self.x_find = False
        self.n_find = False
        self.result_sum = 0
        #Ввод данных
        while not self.x_find:
            self.x_input()
        while not self.n_find:
            self.n_input()

        self.calculating(0, self.x, self.n)
        print("Общая сумма: "+str(self.result_sum))

    def x_input(self):
        """
        Метод для ввода данных по x
        """
        try:
            x = float(input("Введите x: "))
            if x <= 1:
                print("Введённое значение не удовлетворяет заданному диапазону")
            else:
                self.x_find = True
                self.x = x
        except ValueError:
            print("Некорректный ввод данных") 

    def n_input(self):
        """
        Метод для ввода данных по n
        """
        try:
            self.n = int(input("Введите n: "))
            self.n_find = True
        except ValueError:
            print("Некорректный ввод данных") 

    def calculating(self, i, x, n_stop):
        """
        Рекурсивный метод для вычисления N элемента (так требует задание)
        """
        result = (pi/2)+pow(-1,i+1)* 1/((2*i+1)*pow(x,2*i+1))
        self.result_sum += result
        print("i = "+str(i)+", результат: "+str(result))
        #Остановка 
        if i == n_stop:
            return
        self.calculating(i+1, x, n_stop)
        

if __name__ == "__main__":
    Main()