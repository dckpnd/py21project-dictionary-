### Цели и задачи
Нашей целью было создать удобную электронную версию словаря малого языка, обработав PDF-файл.  
Нужно было найти словарь редкого языка в PDF-файле, при этом такого языка, у которого еще не существовало достойного переводчика. Как оказалось, это не такая простая задача, потому что либо языки настолько малочисленные, что найти словарь в открытом доступе практически невозможно, либо языки достаточно крупные, и у них уже есть хорошие переводчики. Поэтому, когда мы случайно нашли словарь табасаранского языка, мы взяли его для работы.

После этого перед нами стояли следующие задачи:  
* распознать текст словаря с помощью ABBY FineReader, включая особые символы и диакритические знаки, почистить его регулярными выражениями.
* создать функции на питоне, которые могли бы работать со словарём и осуществлять поиск по табасаранскому слову, поиск по началу табасаранского слова и поиск по русскому слову
* сделать так, чтобы при поиске табасаранского слова не нужно было ставить ударение (в словаре везде, кроме односложных слов, проставлены ударения)
* сделать возможным поиск с опечатками
* создать сайт и вшить в него получившиеся функции  

В целом всё это получилось, кроме поиска с опечатками, и цели мы достигли. Однако мы столкнулись с некоторыми сложностями, связанными в основном с распознаванием текста словаря. Например, плохо получилось обработать переносы текста на следующую страницу.  

### Как работает программа 

* Текст словаря преобразуется в питоновский словарь: ключ - табасаранское слово, значение - все после. Статьи с одинаковыми словами (омонимы) собирается в один ключ, значения помечаются как 1., 2., ...
* Функция поиска по русскому слову запрашивает у пользователя слово, а потом, пробегаясь по значениям словаря и разделяя их по запятым и точкам с запятой, ищет точные и неточные совпадения слов в определении с запросом пользователя. Если такие находятся, то она сначала выводит точное совпадение, а потом все неточные (например, если человк искал слово *тонуть*, то сначала выведется статья для слова *тонуть*, а потом, под отдельным заголовком, статья для слова *утонуть*).  
* Функция поиска по табасаранскому слову также запрашивает у пользователя слово, а потом проверяет его наличие в ключах словаря и, если находит совпадение, выводит словарную статью.  
* Функция поиска по части слова пробегается по ключам словаря, проверяя, начинается ли ключ на то, что ввёл пользователь, и выводит словарные статьи для всех найденных совпадений.  

Сайт был создан с помощью модуля flask - так как это самый удобный фрэймворк на наш взгляд. Есть основнй файл `login.py`, в котором прописаны все разделы сайта, а также несколько вспомогательных питоновских файлов и несколько HTML-файлов с шаблонами страниц.  


### Что нужно установить
Для того чтобы программа работала, нужно установить на компьютер Python, а также модуль [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/).

```$ pip install Flask```

Затем скачать все файлы из репозитория (с расширениями .py и папку `templates` с .html), положив их в одну папку. Далее нужно запустить файл `login.py` и перейти по ссылке в выдаче.
