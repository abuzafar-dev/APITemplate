# API Template

Django REST Framework asosidagi oddiy API shablon. Kategoriya va mahsulotlar uchun CRUD, qidiruv, saralash, pagination va Swagger hujjati bor.

## Ishga tushirish

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Endpointlar

| Method | URL | Vazifasi |
|---|---|---|
| GET, POST | `/api/categories/` | kategoriyalar |
| GET, PUT, PATCH, DELETE | `/api/categories/<id>/` | bitta kategoriya |
| GET, POST | `/api/products/` | mahsulotlar |
| GET, PUT, PATCH, DELETE | `/api/products/<id>/` | bitta mahsulot |

Filtrlar: `?category=1`, `?search=iphone`, `?ordering=-price`

Swagger: http://127.0.0.1:8000/api/docs/

## Testlar

```bash
python manage.py test
```
