### Описание:

Учебный проект по изучению написания API для сайта сообщений.

Просмотр публикаций, сообществ и комментариев доступен для всех пользователей.
Добавление, изменение и удаление, а также доступ к подпискам, доступны только для зарегистрированных пользователей,
получивших токен.

Проект поддерживает создание jwt-токенов для аутентификации.

### Установка и запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AleksandrPU/api_final_yatube.git
```

```
cd api_final_yatube
```

Создать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов к API:

Получить список доступных endpoints:

```
/api/v1/
```

Пример ответа:

```json
{
    "posts": "http://api.example.org/api/v1/posts/",
    "groups": "http://api.example.org/api/v1/groups/",
    "follow": "http://api.example.org/api/v1/follow/"
}
```
Получение списка публикаций:

```
/api/v1/posts/
```

При запросе публикаций поддерживается пагинация:

```
/api/v1/posts/?offset=5&limit=10
```

Пример ответа:

```
{
  "count": 123,
  "next": "http://api.example.org/posts/?offset=400&limit=100",
  "previous": "http://api.example.org/posts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2001-01-01T01:00:00Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

Для создания и редактирования необходимо зарегистрироваться и получить токен:

```
/api/v1/jwt/create/
```
Тело запроса application/json:

```json
{
  "username": "string",
  "password": "string"
}
```

Создание публикации:

Добавление новой публикации в коллекцию публикаций.

Тело запроса application/json:

```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Пример ответа:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2001-01-01T01:00:00Z",
  "image": "string",
  "group": 0
}
```