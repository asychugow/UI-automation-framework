# Automation Testing Project

Автотесты для веб-приложения и API с использованием Selenium и requests.

## Стек

- **Python** + **pytest**
- **Selenium WebDriver** — UI тесты
- **requests** — API тесты

## 📁 Структура

```
├── api/              # API клиенты
├── base/             # Базовые классы тестов
├── config/           # URL и данные
├── pages/            # Page Object
├── tests/
│   ├── UI/           # UI тесты
│   └── api/          # API тесты
├── conftest.py       # Фикстуры pytest
└── requirements.txt  # Зависимости
```

## Запуск

```bash
# Установить зависимости
pip install -r requirements.txt

# Запустить все тесты
pytest

# Только UI тесты
pytest tests/UI/

# Только API тесты
pytest tests/api/

# Выбранные тесты
pytest tests/UI/forms/test_login.py
```