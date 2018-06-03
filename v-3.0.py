from Essentials import console
Cycle = 0
while Cycle < 1:
    console.clear()
    print("█──█─████───██─█────█──█─█─█───██─█──█─███─████─████")
    print("█─█──█──█──█─█─█────█─█──█─█──█─█─█──█──█──█──█─█──█")
    print("██───████─█──█─████─██───███─█──█─█─██──█──█──█─████")
    print("█─█──█──█─█──█─█──█─█─█────█─█──█─██─█──█──█──█─█")
    print("█──█─█──█─█──█─████─█──█─███─█──█─█──█──█──████─█")

    print("1-info")
    print("2-калькулитор")
    print("3-Выход")

    Menu = input()
    console.clear()



    if Menu == '1':

        print("███──█──█──███──████")
        print("─█───██─█──█────█──█")
        print("─█───█─██──███──█──█")
        print("─█───█──█──█────█──█")
        print("███──█──█──█────████")
        print("как работать с калькулитром.")
        print("число-Enter-действие-Enter-число-Enter-действие(Например=)-Enter-число.")
        print("калькулитор v-3.0")
        print("Python3")
        print("При создания калькулитра ни одна клавиатура не пострадала.")
        print("Сделанный Роменским Арсением 2017-2018©")

        input()


    if Menu == '2':

        print("Начали!")

# a-первое цифровое значение в которое после записываетса ответ вырожения
# p-Арефмитический знак. Например:+ - / * =
# b-Второе любое число.


        a = input()

        Cycle2 = 0
        while Cycle2 < 1:

            p = input()
            b = input()
            if p == '=':
                Cycle2 += 1
                print(a)

            if p == '-':
                a = int(a) - int(b)

            elif p == '+':
                a = int(a) + int(b)

            elif p == '*':
                a = int(a) * int(b)

            elif p == '/':

                if b != '0':

                    a = int(a) / int(b)

                if b == '0':

                    print ("Error STOP")
                    Cycle2 += 1
                    b = input()

                

    if Menu == '3':
        print("Вы уверены ?")
        print("Да-1                 Нет-2")
        e = input()
        if e == '1':
            Cycle += 1

        if e == '2':
            print("Ок")
            import time
            time.sleep(1)


    elif Menu > '3':

        print("Перезапуск")

        

        import time
        time.sleep(0.30)

        console.clear()

        print ("Ошибка")
