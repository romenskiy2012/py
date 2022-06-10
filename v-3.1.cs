int Cycle = 0, Menu;
while (Cycle < 1){
    Console.Clear();
    Console.WriteLine("█──█─████───██─█────█──█─█─█───██─█──█─███─████─████");
    Console.WriteLine("█─█──█──█──█─█─█────█─█──█─█──█─█─█──█──█──█──█─█──█");
    Console.WriteLine("██───████─█──█─████─██───███─█──█─█─██──█──█──█─████");
    Console.WriteLine("█─█──█──█─█──█─█──█─█─█────█─█──█─██─█──█──█──█─█");
    Console.WriteLine("█──█─█──█─█──█─████─█──█─███─█──█─█──█──█──████─█");

    Console.WriteLine("1-info");
    Console.WriteLine("2-калькулитор");
    Console.WriteLine("3-Выход");

    Menu = Int32.Parse(Console.ReadLine());
    Console.Clear();



    if (Menu == 1){

        Console.WriteLine("███──█──█──███──████");
        Console.WriteLine("─█───██─█──█────█──█");
        Console.WriteLine("─█───█─██──███──█──█");
        Console.WriteLine("─█───█──█──█────█──█");
        Console.WriteLine("███──█──█──█────████");
        Console.WriteLine("как работать с калькулитром.");
        Console.WriteLine("число-Enter-действие-Enter-число-Enter-действие(Например=)-Enter-число.");
        Console.WriteLine("калькулитор v-3.0");
        Console.WriteLine("Python3");
        Console.WriteLine("При создания калькулитра ни одна клавиатура не пострадала.");
        Console.WriteLine("Сделанный Роменским Арсением 2017-2022©");

        Console.ReadLine();
    }

    else if (Menu == 2){

        Console.WriteLine("Начали!");

// a-первое цифровое значение в которое после записываетса ответ вырожения
// p-Арефмитический знак. Например:+ - / * =
// b-Второе любое число.

        int a, b;
        string p;
        a = Int32.Parse(Console.ReadLine());

        int Cycle2 = 0;
        while (Cycle2 < 1){

            p = Console.ReadLine();

            if (p == "="){
                Console.WriteLine(a);
                Console.ReadLine();
                break;
            }
            else b = Int32.Parse(Console.ReadLine());
            if (p == "-"){
                a = a - b;
            }
            else if (p == "+"){
                a = a + b;
            }
            else if (p == "*"){
                a = a * b;
            }
            else if (p == "/"){

                if (b != 0){

                    a = a / b;
                }
                if (b == 0){

                    Console.WriteLine("Error STOP");
                    Cycle2++;
                    b = Int32.Parse(Console.ReadLine());
                }
            }
        }

    }


    else if (Menu == 3){
        Console.WriteLine("Вы уверены ?");
        Console.WriteLine("Да-1                 Нет-2");
        int e = Int32.Parse(Console.ReadLine());
        if (e == 1) Cycle++;

        if (e == 2) Console.WriteLine("Ok");
    }

    else{
        Console.WriteLine("Перезапуск");

        Console.Clear();

        Console.WriteLine("Ошибка");
    }
}


/*


Console.WriteLine("Hello, World!");
int A = 41;
string Q = "41";
bool SS = true;
double SSAS = 1.2;

int soud(){
  Console.Write("SSSSSSSSS\n");
  return 0;
}
Q = Console.ReadLine();
Console.WriteLine($"Вы написали: {Q}");
//Q = ridline("SAS: ");
Console.WriteLine($"Число: {A} и дробное: {SSAS}\nА теперь сложить: {A+SSAS}");

Console.WriteLine(A == 41);
Console.WriteLine(SS);
Console.Write("SSSSSSSSS\n");
for (A = 9; A != 0; A--){
  Console.Write(A + "\n");
}


if (A != 1){
  Console.WriteLine("\nSUS");
}
else if (A == 1) Console.WriteLine("1111");

else Console.WriteLine("SAS");


soud();
*/
