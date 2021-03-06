# Проект 1. Игра: Угадай число. PYTHON-8. Финальное задание

## Оглавление  
[1. Описание проекта](https://github.com/alexskymax/sf_data_science/blob/main/project_0/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/alexskymax/sf_data_science/blob/main/project_0/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/alexskymax/sf_data_science/blob/main/project_0/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/alexskymax/sf_data_science/blob/main/project_0/README.md#Этапы-работы-над-проектом)  
[5. Результаты](https://github.com/alexskymax/sf_data_science/blob/main/project_0/README.md#Результаты)    
[6. Выводы](https://github.com/alexskymax/sf_data_science/blob/main/project_0/README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное количество попыток.

:arrow_up:[к оглавлению](https://github.com/alexskymax/sf_data_science/blob/main/project_0/README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python

:arrow_up:[к оглавлению](https://github.com/alexskymax/sf_data_science/blob/main/project_0/README.md#Оглавление)

### Краткая информация о данных

В данном проекте отсутствуют данные для обработки.
  
:arrow_up:[к оглавлению](https://github.com/alexskymax/sf_data_science/blob/main/project_0/README.md#Оглавление)


### Этапы работы над проектом  

Проект состоит из двух частей, в первой реализуем функцию угадывания чисел от 1 до 100, во второй части создаём функцию, которая подсчитывает среднее значение n-количества попыток за которое удалось угадать число. 

Создаём функцию random_predict, которая будет угадывать значение аргумента. В качестве аргумента задаем по умолчанию целое число 1.

* Создаём переменную-счётчик count, в качестве значения указываем количество попыток, за которое удалось угадать число.

* Создаём переменную predict, в которую будем генерировать значение для сравнения с загаданным числом. Диапазон для генератора случайных чисел задаём переменными min_range и max_range, которым присваиваем значения 1 и 101 соответственно.

* Далее создаём бесконечный цикл.

    * "Включаем" счётчик count.

    * В цикле мы сравниваем нашу переменную predict с заданным в качестве аргумента функции числом, и если оно меньше присваиваем это значение переменной min_range, если больше - max_range плюс 1, и запускаем генератор случайных чисел для переменной predict заново.

    * Если значения predict и number равны, завершаем цикл.

* Возвращаем значение count.

Во второй части проекта создаём функцию score_game для подсчёта среднего значения количества попыток, за которое удалось угадать загаданное число из 1000 повторений.

* Создаём пустой список count_ls, куда будем складывать значения count из 1000 повторений.

* Создаём переменную random_array, в качестве значения используем генератор случайных чисел в диапазоне от 1 до 100.

* Далее создаём цикл, который будет перебирать значения из переменной random_array и подставлять их в качестве аргумента функции random_predict, результаты функции заносятся в список count_ls.

* Возвращаем переменную score, в которую заносим среднее значение количества попыток из списка count_ls.

Выводим строку с результатом среднего значения количества попыток, за которое удалось угадать число из 1000 повторений.


:arrow_up:[к оглавлению](https://github.com/alexskymax/sf_data_science/blob/main/project_0/README.md#Оглавление)


### Результаты:  

Разработанная программа позволяет угадывать числа в диапазоне от 1 до 100, в среднем за 9 попыток.

:arrow_up:[к оглавлению](https://github.com/alexskymax/sf_data_science/blob/main/project_0/README.md#Оглавление)


### Выводы:  

Данное решение полностью отвечает требованиям финального задания блока PYTHON-8. 

:arrow_up:[к оглавлению](https://github.com/alexskymax/sf_data_science/blob/main/project_0/README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами