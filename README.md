# Employees REST API (Flask + PostgreSQL)

Overview
--------

Small example REST API built with Flask and SQLAlchemy to manage employees.

Requirements
------------

- Python 3.10+
- PostgreSQL (or use any DB supported by SQLAlchemy)
- Recommended Python packages (see `requirements.txt`):
  - Flask
  - Flask-SQLAlchemy
  - python-dotenv
  - psycopg2-binary

Quickstart
----------

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
# or: .venv\Scripts\activate    # cmd
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create a PostgreSQL database and user (example):

```sql
CREATE DATABASE testdb2;
-- ensure connection string matches DATABASE_URL in .env
```

4. Create a `.env` file or export environment variables:

```
DATABASE_URL=postgresql://postgres:postgres@localhost/testdb2
SECRET_KEY=your-secret-key
FLASK_ENV=development
```

Run (development)
-----------------

Create tables and run the app locally:

```powershell
# from project root
python app.py
```

API Endpoints
-------------

- GET /employees — list all employees
- GET /employees/<id> — get single employee
- POST /employees — create employee (JSON body: `name`, optional `position`, `salary`)
- PUT /employees/<id> — update employee (JSON fields to change)
- DELETE /employees/<id> — delete employee
- PATCH /employees/<id> - partial update (JSON fields to change)

Example curl (create):

```bash
curl -X POST http://127.0.0.1:5000/employees \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","position":"Engineer","salary":75000}'
```
Example curl (partial update):
```bash
curl -X PATCH http://127.0.0.1:5000/employees/1 \
  -H "Content-Type: application/json" \
  -d '{"position":"Senior Engineer","salary":82000}'
```
Notes
-----

- The project currently uses a minimal configuration file `config.py` to read `DATABASE_URL` and `SECRET_KEY` from the environment. For production, use a strong `SECRET_KEY` and secure DB credentials.
- Consider adding `Flask-Migrate` for proper migrations rather than `db.create_all()`.
- Add input validation and authentication before using in production.

Where to look
-------------

- Main app: `app.py`
- Configuration: `config.py`
- Requirements: `requirements.txt`

License
-------

For learning/demo purposes.

Step-by-step (beginner)
-----------------------

Follow these one-by-one. Tell me when each is done.

1. Create a virtual environment in the project root.
2. Activate the virtual environment.
3. Add `Flask`, `Flask-SQLAlchemy`, `python-dotenv`, `psycopg2-binary` to `requirements.txt`.
4. Install dependencies with `pip install -r requirements.txt`.
5. Create a `.env` with `DATABASE_URL=postgresql://<user>:<pass>@localhost/testdb2` and `SECRET_KEY`.
6. Update `config.py` to read `SQLALCHEMY_DATABASE_URI` from `DATABASE_URL` and set `SQLALCHEMY_TRACK_MODIFICATIONS = False`.
7. In `app.py` import `jsonify` and initialize `db = SQLAlchemy(app)` after `app.config.from_object('config.Config')`.
8. Add an `Employee` model with `id, name, position, salary` and `to_dict()`.
9. Implement REST endpoints: `GET /employees`, `GET /employees/<id>`, `POST /employees`, `PUT /employees/<id>`, `PATCH /employees/<id>`, `DELETE /employees/<id>`.
10. For `POST` parse JSON, create `Employee`, `db.session.add()` and `db.session.commit()`, return `jsonify(...), 201`.
11. For `PUT` replace fields; for `PATCH` update only provided fields.
12. For single `GET` use `Employee.query.get_or_404(id)` and return JSON.
13. For `DELETE` remove and return 204.
14. Add `if __name__ == '__main__': db.create_all(); app.run(debug=True)` for local dev.
15. Test endpoints with `curl` or Postman.
16. Optionally add `Flask-Migrate` and create migrations.
17. Add input validation and error handling (return 400 on bad input).
18. Add tests using `pytest` and Flask test client.
