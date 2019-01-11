# Veronica
Данный репрозиторий содержит демо-версию проекта для бронирования столиков в кафе или ресторане через сообщения в группе vk. 
Весь проект написан на python с помощью vk_api.

# Структура репозитория

```
+--action_for_user.py                 Здесь прописаны основные варианты поведения программы, при общении с пользователем
+--add_table.py                       Здесь прописаны функции, при помощи которых можно получить данные из базы данных
+--config.py/                         Здесь хранится api-токен
+--create_data_base.py/               Этот файл создавался для заполнения таблиц базы данных
+--create_key_board.py/               В этом файле содержатся функции, с помощью которых генерировался json объект, который преобразовывался в клавиатуру для пользователя
+--server.py/                         Основной файл, в котором написаны функции для получения сообщения и дальнейших действий
+--server_manager.py/                 Исполняемый файл, который создает экземпляр объекта сервера
+--test_data_base/                    Основная база данных, в которой хранятся таблицы с заказами, столиками и типами столиков
```

# Структура бронирования
Для начала пользователю нужно зайти в группу ресторана или кафе и написать сообщение в группу. Сразу же появится приветственное сообщение, и бот предложит пользователю выбрать, на сколько человек он хочет забронировать столик.

![alt text](https://pp.userapi.com/c850432/v850432492/899c6/opL0JisWqbI.jpg)

После выбора количества человек, пользователю предложат выбрать тип столика, который его интересует. Вся информация о столиках и их типах
берется из базы данных

![alt text](https://pp.userapi.com/c849420/v849420480/100b27/GxbZIeAKVws.jpg)

Далее предлагается выбрать дату и время заказа

![alt text](https://pp.userapi.com/c850432/v850432492/899b8/-d0MXDYM1ro.jpg)

![alt text](https://pp.userapi.com/c850432/v850432492/899b0/C5LSCDpgxTQ.jpg)

и в конце бот просит пользователя ввести информацию о себе для подтверждения заказа.

![alt text](https://pp.userapi.com/c850432/v850432492/899a8/1DWOD26JCWo.jpg)

Вся информация о заказе, id пользователя харнится в базе данных, в таблице с заказами

![alt text](https://pp.userapi.com/c850432/v850432492/89999/euoQog9DhXw.jpg)

Информация о заказе также поступает менеджеру в личные сообщения, после чего он может подтвердить или отклонить заявку

# Принцип работы
Исполняемым файлом является server_manager.py. В нем создается экземпляр класса server и начинает выполнение функция, 
которая работает по принципу Long Poll API. Как только пришло новое сообщение в группу, проверяется писал ли пользователь раннее
и предлагает ему выбрать столик на какое-то количество человек. После выбора кол-ва человек, в базе данных проверяется таблица
со столиками и если есть свободные столики, то они выводятся пользователю. Далее пользователь выбирает дату и время заказа, которая 
хранится в таблице с заказами. Более подробное описание кода представлено в комментариях к коду.
