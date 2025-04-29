# CodeLeap Backend Engineering Test

This is a repository created to participate in CodeLeap's Junior Backend selection process.

## Requirements

Base url endpoint: "/careers/"

Required methods: POST, GET, PATCH, DELETE

CExpected behaviors::
    - POST with JSON:
```json
    {
        "username": "string",
        "title": "string",
        "content": "string"
    }
```
    - GET response:
```json
{
    "id": "number",
    "username": "string",
    "created_datetime": "datetime",
    "title": "string",
    "content": "string"
}
```
    - PATCH it must not allow changes to: id, username, created_datetime


**Assumed** behaviors:
    - No mention of the PUT method — assumed to be not allowed
    - No specification or requirement for a database — sqlite was used
    - No requirement for a user interface — all responses are returned in JSON


## Running with Docker
When running via Docker, the entrypoint will automatically execute the tests.
```bash
docker compose up --build
```
