![python veriosn](https://img.shields.io/badge/python-3.7%2B-blue)
![](https://img.shields.io/badge/test-task-red)

## Решение тестового задания на должность "Python-разработчки"

Целью тестового задания являлось разработка REST API для системы комментариев блога cо следующими API-методами:
* Добавление статьи или сущности, которую можно будет комментировать;
* Добавление комментария к статье;
* Добавление комментария на комментарий, с возможностью любой вложенности;
* Получение всех комментариев к статье вплоть до 3 уровня вложенности;
* Получение всех вложенных комментариев для комментария 3 уровня;
* По запросу получать древовидную структуру комментариев.

**Для решения данного задания использовался следующий стэк технологий**

* Django DRF
* Postgre SQL
* Docker

**Для запуска предоставленного решения на локальном ПК следуйте инструкциям ниже**

*Предварительно у вас должен быть установлен docker и docker-compose*


1. Перейдите в удобную для проекта папку и клонируйте данный репозиторий к себе на локальный ПК
   
   ```
   git clone https://github.com/acecrosser/kvartirka.git
   ```
2. Перейдите в созданную папку "kvartirka"
3. Установите общие права доступа на файл "entrypoint.sh"
   
   ```
   chmod 777 entrypoint.sh
   ```
4. Находясь в корне папки "kvartirka", запуститет сборку Docker-контейнера
   
   ```
   docker build .
   ```
5. Далее запустите сборку композиции контейнеров
   
   ```
   docker-compose build
   ```
6. Запустите docker-compose
   
   ```
   docker-compose up -b
   ```
7. При успешном запуске в консоле отобразится следующее:
   
   ```
   Creating network "kvartirka_default" with the default driver
   Creating kvartirka_db ... done
   Creating kvartirka_web ... done
   ```
8. Перейдите в браузере на страницу http://0.0.0.0:8000
9. Чтобы завершить презентацию реализации задания выполните следующию команду:
   
   ```
   docker-compose down -v
   ```
   
**Создание первого комментария к статье**

    
    {
        "email": "Указать почту",
        "text": "Текст комментария',
        "post": <id статьи или сущности которую комментируем>
        "parent": <id комментария который комментируем> 
        # Важно! Указывать у параметра "parent": <null> если это первый комментарий к сущности
    }
    

По возникшим вопросам пишите в телеграм [@acecrooser](https://t.me/acecrosser)
