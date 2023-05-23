# UNICA-ManagerAccounts-API
API to Manage UNICA System Accounts

## How run this project 
<br>

- **Create Env**
```bash
python -m venv env/local #env/local is the directory of your env
```

- **Activate Env**
```bash
#Linux bash/zsh
source venv/bin/activate

#Windows cmd
venv\Scripts\activate.bat

#Windows PowerShell
venv\Scripts\activate.ps1
```

- **Install Requeriments.txt *Local***

```bash
pip3 install -r requirements/local.txt
```

- **Init Flask Project**

    how to create migrations

    * **flask db init:** This command initializes the migrations directory in the project, creating a folder called migrations in the root of the project.

    * **flask db migrate:** This command detects changes to the models and generates a migration file in the migrations folder.

    * **flask db upgrade:** This command applies the pending migrations to the database schema, creating or updating the tables as necessary.

- **Run project locally**

    navigate to src path

    ```python
    flask run
    ```

    If you want to specify the port

    ```python
    flask run --port=NUMERO_PUERTO
    ```

    Run App on Debug Mode

    ```python
    flask run --port=NUMERO_PUERTO --debug
    ```

### **Endpoints Dev Status**
| Method |             Endpoint            | Status |
| ------ |:-------------------------------:| ------:|
| POST   |         /api/v1/signup/         |      ✓ |
| DELETE |         /api/v1/signup/         |      × |
| PUT    |         /api/v1/signin/         |      ✓ |
| GET    |         /api/v1/signin/         |      ✓ |
| POST   | /api/v1/signup-change-password/ |      × |
| PUT    | /api/v1/signup-change-password/ |      × |
