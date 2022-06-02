### Цели и задачи
Нашей целью было создать удобную электронную версию словаря малого языка, обработав PDF-файл.  
Нужно было найти словарь редкого языка в PDF-файле, при этом такого языка, у которого еще не существовало достойного переводчика. Как оказалось, это не такая простая задача, потому что либо языки настолько малочисленные, что найти словарь в открытом доступе практически невозможно, либо языки достаточно крупные, и у них уже есть хорошие переводчики. Поэтому, когда мы случайно нашли словарь табасаранского языка, мы взяли его для работы.

После этого перед нами стояли следующие задачи:  
* распознать текст словаря с помощью (*какой-то программы*), включая особые символы и диакритические знаки, почистить его регулярками
* создать функции на питоне, которые могли бы работать со словарём и осуществлять поиск по табасаранскому слову, поиск по началу табасаранского слова и поиск по русскому слову
* сделать так, чтобы при поиске табасаранского слова не нужно было ставить ударение (в словаре везде, кроме односложных слов, проставлены ударения)
* сделать возможным поиск с опечатками
* создать сайт и вшить в него получившиеся функции  
В целом всё это получилось, кроме поиска с опечатками, и цели мы достигли. Однако мы столкнулись с некоторыми сложностями, связанными в основном с распознаванием текста словаря. Например, плохо получилось обработать переносы текста на следующую страницу.  

### Как работает программа
Словарь был обработан с помощью регулярных выражений: 

Функция поиска по русскому слову запрашивает у пользователя слово, а потом, пробегаясь по значениям словаря и разделяя их по запятым и точкам с запятой, ищет точные и неточные совпадения слов в определении с запросом пользователя. Если такие находятся, то она сначала выводит точное совпадение, а потом все неточные (например, если человк искал слово *тонуть*, то сначала выведется статья для слова *тонуть*, а потом, под отдельным заголовком, статья для слова *утонуть*).  
Функция поиска по табасаранскому слову также запрашивает у пользователя слово, а потом проверяет его наличие в ключах словаря и, если находит совпадение, выводит словарную статью.  
Функция поиска по части слова пробегается по ключам словаря, проверяя, начинается ли ключ на то, что ввёл пользователь, и выводит словарные статьи для всех найденных совпадений.  

Сайт был создан с помощью модуля flask - его нам посоветовал наш куратор. Есть основнй файл login.py, в котором прописаны все разделы сайта, а также несколько вспомогательных питоновских файлов и несколько HTML-файлов с шаблонами страниц.  


### Что нужно установить
Для того чтобы программа работала, нужно установить на компьютер Python, а также модуль Flask. Затем скачать все файлы из репозитория (с расширениями .py и .html, а также текст словаря и два изображения), положив их в одну папку. При этом все HTML-файлы нужно положить во вложенную папку с названием templates. Далее нужно запустить файл login.py и перейти по ссылке в выдаче.
