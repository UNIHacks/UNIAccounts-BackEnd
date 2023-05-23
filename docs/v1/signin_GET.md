## Check Acount *signIn*

<p class="route_text">
    <span class="method-GET">GET</span> <code>https://unica-accounts.com/api/v1/signin/</code>
</p>

<h2>
    Examples
</h2>

<p class="text_endpoint">
    &emsp; - Request
</p>

```yaml
in: AUTH
TOKEN: 'sklndansd548488a4dajndbkabdbasd'
```
```yaml
in: HEADERS
API_KEY: 'sklndansd548488a4dajndbkabdbasd'
```
**Notes:**<br>
- For Check Authentication is necessary ``jwt``
<br><br>

<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
  "message": "Valid Token",
  "user": {
    "_id": "",
    "account_number": "1",
    "careers": "Ingenieria en Computación",
    "email": "example@email.com",
    "exp": 1681877688,
    "half_year": 3,
    "last_name_fathers": "PÉREZ",
    "last_name_mothers": "ACOSTA",
    "name": "RUBEN RODRIGO",
    "nick_name": "ruber45",
    "password": "", ## Password void
    "role": "admin",
    "role_key": "sdasad4534junSD"
  }
}

```
```json
{
    "message": "Token Expired",
    "status_code": 200
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Invalid Token",
    "status_code": 401
}

```

<h2>
    Table Types
</h2>
<p class="text_endpoint">
    &emsp; - Request
</p>

| Section | Name    |           Description          |   Type |
| ------- | ------- |:------------------------------:| ------:|
| AUTH    | TOKEN   |      Password of New User      | String |
| HEADERS | API_KEY | API key provided by the system | String |
<p class="text_endpoint">
    &emsp; - Response
</p>

| Name        |     Description     |       Type |
| ----------- |:-------------------:| ----------:|
| message     | Message of Response |     String |
| user        |      User data      | JSON *[User]* |
| status_code |   Status Code HTTP  |    Integer |
