# Hero API Test Project

Тестовый Python-проект для работы с API супергероев.

Проект:

* загружает данные о героях,
* сохраняет их в JSON,
* ищет самого высокого героя по:

    * полу (`Male` / `Female`)
    * наличию работы (`True` / `False`)
* запускает автотесты через `pytest`.

---

## Структура проекта

```text
src/
    api.py
    heroes.py

tests/
    test_heroes.py

tests/data/
    full.json
    sample.json
    loaded.json
    answer.json

start.py
requirements.txt
```

---

## Установка проекта

### 1. Клонировать репозиторий

```bash
git clone https://github.com/incomagia/test-hero_api.git
```

---

### 2. Перейти в папку проекта

```bash
cd test-hero_api
```

---

### 3. Создать виртуальное окружение

```bash
python -m venv .venv
```

---

### 4. Активировать окружение

#### Windows CMD

```bash
.venv\Scripts\activate
```

#### PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

---

### 5. Установить зависимости

```bash
pip install -r requirements.txt
```

---

## Запуск проекта

```bash
python start.py
```

---

## Что делает start.py

* запускает поиск героя,
* выводит результат в консоль,
* сохраняет результат в:

    * `tests/data/answer.json`
* запускает автотесты `pytest`.

---

## Запуск тестов отдельно

Обычный запуск:

```bash
pytest
```

Подробный вывод:

```bash
pytest -v
```

---

## Используемые технологии

* Python 3
* pytest
* requests
* JSON
