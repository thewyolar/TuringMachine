import numpy as np

N = 1000  # Длина ленты


class TuringMachine:
    def __init__(self, program, data, state=0):
        self.program = program
        self.state = str(state)
        self.tape = ''.join(['_'] * N)
        self.head = N // 2
        self.tape = self.tape[:self.head] + data + self.tape[self.head:]

    def step(self):
        if self.state != 'H':
            current = self.tape[self.head]
            replacement, direct, state = self.program.get((self.state, current))
            self.tape = self.tape[:self.head] + replacement + self.tape[self.head + 1:]
            if direct != '*':
                if direct == 'r':
                    self.head += 1
                else:
                    self.head += -1
            self.state = state
            print(f"Лента МТ в текущем состоянии: {self.tape.replace('_', '')} {self.state}")

    def run(self, max_iter=9999):
        i = 0
        while self.state != 'H' and i < max_iter:
            self.step()
            i += 1
        print(f"Лента МТ в конечном состоянии: {self.tape.replace('_', '')} {self.state}")
        print(f"Кол-во итераций: {i}\n")


def add_numbers():
    # Программа для сложения двух чисел
    addition_program = {('0', '0'): ('0', 'r', '0'),
                        ('0', '1'): ('1', 'r', '0'),
                        ('0', '_'): ('_', 'r', '1'),
                        ('1', '0'): ('0', 'r', '1'),
                        ('1', '1'): ('1', 'r', '1'),
                        ('1', '_'): ('_', 'l', '2'),
                        ('2', '0'): ('1', 'l', '2'),
                        ('2', '1'): ('0', 'l', '3'),
                        ('2', '_'): ('_', 'r', '5'),
                        ('3', '0'): ('0', 'l', '3'),
                        ('3', '1'): ('1', 'l', '3'),
                        ('3', '_'): ('_', 'l', '4'),
                        ('4', '0'): ('1', 'r', '0'),
                        ('4', '1'): ('0', 'l', '4'),
                        ('4', '_'): ('1', 'r', '0'),
                        ('5', '1'): ('_', 'r', '5'),
                        ('5', '_'): ('_', '*', 'H')}

    print("\n---------Сложение чисел---------")
    n = int(input("Введите первое число: "))
    m = int(input("Введите второе число: "))

    data = np.binary_repr(n) + "_" + np.binary_repr(m)

    tm = TuringMachine(addition_program, data)
    tm.run()


def check_palindrome():
    # Программа для обнаружения палиндрома
    palindrome_program = {('0', '0'): ('0', 'r', '0'),
                          ('0', '_'): ('_', 'l', '1'),
                          ('0', '1'): ('1', 'r', '0'),
                          ('1', '_'): ('1', '*', 'H'),
                          ('1', '0'): ('_', 'l', '2'),
                          ('1', '1'): ('_', 'l', '4'),
                          ('2', '_'): ('_', 'r', '3'),
                          ('2', '0'): ('0', 'l', '2'),
                          ('2', '1'): ('1', 'l', '2'),
                          ('3', '_'): ('_', '*', '0'),
                          ('3', '0'): ('_', 'r', '0'),
                          ('3', '1'): ('1', '*', '6'),
                          ('4', '_'): ('_', 'r', '5'),
                          ('4', '0'): ('0', 'l', '4'),
                          ('4', '1'): ('1', 'l', '4'),
                          ('5', '_'): ('_', '*', '0'),
                          ('5', '0'): ('0', '*', '6'),
                          ('5', '1'): ('_', 'r', '0'),
                          ('6', '_'): ('0', '*', 'H'),
                          ('6', '0'): ('_', 'r', '6'),
                          ('6', '1'): ('_', 'r', '6')}

    print("\n---------Обнаружение палиндрома---------")
    data = input("Введите последовательность: ")

    tm = TuringMachine(palindrome_program, data)
    tm.run()


def bin_to_un():
    # Программа для преобразования двоичного числа в унарное
    bin_to_un_program = {('0', '0'): ('0', 'r', '0'),
                         ('0', '1'): ('1', 'r', '0'),
                         ('0', '_'): ('_', 'l', '1'),
                         ('1', '1'): ('0', 'r', '2'),
                         ('1', '0'): ('1', 'l', '1'),
                         ('1', '_'): ('_', 'r', '5'),
                         ('2', '0'): ('0', 'r', '2'),
                         ('2', '1'): ('1', 'r', '2'),
                         ('2', '_'): ('_', 'r', '3'),
                         ('3', '_'): ('1', 'l', '4'),
                         ('3', '1'): ('1', 'r', '3'),
                         ('4', '1'): ('1', 'l', '4'),
                         ('4', '_'): ('_', 'l', '1'),
                         ('5', '1'): ('_', 'r', '5'),
                         ('5', '_'): ('_', 'r', 'H')}

    print("\n---------Преобразование двоичного числа в унарное---------")
    data = input("Введите двоичное число: ")

    tm = TuringMachine(bin_to_un_program, data)
    tm.run()


def un_to_bin():
    # Программа для преобразования унарного числа в двоичное
    un_to_bin_program = {('0', '1'): ('1', 'r', '0'),
                         ('0', '_'): ('_', 'l', '1'),
                         ('1', '1'): ('_', 'l', '2'),
                         ('1', '_'): ('_', '*', 'H'),
                         ('2', '1'): ('1', 'l', '2'),
                         ('2', '_'): ('_', 'l', '3'),
                         ('3', '_'): ('1', 'r', '4'),
                         ('3', '0'): ('1', 'r', '4'),
                         ('3', '1'): ('0', 'l', '3'),
                         ('4', '0'): ('0', 'r', '4'),
                         ('4', '1'): ('1', 'r', '4'),
                         ('4', '_'): ('_', 'r', '0')}

    print("\n---------Преобразование унарного числа в двоичное---------")
    data = input("Введите унарное число: ")

    tm = TuringMachine(un_to_bin_program, data)
    tm.run()


def double_length_sequence():
    # Программа для удвоения длины последовательности
    double_length_sequence_program = {('0', '1'): ('_', 'r', '1'),
                                      ('1', '1'): ('1', 'r', '1'),
                                      ('1', '_'): ('_', 'r', '2'),
                                      ('2', '1'): ('1', 'r', '2'),
                                      ('2', '_'): ('1', 'r', '3'),
                                      ('3', '_'): ('1', 'l', '4'),
                                      ('4', '1'): ('1', 'l', '4'),
                                      ('4', '_'): ('_', 'l', '5'),
                                      ('5', '1'): ('1', 'l', '5'),
                                      ('5', '_'): ('_', 'r', '6'),
                                      ('6', '1'): ('_', 'r', '1'),
                                      ('6', '_'): ('_', 'r', 'H')}

    print("\n---------Удвоение длины последовательности---------")
    data = input("Введите последовательность единиц: ")

    tm = TuringMachine(double_length_sequence_program, data)
    tm.run()


if __name__ == "__main__":
    response = True
    print("============Машина Тьюринга============")
    while response:
        command = input("\nКоманды:\n 1 - Сложение двух чисел.\n 2 - Проверка на палиндром.\n 3 - Перевод бинарного "
                        "числа в унарное.\n 4 - Перевод унарного числа в бинарное.\n 5 - Удвоение длины "
                        "последовательности.\n")

        match command.split():
            case ['1']:
                add_numbers()
            case ['2']:
                check_palindrome()
            case ['3']:
                bin_to_un()
            case ['4']:
                un_to_bin()
            case ['5']:
                double_length_sequence()
            case _:
                print(f"Невозможно выполнить команду {command!r}!")

        answer = input("Хотите продолжить? (Y/n): ")
        response = True if answer == 'Y' else False