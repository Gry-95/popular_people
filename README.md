### Автор
GitHub: https://github.com/gry-95
## Проект о популярных людях
### Описание:
Реализовано api, личный кабинет, форма добавления новых записей по категория и тэгам, 
### Запуск проекта:
- Клонировать репозиторий к себе на компьютер
```
git clone https://github.com/Gry-95/popular_people

python -m venv env
env/scripts/activate
python -m pip install --upgrade pip
```
- Установить все из requiremets.txt
```
pip install -r requirements.txt
```
- Сделать миграции
```
python manage.py migarte
```
- В корне проекта запустить сервер командой
```
python manage.py runserver
```
### Технологии:
* Python 3.12
* Django 5
* DjangoRestFramework 3.14
### О проекте:
- Добавление/удаление/редактирование новых записей
- Пагинация
- Api
- Регистрация
- Смена пароля
- Восстановление пароля (email message)
### В будушем:
- Настройка кэширования
- Деплой на сервер
