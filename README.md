# Технічне завдання для Maklai

Для перевірки роботи програми треба у віртуальному середовищі проєкту встановити 
Flask і запустити командою `python main.py`. Також перед запуском варто переконатись, 
що модуль itertools встановлений у віртуальному середовищі (він входить у пакет базових
модулів, але краще пересвідчитись).

## Робота програми

Вся програма складається із двох файлів: `main.py` та `tools.py`. 
Перший виконує роль основної, в ньому запускається сервер на Flask, який слухає localhost 
на порту 8000. При переході по шляху `/paraphrase` запускається єдиний ендпоінт.
Далі з аргументів GET запиту отримуємо дерево у string формі, ліміт (default = 20) і
ноди, які підлягають комбінаціям (default = ['NP']).
Після цього викликаються 3 функції, прописані у модулі `tools.py`.

Модуль `tools.py` містить у собі 3 функції — `find_key_nodes`, `generate_combinations` 
та `generate_trees`. 
Ці функції працюють відповідним чином:
1. `find_key_nodes` використовує дві вкладені функції: `in_depth` та `check_node`. Перша 
використовується для занурення у глибину, і виконується рекурсивно, друга перевіряє поточний 
вузол на задовільність умові.
2. `generate_combinations` генерує всі можливі комбінації й перестановки на основі знайдених
нод. Для реалізації цього використовуються функції `permutations` та `product` з бібліотеки `itertools`.
3. `generate_trees` проходить по всіх згенерованих комбінаціях розміщення нод та генерує словник 
зі string формою дерева.

В кінцевому результаті при виконанні, наприклад, запиту наданого у технічному завданні, а саме `localhost:8000/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )` буде повернуто JSON з усіма можливими комбінаціями цього речення за заданими умовами.