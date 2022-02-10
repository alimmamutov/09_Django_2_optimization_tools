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
***
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