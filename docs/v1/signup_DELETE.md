## Detele Acount *signUp*

<p class="route_text">
    <span class="method-DELETE">DELETE</span> <code>https://unica-accounts.com/api/v1/signup/</code>
</p>

<h2>
    Examples
</h2>

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
    "message": "Succesfull Delete Account",
    "status_code": 200
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error to Delete",
    "status_code": 500
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

| Name        |     Description     |    Type |
| ----------- |:-------------------:| -------:|
| message     | Message of Response |  String |
| status_code |   Status Code HTTP  | Integer |
