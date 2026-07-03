# Employee Management Portal

A **console-based Employee Management System** built with Python and MySQL.  
No web framework. No GUI. Pure terminal application.

---

## Project Overview

This portal allows employees to log in, view their personal details, submit daily
wellness check-ins, and read company notifications and holidays.  
Admins can view all employee records, check health statuses, and post notifications.

---

## Features

| Module            | Description                                              |
|-------------------|----------------------------------------------------------|
| Login             | Role-based login for Admin and Employees                 |
| Employee Portal   | View personal details, wellness records, holidays, notifications |
| Wellness Mitra    | Daily health check-in with automatic Well/Unwell result  |
| Admin Dashboard   | View all employees, check health records                 |
| Notifications     | Read and post notifications (stored in `data/notif.txt`) |
| Holiday List      | View company holidays (stored in `data/list.txt`)        |

---

## Folder Structure

```
Employee-Portal/
│
├── main.py            ← Entry point — run this to start the app
├── config.py          ← All credentials and file paths
├── database.py        ← MySQL connection and query execution
├── auth.py            ← Login and credential validation
├── admin.py           ← Admin menus and operations
├── employee.py        ← Employee menus and wellness logic
├── file_manager.py    ← File read/write for notif.txt and list.txt
├── utils.py           ← Shared UI helpers (banner, separator, inputs)
│
├── requirements.txt   ← Python dependencies
├── database.sql       ← Database schema and sample data
├── .gitignore         ← Files excluded from Git
├── README.md          ← This file
│
└── data/
    ├── notif.txt      ← Company notifications
    └── list.txt       ← Holiday list
```

---

## Login Credentials

| Role       | ID    | Password |
|------------|-------|----------|
| Admin      | admin | adm34    |
| Employee 1 | Emp1  | meow123  |
| Employee 2 | Emp2  | nn123    |
| Employee 3 | Emp3  | jivi11   |
| Employee 4 | Emp4  | kanha22  |

---

## Requirements

- Python 3.x
- MySQL Server (running on localhost)
- mysql-connector-python

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Muskan-Vishwakarma22/Employee-portal.git
cd Employee-portal
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up the database
Open MySQL Workbench or MySQL CLI and run:
```sql
source database.sql
```
Or paste the contents of `database.sql` directly into your MySQL client.

### 4. Configure database credentials
Open `config.py` and update `DB_CONFIG` if your MySQL password differs:
```python
DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",
    "password": "your_password",   # ← change this
    "database": "muskanproject",
}
```

---

## Running the Project

```bash
python main.py
```

---

## Screenshots

> Add screenshots of the running application inside a `screenshots/` folder.

---

## Future Improvements

- Password hashing with `bcrypt` for secure credential storage
- Move credentials to a `.env` file using `python-dotenv`
- Allow admin to add/remove employees dynamically
- Export health reports to CSV
- Add date format validation for wellness entries
- Login attempt lockout after N failed tries
