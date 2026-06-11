# RESTful API

## Description

This project covers the fundamentals of RESTful APIs using Python. It progresses from understanding HTTP/HTTPS basics, consuming APIs with command-line tools and Python, to building and securing APIs with Flask.

## Learning Objectives

- Understand the difference between HTTP and HTTPS
- Know the main HTTP methods and status codes
- Use `curl` to interact with REST APIs
- Use the `requests` library to consume APIs in Python
- Parse and manipulate JSON data
- Build a simple HTTP server using Python's `http.server` module
- Build a REST API with Flask
- Secure an API with Basic Auth and JWT

## Requirements

- Python 3.x
- `requests` library
- `flask`
- `flask-httpauth`
- `flask-jwt-extended`
- `werkzeug`

Install dependencies:

```bash
pip install requests flask flask-httpauth flask-jwt-extended
```

## Files

| File | Description |
|------|-------------|
| `task_00_http_https.md` | Basics of HTTP/HTTPS: methods, status codes, request/response cycle |
| `task_01_curling_example.sh` | Consuming a public API using `curl` from the command line |
| `task_02_requests.py` | Fetching and saving posts from JSONPlaceholder using Python `requests` |
| `task_03_http_server.py` | Simple HTTP server using Python's built-in `http.server` module |
| `task_04_rest_api.py` | REST API with Flask supporting CRUD operations on users |
| `task_05_basic_security.py` | Flask API secured with Basic Auth and JWT authentication |

## Usage

### Task 02 - Python Requests

```bash
python3 main_02_requests.py
```

Prints post titles and saves all posts to `posts.csv`.

### Task 03 - HTTP Server

```bash
python3 task_03_http_server.py
```

Available endpoints:
- `GET /` — welcome message
- `GET /data` — returns JSON data
- `GET /status` — returns "OK"
- `GET /info` — returns API version info

### Task 04 - Flask REST API

```bash
python3 task_04_rest_api.py
```

Available endpoints:
- `GET /` — welcome message
- `GET /status` — returns "OK"
- `GET /data` — returns list of usernames
- `GET /users/<username>` — returns a specific user
- `POST /add_user` — adds a new user (JSON body: `username`, `name`, `age`, `city`)

### Task 05 - Flask API Security

```bash
python3 task_05_basic_security.py
```

Available endpoints:
- `GET /basic-protected` — protected with Basic Auth (user1:password or admin1:password)
- `POST /login` — returns a JWT token (JSON body: `username`, `password`)
- `GET /jwt-protected` — protected with JWT
- `GET /admin-only` — protected with JWT, requires admin role

## Author

**panaki-gillot** - [Holberton School](https://www.holbertonschool.com/)
