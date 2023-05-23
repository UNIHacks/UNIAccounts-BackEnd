## Login Acount *signIn*

<p class="route_text">
    <span class="method-PUT">PUT</span> <code>https://unica-accounts.com/api/v1/signin/</code>
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
    "account_number": "316259878",
}

```
**Notes:**<br>
- For Authentication, only one is necessary  ```nick_name | email | account_number```
<br><br>

<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
    "message": "Succesfull signIn",
    "status_code": 200,
    "jwt": "juasdhasdaj548456ad3ad64",
    "service_name": "UNICA_MANAGER_ACCOUNTS_API"
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error signIn",
    "status_code": 500
}

```
<p class="text_endpoint">
    &emsp; - Response 403 ERROR
</p>

```json
{
  "message": "Password Invalid",
  "status_code": 403
}
```
<h2>
    Table Types
</h2>
<p class="text_endpoint">
    &emsp; - Request
</p>

| Name           |         Description        |    Type |
| -------------- |:--------------------------:| -------:|
| nick_name      |      NickName of User      | *String |
| password       |    Password of New User    |  String |
| email          |      Email of New User     | *String |
| account_number | Number Account of New User | *String |

<p class="text_endpoint">
    &emsp; - Response
</p>

| Name         |     Description     |    Type |
| ------------ |:-------------------:| -------:|
| message      | Message of Response |  String |
| status_code  |   Status Code HTTP  | Integer |
| jwt          |    JSON Web Token   |  String |
| service_name |     Service Name    |  String |
