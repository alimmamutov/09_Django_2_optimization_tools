# Django Framework. Инструменты оптимизации
## Мамутов Алим - Интернет магазин одежды
***
****Служебное****
***
*Для установки нужного venv:*
    
    pip install -r requirements.txt     
(requirements.txt лежит в корне проекта)

*Для выгрузки venv:*

    pip freeze > requirements.txt

*Для очистки venv:*

    pip uninstall -r requirements.txt

***Для передачи файлов по SSH***

*На сервер:*

      pscp -P 22 “C:\files or docs\filename” root@178.21.11.180:/home/django/09_Django_2_optimization_tools/

*С сервера:*

      pscp -P 22 root@178.21.11.180:/home/django/09_Django_2_optimization_tools/ C:\Users\Алим\Desktop\Geek\009_Django_Optim_Tools
***


**Урок 01 Отправка электронной почты. Контекстные процессоры**

1. Организовать выдачу сообщения об успешной отправке письма с кодом подтверждения в окне регистрации пользователя.
   
        Реализовано в том виде, в котором делали на уроке
   
2. Реализовать активацию пользователя при переходе по ссылке из письма.
   
        Реализовано в том виде, в котором делали на уроке
   
3. Создать контекстный процессор для корзины и скорректировать код контроллеров основного приложения.

        Реализовано в том виде, в котором делали на уроке

***

**Урок 2. Регистрация через социальную сеть. Django-ORM: связь один-к-одному**
1. Реализовать в проекте простой вариант аутентификации пользователя через социальную сеть VK+.
   
         Реализовано
2. Поработать со связью моделей «один-к-одному»: создать профиль пользователя и обеспечить возможность его редактирования.

         Реализовано
3. Реализовать автоматическое заполнение профиля пользователя при аутентификации через социальную сеть.

         Реализовано, но изменение анкеты происходит и не только в момент регистрации, но и при обычной авторизации уже
         сохораненного пользователя. пока оставлю как есть, но потом планирую исправить

4. Проверить работу исключения «AuthForbidden», например, задав при проверке минимальный возраст 100 лет.

            Прописал в сеттингсах:
            SOCIAL_AUTH_LOGIN_ERROR_URL = '/users/error/   SOCIAL_AUTH_RAISE_EXCEPTIONS = False
            Но работает только при отключенном режиме отладки


5. *Получить и сохранить язык из сети VK+.

         Реализовано

6. *Получить и сохранить foto из сети VK+.

         Реализовано
***

**Урок 3. Работа с заказом пользователя: CBV, Django formsets**

1. Создать выпадающее меню для ссылки на личный кабинет пользователя в меню. 
   
         Реализовано
   
2. Создать приложение для работы с заказами пользователя.
   
         Реализовано
   
3. Создать контроллеры CRUD для заказа на базе Django CBV.

         Реализовано

4. Реализовать обновление статуса заказа при совершении покупки.

         Реализовано
   
5. Обновить контроллеры проекта – перевести на Django CBV.
   
         Реализовано
   
6. *Организовать работу со статусом заказов в админке (имитация обработки заказа в магазине).
   
         Реализовано, но в очень утрированном варианте. (Статус можно поменять на странице заказа или в списке заказов)
         Саму функцию переключатель сделал методом объекта
***

**Урок 4. Работа с заказом пользователя: CBV, Django formsets**

1. Организовать работу с остатками товара в проекте (попробовать оба способа).


      Реализовано как на уроке

2. Реализовать обновление статистики заказа через jQuery.


      Реализовано как на уроке

3. Расширить функционал работы с формами при помощи «django-dynamic-formset».


      Реализовано как на уроке

4. Реализовать асинхронное обновление цены при добавлении нового продукта в заказ.


      Реализовано через аякс
      Возникшие проблемы:
         Проблема:         
            Заметил, что в форме создания заказа при добавлении строки возникает косяк с присвоением класса для поля price
            то есть по умолчанию для всех полей, которые относятся к модели OrderItem (такие как Product, Quantity),  
            name типа orderitems-ТекущийИндексСтроки-НазваниеПоля, но для поля price, тег span имеет класс с неверным
            индексом строки (индекс не наращивается).
         Решение:
            я увидел, что класс у тега span при формировании формы модели присваивается в шаблоне order_form, исходя из 
            номера итерации в цикле. но это не срабатывает при добавлении новой строки нашим методом jQuery.formset. 
            Что нужно исправить в шаблоне для обхода такогшо исключения, я так и не нарыл(
            Пришлось принудительно удалять класс и добавлять с правильным ай ди в коде JS (функция addOrderItem(row))
            Не знаю насколько это правильно, но как костыль, вродже работает)
         

***

**Урок 5. Развертывание Django-проекта на VPS от REG.RU**
1. Создать файл зависимостей «requirements.txt» для проекта.


      реализовано

2. Экспортировать данные из базы.


      реализовано

3. Установить и настроить сервер Ubuntu Server 17.


      реализовано

4. Развернуть проект на сервере.


      реализовано
      адрес - 178.21.11.180:80

Так как образ виртуальной машины достаточно большого размера, вместо него необходимо в архиве с ДЗ выслать скриншоты с выполненными шагами. Если на каком-то шаге начались проблемы – необходимо написать о них в файле «readme.txt». Если удастся развернуть проект на реальном хостинге – высылайте ссылку.


***

**Урок 6. Профилирование и нагрузочное тестирование проекта, оптимизация работы с базой данных**
1. Установить приложение «django-debug-toolbar». Оценить время загрузки страниц. Найти самые медленные контроллеры. Заполнить таблицу с количеством запросов и дубликатов на страницах проекта.



2. Визуализировать структуру моделей проекта при помощи «django_extensions», создать файл «geekshop_urls.txt» с URL-адресами проекта.



3. Установить утилиту «siege» и провести функциональное тестирование. Зафиксировать результаты в текстовом файле (какие контроллеры работали с ошибками).



4. Провести нагрузочное тестирование отдельных страниц и записать результаты в таблицу.



5. Провести тестирование в режиме интернета. Записать данные в таблицу. Определить условия, при которых начинаются отказы.



6. Провести оптимизацию работы с БД в проекте. Оценить эффект.



7. Визуализация таблиц субд


