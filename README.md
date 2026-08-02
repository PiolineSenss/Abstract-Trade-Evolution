# Abstract Trade

Платформа для генерации, коллекционирования и торговли математическими фракталами в виде NFT.

## Как это работает

Сервер на Flask генерирует уникальные фракталы из случайных математических формул (аналоги множества Мандельброта с вариациями). Каждый фрактал — визуально неповторимая абстракция с уникальной палитрой цветов. Пользователь подключает Ethereum-кошелёк (Sign-In with Ethereum), получает доступ к своим фракталам и может выставлять их на маркетплейс для покупки/продажи за внутренний баланс.

## Стек

- **Backend:** Flask, SQLAlchemy (SQLite)
- **Frontend:** Jinja2 шаблоны
- **Auth:** Sign-In with Ethereum (eth-account + JWT)
- **Math:** NumPy, Matplotlib, mpmath (высокоточная арифметика для фракталов)
- **CORS:** flask-cors

## Запуск

```bash
pip install -r requirements.txt
python main.py
```

Приложение поднимется на `http://localhost:8000`.

## API

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| POST | `/auth/nonce` | Получить nonce для подписи |
| POST | `/auth/login` | Вход через Ethereum-подпись |
| POST | `/auth/logout` | Выход |
| GET | `/auth/me` | Текущий пользователь |
| GET | `/auth/balance` | Баланс |
| POST | `/auth/add-balance` | Пополнить баланс |
| POST | `/fractal/generate` | Сгенерировать фрактал |
| GET | `/fractal/my-fractals` | Мои фракталы |
| GET | `/fractal/fractal/<id>` | Получить фрактал |
| PUT | `/fractal/fractal/<id>/name` | Переименовать фрактал |
| POST | `/marketplace/list` | Выставить на продажу |
| DELETE | `/marketplace/unlist/<id>` | Снять с продажи |
| GET | `/marketplace/listings` | Все активные листинги |
| POST | `/marketplace/buy/<id>` | Купить фрактал |
| GET | `/marketplace/my-listings` | Мои листинги |

## Структура проекта

```
├── main.py              # Flask-приложение, маршруты страниц
├── models.py            # Модели: User, Fractal, Listing
├── requirements.txt     # Зависимости
├── routers/
│   ├── auth.py          # Аутентификация (Ethereum SIWE + JWT)
│   ├── fractal.py       # Генерация и управление фракталами
│   └── marketplace.py   # Маркетплейс (листинги, покупки)
└── templates/           # HTML-шаблоны
```

## Лицензия

MIT
