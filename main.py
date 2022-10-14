import numpy as np

N = 1000  # Длина ленты


class TuringMachine:
    def __init__(self, program, data, state=0):
        self.program = dict()
        self.state = str(state)
        self.tape = ''.join(['_'] * N)
        self.head = N // 2
        self.tape = self.tape[:self.head] + data + self.tape[self.head:]
        for line in program.splitlines():
            s, a, r, d, s1 = line.split(' ')
            self.program[s, a] = (r, d, s1)

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
    program = open('programs/addition.txt').read()

    print("\n---------Сложение чисел---------")
    n = int(input("Введите первое число: "))
    m = int(input("Введите второе число: "))

    data = np.binary_repr(n) + "_" + np.binary_repr(m)

    tm = TuringMachine(program, data)
    tm.run()


def check_palindrome():
    # Программа для обнаружения палиндрома
    program = open('programs/palindrome.txt').read()

    print("\n---------Обнаружение палиндрома---------")
    data = input("Введите последовательность: ")

    tm = TuringMachine(program, data)
    tm.run()


def bin_to_un():
    # Программа для преобразования двоичного числа в унарное
    program = open('programs/bin_to_un.txt').read()

    print("\n---------Преобразование двоичного числа в унарное---------")
    data = input("Введите двоичное число: ")

    tm = TuringMachine(program, data)
    tm.run()


def un_to_bin():
    # Программа для преобразования унарного числа в двоичное
    program = open('programs/un_to_bin.txt').read()

    print("\n---------Преобразование унарного числа в двоичное---------")
    data = input("Введите унарное число: ")

    tm = TuringMachine(program, data)
    tm.run()


def double_length_sequence():
    # Программа для удвоения длины последовательности
    program = open('programs/double_length_sequence.txt').read()

    print("\n---------Удвоение длины последовательности---------")
    data = input("Введите последовательность единиц: ")

    tm = TuringMachine(program, data)
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
