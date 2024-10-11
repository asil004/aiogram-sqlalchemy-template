# aiogram-and-sqlalchemy-template

A simple bot template of using aiogram 3.x + async sqlalchemy 2.0+.

Used tech:

* [aiogram 3.x](https://github.com/aiogram/aiogram)
* [SQLAlchemy 2.0+](https://www.sqlalchemy.org/)
* PostgreSQL as database
* psycopg3 as database driver for SQLAlchemy
* Docker with docker-compose for deployment

## Quick Start Guide

### Setting Up Locally

#### 1. Repository Initialization

- **Clone the Repository**

#### 2. Environment Setup

- **Create a Virtual Environment**:
  ```bash
  python3.11 -m venv .venv
  ```
- **Activate the Virtual Environment**:
  ```bash
  source .venv/bin/activate
  ```

#### 3. Configuration

- **Environment Variables**:
    - Copy the example environment file:
      ```bash
      cp .env.example .env
      ```
    - _Note: The API can operate without this step, but configuring the environment variables is recommended for full
      functionality._

#### 4. Dependency Management

- **Install Dependencies**:
  ```bash
  pip install -r requirements.txt
  ```

#### 5.0 Update ```bot/db/__init__.py```

- Just add the new model an ```__init__```.py file

#### 5. Database Setup

- **Run Migrations**:
  ```bash
  make migrate
  ```

#### 6. Launching the bot

- **Start the bot**:
  ```bash
  make run.bot
  ```

##

### Setting Up with Docker

#### 1. Repository Initialization

- **Clone the Repository**

#### 2. Configuration

- Follow the steps in the top 👆 to set up the `.env` file.

#### 3. Docker Compose

- **Run Docker Compose**:
  ```bash
  docker compose up -d
  ```

### --------------------------------------------------------------------------------------

# aiogram-va-sqlalchemy-telegram bot-shabloni

aiogram 3.x + async sqlalchemy 2.0+ bot shabloni.

Foydalanilgan texnologiyalar:

* [aiogram 3.x](https://github.com/aiogram/aiogram)
* [SQLAlchemy 2.0+](https://www.sqlalchemy.org/)
* Ma'lumotlar ombori sifatida PostgreSQL
* SQLAlchemy uchun ma'lumotlar bilan ishlash psycopg3
* Deploy qilish uchun Docker va docker-compose

## Tezkor Boshlash Qo'llanma

### O'rnatish

#### 1. Repositorni ko'chirib oling

- **Repositoriyani klonlang**

#### 2. Muhitni O'rnatish

- **Virtual muhit yaratish**:
  ```bash
  python3.11 -m venv .venv
  ```
- **Virtual muhitni faollashtirish**:
  ```bash
  source .venv/bin/activate
  ```

#### 3. Sozlash

- **Muhit o'zgaruvchilari**:
    - Misol muhit faylini nusxalash:
      ```bash
      cp .env.example .env
      ```
    - _Izoh: API bu qadam yo'q, lekin muhit o'zgaruvchilarini sozlash to'liq funksionallik uchun maslahat beriladi._

#### 4. Kutubxonalarni o'rnatib olish

- **Kutubxonalarni o'rnatish**:
  ```bash
  pip install -r requirements.txt
  ```

#### 5. Ma'lumotlar omborini sozlash

- **Migratsiyalarni ishga tushirish**:
  ```bash
  make migrate
  ```

#### 6. Botni ishga tushirish

- **Botga run berish**:
  ```bash
  make run.bot
  ```

##

### Docker bilan O'rnatish

#### 1. Repositorni klonlash

- **Repositoriyani klonlang**

#### 2. Sozlash

- `.env` faylini sozlash uchun yuqoridagi qadamlarni o'rganib chiqing.

#### 3. Docker Compose

- **Docker Compose ni ishga tushiring**:
  ```bash
  docker compose up -d
  ```