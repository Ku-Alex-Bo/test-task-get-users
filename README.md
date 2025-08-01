# 📝 Тестовое задание на позицию Python Junior Developer

## 📦 Стек

- `beautifulsoup4` — Извлечение данных из HTML
- `requests` — Работа с HTTP-запросами
- `dynaconf` — Динамическая конфигурация
- `tabulate` — Вывод табличных данных в консоль
- `pydantic` — Типизация моделей
- `isort`, `black`, `flake8` — Стиль и форматирование кода

## 🚀 Запуск:

1. **Клонируйте репозиторий:**

```bash
git clone https://github.com/Ku-Alex-Bo/test-task-get-users/
cd test-task-get-users/
```

2. **Создайте виртальное окружение:**
```bash
setup-venv
```
Для активации:
- *Windows*
```bash
venv\Scripts\activate
```
- *Mac/Linux*
```bash
source venv/bin/activate
```

3. **Установите зависимости:**
```bash
make install
```
Для установки всех зависимостей (включая dev):
```bash
make install-dev
```

5. **Создайте .env файл на основе .env.example:**
```bash
make setup-env
```

5. **Запустите скрипт:**
```bash
make run
```

## Реализация:
Приложение app разделено на три основных модуля:
- `client.py` Класс Client для работы с HTTP-запросами
- `parser.py` Класс Parser для извлечения данных из HTML
- `worker.py` Функция run_worker работающая по алгоритму:
  1. Получаем токен и сессию
  2. Получаем ссылку на бд
  3. Получаем ссылку на таблицу
  4. Извлекаем данные из таблицы
  5. Выводим в консоль, как требуется по заданию
