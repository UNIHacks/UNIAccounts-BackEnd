## Create Acount *signUp*

<p class="route_text">
    <span class="method-POST">POST</span> <code>https://unica-accounts.com/api/v1/signup/</code>
</p>

<h2>
    Examples
</h2>

```yaml
in: HEADERS
API_KEY: 'sklndansd548488a4dajndbkabdbasd'
```

<p class="text_endpoint">
    &emsp; - Request
</p>

```json
{
    "nick_name": "UserExample",
    "password": "passwordExample34*",
    "email": "example@email.com",
    "name": "Ruben Rodrigo",
    "last_name_fathers": "Pérez",
    "last_name_mothers": "Acosta",
    "account_number": "316259878",
    "careers": "Ingenieria en Computación",
    "role": "admin",
    "role_key": "sdasad4534junSD",
    "half_year": 4
}

```

<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
    "message": "Succesfull signUp",
    "status_code": 200
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error signUp",
    "status_code": 500
}

```
<p class="text_endpoint">
    &emsp; - Response 428 ERROR
</p>

```json
{
  "message": "Error nick_name in use",
  "status_code": 428
}
```
<h2>
    Table Types
</h2>
<p class="text_endpoint">
    &emsp; - Request
</p>

| Name              |             Description            |     Type |
| ----------------- |:----------------------------------:| --------:|
| nick_name         |       NickName of User signUp      |   String |
| password          |        Password of New User        |   String |
| email             |          Email of New User         |  *String |
| name              |          Name of New User          |   String |
| last_name_fathers |        Last Name of New User       |   String |
| last_name_mothers |        Last Name of New User       |   String |
| account_number    |     Number Account of New User     |   String |
| careers           |         Careers of New User        |   String |
| half_year         |          Half Year 1 to N          | *Integer |
| role              |          Role of New User          |   String |


<p class="text_endpoint">
    &emsp; - Response
</p>

| Name        |     Description     |    Type |
| ----------- |:-------------------:| -------:|
| message     | Message of Response |  String |
| status_code |   Status Code HTTP  | Integer |
