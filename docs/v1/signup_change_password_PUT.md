## Request Change Password of Acount *signUp*

Change Password of Acount

<p class="route_text">
    <span class="method-PUT">PUT</span> <code>https://unica-accounts.com/api/v1/signup-change-password/</code>
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
    "new_password": "newPassword12*"
}

```

<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
    "message": "Succesfull Change Password of Acount",
    "status_code": 200
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error Change Password of Acount",
    "status_code": 500
}

```

<h2>
    Table Types
</h2>
<p class="text_endpoint">
    &emsp; - Request
</p>

| Name         |       Description       |   Type |
| ------------ |:-----------------------:| ------:|
| nick_name    | NickName of User signUp | String |
| new_password | New Password of Account | String |


<p class="text_endpoint">
    &emsp; - Response
</p>

| Name        |     Description     |    Type |
| ----------- |:-------------------:| -------:|
| message     | Message of Response |  String |
| status_code |   Status Code HTTP  | Integer |
