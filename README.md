# Django application

---
## 🏠 Homework

Homework related actions.

### ▶️ Run

Make all actions needed for run homework from zero.

```shell
make d-homework-i-run
```

### 🚮 Purge

Make all actions needed for delete homework.

```shell
make d-homework-i-purge
```

---

## 🛠️ Dev

### Initialize dev

Install dependencies and register pre-commit.

```shell
make init-dev
```

---

## 🐳 Docker

Use services in dockers.

### ▶️ Run

Just run

```shell
make d-run
```

### ⏹️Stop

Stop services

```shell
make d-stop
```

### 🚮 Purge

Purge all data related with services

```shell
make d-purge
```

## 🗄 DataBase
```shell
make d-run-i-local-dev
```
### 🧳Make migration
```shell
make migrations
```
### 🛫Migrate
```shell
make migrate
```
***
## 🐳SuperUser
### 🔩Create
```shell
make init-dev-i-create-superuser
```
### 🗑️Delete
```shell
make init-dev-i-delete-superuser
```
***