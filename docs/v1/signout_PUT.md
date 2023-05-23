## LogOut Acount *signOut*

<p class="route_text">
    <span class="method-PUT">PUT</span> <code>https://unica-accounts.com/api/v1/signout/</code>
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


<p class="text_endpoint">
    &emsp; - Response 200 OK
</p>

```json
{
  "message": "SignOut Successful",
  "status_code": 200
}

```

<p class="text_endpoint">
    &emsp; - Response 500 ERROR
</p>

```json
{
    "message": "Error signOut",
    "status_code": 500
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
| status_code |   Status Code HTTP  |    Integer |
