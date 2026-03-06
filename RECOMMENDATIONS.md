# Рекомендации по расширению тестового покрытия

## 📊 Текущее состояние проекта

| Категория | Файлов тестов | Покрытие |
|-----------|---------------|----------|
| **UI тесты** | 5 | Формы + элементы |
| **API тесты** | 2 | Users + Health |

### Существующие тесты

**UI:**
- `tests/UI/forms/test_login.py` — валидный/невалидный логин
- `tests/UI/forms/test_register.py` — регистрация
- `tests/UI/forms/test_inputs.py` — поля ввода
- `tests/UI/elements/test_dropdown.py` — выпадающие списки
- `tests/UI/elements/test_checkboxes.py` — чекбоксы

**API:**
- `tests/api/test_users.py` — register, login, profile
- `tests/api/test_health_api.py` — health check

---

## 🎯 Приоритетный список новых тестов

### 1. File Upload / File Download ⭐⭐⭐

**Страницы:** `/upload`, `/download`, `/secure-download`

**Почему важно:**
- Загрузка файлов — распространённый кейс в реальных проектах
- Скачивание файлов и валидация содержимого
- Secure download с авторизацией (связка login + download)

**Что тестировать:**
```python
# test_upload.py
- Загрузка .txt файла
- Загрузка .png/.jpg изображения
- Попытка загрузки без выбора файла
- Загрузка файла с большим размером

# test_download.py
- Скачивание файла и проверка имени
- Скачивание файла и проверка содержимого
- Secure download (требуется авторизация)
```

**Selenium API:** `send_keys()` для input[type=file]

---

### 2. JavaScript Dialogs (Alerts) ⭐⭐⭐

**Страница:** `/javascript_dialogs`

**Почему важно:**
- Работа с Selenium Alert API
- Три типа диалогов: alert, confirm, prompt

**Что тестировать:**
```python
# test_alerts.py
- alert(): принятие алерта, проверка текста
- confirm(): нажатие OK
- confirm(): нажатие Cancel
- prompt(): ввод текста и подтверждение
- prompt(): отмена
- dismiss() vs accept()
```

**Selenium API:** `driver.switch_to.alert`

---

### 3. Drag and Drop ⭐⭐⭐

**Страницы:** `/drag_and_drop`, `/drag_and_drop_circles`

**Почему важно:**
- ActionChains в Selenium
- Перетаскивание элементов — частый кейс в UI

**Что тестировать:**
```python
# test_drag_and_drop.py
- Перетаскивание колонки A в колонку B
- Перетаскивание кругов (colored circles)
- Валидация результата (текст "A" в колонке B)
- Drag and drop с offset
```

**Selenium API:** `ActionChains.drag_and_drop()`, `click_and_hold()`

---

### 4. Radio Buttons ⭐⭐

**Страница:** `/radio_buttons`

**Почему важно:**
- Выбор одного значения из группы
- Отличие от чекбоксов (multiple choice vs single choice)

**Что тестировать:**
```python
# test_radio_buttons.py
- Выбор опции по value
- Выбор опции по label
- Проверка, что выбрана только одна опция
- Изменение выбора (с одной опции на другую)
- Проверка состояния selected
```

---

### 5. Dynamic Content / Controls ⭐⭐

**Страницы:** `/dynamic_content`, `/dynamic_controls`, `/dynamic_loading`

**Почему важно:**
- Ожидание появления/исчезновения элементов
- Работа со spinner/loading
- Enable/disable элементов управления

**Что тестировать:**
```python
# test_dynamic_content.py
- Проверка изменения контента после обновления
- Ожидание появления текста

# test_dynamic_controls.py
- Enable/disable checkbox с задержкой
- Ожидание кнопки после enable
- Spinner/loading индикатор

# test_dynamic_loading.py
- Ожидание контента после клика на Start
- Проверка spinner исчезновения
```

**Selenium API:** `WebDriverWait`, `expected_conditions`

---

### 6. Broken Images ⭐⭐

**Страница:** `/broken_images`

**Почему важно:**
- Проверка битых изображений
- Работа с атрибутами img
- Валидация alt-текста

**Что тестировать:**
```python
# test_broken_images.py
- Обнаружение битых изображений (через JS)
- Проверка наличия alt-текста
- Валидация HTTP статуса изображения
- Проверка иконки "broken" для битых картинок
```

**Selenium API:** `execute_script` для проверки naturalWidth

---

### 7. Hovers + Tooltips ⭐

**Страницы:** `/hovers`, `/tooltips`

**Почему важно:**
- ActionChains move_to_element
- Проверка всплывающих подсказок

**Что тестировать:**
```python
# test_hovers.py
- Наведение на figure, проверка подписи
- Проверка появления link "View profile"

# test_tooltips.py
- Наведение на элемент, проверка tooltip текста
- Проверка исчезновения tooltip после ухода курсора
```

**Selenium API:** `ActionChains.move_to_element()`

---

### 8. Multiple Windows / Iframes ⭐

**Страницы:** `/multiple_windows`, `/iframe`

**Почему важно:**
- Переключение между окнами (window_handles)
- Работа с iframe (switch_to.frame)

**Что тестировать:**
```python
# test_multiple_windows.py
- Клик на ссылку, открытие нового окна
- Переключение на новое окно (switch_to.window)
- Проверка контента в новом окне
- Закрытие нового окна, возврат к исходному

# test_iframe.py
- Переключение на iframe по id/name/index
- Взаимодействие с элементами внутри iframe
- Возврат к основному документу (switch_to.default_content)
- Вложенные iframe
```

**Selenium API:** `driver.window_handles`, `driver.switch_to.window()`, `driver.switch_to.frame()`

---

### 9. HTTP Status Codes ⭐

**Страница:** `/status_codes`

**Почему важно:**
- Проверка 200, 301, 404, 500
- Обработка редиректов

**Что тестировать:**
```python
# test_status_codes.py
- Клик на ссылку 200 — проверка успешной загрузки
- Клик на ссылку 301 — проверка редиректа
- Клик на ссылку 404 — проверка страницы Not Found
- Клик на ссылку 500 — проверка Server Error
```

---

### 10. Forgot Password Form ⭐

**Страница:** `/forgot_password`

**Почему важно:**
- Восстановление пароля — критичный user flow
- Валидация email формата

**Что тестировать:**
```python
# test_forgot_password.py
- Ввод валидного email — проверка сообщения об отправке
- Ввод несуществующего email
- Ввод невалидного формата email
- Пустое поле email
```

---

## 📦 API тесты (расширение)

**Base URL:** `https://practice.expandtesting.com/notes/api`

### Существующие тесты
```
✅ POST /users/register
✅ POST /users/login  
✅ GET /users/profile
✅ GET /health-check
```

### Отсутствующие тесты

#### Notes CRUD (Notes App API)
```python
# test_notes.py
❌ POST /notes — создание заметки
❌ GET /notes — список всех заметок
❌ GET /notes/{id} — получение заметки по ID
❌ PUT /notes/{id} — обновление заметки
❌ DELETE /notes/{id} — удаление заметки
```

#### Profile Management
```python
# test_profile.py
❌ PUT /users/profile — обновление профиля (name, email)
❌ DELETE /users/profile — удаление аккаунта
```

#### Негативные сценарии
```python
# test_users_negative.py
❌ POST /users/register с пустыми полями (400)
❌ POST /users/register с коротким паролем (400)
❌ POST /users/login с несуществующим email (401)
❌ POST /users/login с пустым password (400)
❌ GET /users/profile без токена (401)
❌ GET /users/profile с невалидным токеном (401)
```

---

## 🗂️ Рекомендуемая структура проекта

```
tests/
├── UI/
│   ├── forms/
│   │   ├── test_login.py              ✅
│   │   ├── test_register.py           ✅
│   │   └── test_forgot_password.py    ❌ НОВОЕ
│   ├── elements/
│   │   ├── test_dropdown.py           ✅
│   │   ├── test_checkboxes.py         ✅
│   │   ├── test_radio_buttons.py      ❌ НОВОЕ
│   │   └── test_sliders.py            ❌ НОВОЕ
│   ├── files/
│   │   ├── test_upload.py             ❌ НОВОЕ
│   │   └── test_download.py           ❌ НОВОЕ
│   ├── dialogs/
│   │   └── test_alerts.py             ❌ НОВОЕ
│   ├── drag_drop/
│   │   └── test_drag_and_drop.py      ❌ НОВОЕ
│   ├── windows/
│   │   ├── test_iframes.py            ❌ НОВОЕ
│   │   └── test_multiple_windows.py   ❌ НОВОЕ
│   ├── dynamic/
│   │   ├── test_dynamic_content.py    ❌ НОВОЕ
│   │   ├── test_dynamic_controls.py   ❌ НОВОЕ
│   │   └── test_dynamic_loading.py    ❌ НОВОЕ
│   ├── images/
│   │   └── test_broken_images.py      ❌ НОВОЕ
│   ├── navigation/
│   │   ├── test_hovers.py             ❌ НОВОЕ
│   │   ├── test_tooltips.py           ❌ НОВОЕ
│   │   └── test_status_codes.py       ❌ НОВОЕ
│   └── frames/
│       └── test_iframes.py            ❌ НОВОЕ
│
└── api/
    ├── test_users.py                  ✅
    ├── test_health.py                 ✅
    ├── test_notes.py                  ❌ НОВОЕ
    ├── test_profile.py                ❌ НОВОЕ
    └── test_users_negative.py         ❌ НОВОЕ
```

---

## 🔧 Архитектурные улучшения

### 1. Убрать time.sleep()

**Проблема:**
```python
# Сейчас в тестах:
time.sleep(2)  # Ждём 2 секунды
```

**Решение:**
```python
# Заменить на явные ожидания:
self.wait.until(EC.visibility_of_element_located(locator))
```

### 2. Добавить Allure-аннотации

```python
import allure

@allure.feature("Login")
@allure.story("Авторизация пользователя")
class TestLoginPage(BaseTest):
    
    @allure.title("Успешный вход в систему")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self):
        ...
```

### 3. Скриншоты при падении тестов

**conftest.py:**
```python
import pytest
import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == 'call' and report.failed:
        if hasattr(item.cls, 'driver'):
            driver = item.cls.driver
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            screenshot_path = f"screenshots/{item.name}_{timestamp}.png"
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot(screenshot_path)
```

### 4. Вынести данные в .env

**.env:**
```env
LOGIN=practice
PASSWORD=SuperSecretPassword!
BASE_URL=https://practice.expandtesting.com
API_BASE_URL=https://practice.expandtesting.com/notes/api
```

**config/data.py:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

class Data:
    LOGIN = os.getenv("LOGIN", "practice")
    PASSWORD = os.getenv("PASSWORD", "SuperSecretPassword!")
```

### 5. Исправить опечатки в кодах

**pages/inputs_page.py:**
```python
# Было:
NUMBER_OTPUT_FIELD  # опечатка
TEXT_OTPUT_FIELD
PASSWORD_OTPUT_FIELD

# Стало:
NUMBER_OUTPUT_FIELD
TEXT_OUTPUT_FIELD
PASSWORD_OUTPUT_FIELD
```

**pages/host_page.py:**
```python
# Было:
TEST_REGITER_PAGE_LINK  # опечатка

# Стало:
TEST_REGISTER_PAGE_LINK
```

---

## 📋 План внедрения

| Приоритет | Тест | Оценка времени | Сложность |
|-----------|------|----------------|-----------|
| 🔴 HIGH | File Upload | 30 мин | ⭐ |
| 🔴 HIGH | JavaScript Alerts | 30 мин | ⭐ |
| 🔴 HIGH | API Notes CRUD | 45 мин | ⭐⭐ |
| 🟡 MEDIUM | Radio Buttons | 20 мин | ⭐ |
| 🟡 MEDIUM | Drag and Drop | 45 мин | ⭐⭐ |
| 🟡 MEDIUM | Dynamic Controls | 40 мин | ⭐⭐ |
| 🟡 MEDIUM | Broken Images | 30 мин | ⭐⭐ |
| 🟢 LOW | Hovers + Tooltips | 30 мин | ⭐ |
| 🟢 LOW | Multiple Windows | 30 мин | ⭐⭐ |
| 🟢 LOW | Iframes | 30 мин | ⭐⭐ |
| 🟢 LOW | HTTP Status Codes | 20 мин | ⭐ |
| 🟢 LOW | Forgot Password | 30 мин | ⭐ |

---

## 🚀 Быстрый старт

**Рекомендуемый порядок реализации:**

1. **File Upload** — простой тест, высокая ценность
2. **JavaScript Alerts** — отработка Alert API
3. **Radio Buttons** — быстрое добавление
4. **API Notes CRUD** — расширение API покрытия
5. **Drag and Drop** — отработка ActionChains
6. **Dynamic Controls** — отработка WebDriverWait
7. **Остальные** — по мере необходимости

---

## 📚 Полезные ссылки

- [Selenium WebDriver Docs](https://www.selenium.dev/documentation/)
- [Expand Testing Practice](https://practice.expandtesting.com/)
- [Pytest Fixtures](https://docs.pytest.org/en/latest/explanation/fixtures.html)
- [Allure Pytest](https://allurereport.org/docs/pytest/)
