# Basics of HTTP/HTTPS

## HTTP vs HTTPS

**HTTP** (HyperText Transfer Protocol) is the foundation of data communication on the web.
It is an application-layer protocol that defines how messages are formatted and transmitted
between web browsers and servers.

**HTTPS** (HTTP Secure) is the encrypted version of HTTP. It uses **TLS/SSL** to encrypt
communication between client and server, ensuring:
- **Confidentiality**: data is encrypted and cannot be read by third parties
- **Integrity**: data cannot be altered in transit
- **Authentication**: the server identity is verified via certificates

## HTTP Methods

| Method   | Description                                      |
|----------|--------------------------------------------------|
| GET      | Retrieve data from the server (read-only)        |
| POST     | Send data to the server to create a resource     |
| PUT      | Update an existing resource (full replacement)   |
| PATCH    | Partially update an existing resource            |
| DELETE   | Delete a resource from the server                |
| HEAD     | Same as GET but returns only headers             |
| OPTIONS  | Describes the communication options for the URL  |

## Common HTTP Status Codes

| Code | Meaning                  | Description                                              |
|------|--------------------------|----------------------------------------------------------|
| 200  | OK                       | Request succeeded                                        |
| 201  | Created                  | Resource successfully created                            |
| 204  | No Content               | Request succeeded, no content to return                  |
| 301  | Moved Permanently        | Resource has been permanently moved to a new URL         |
| 400  | Bad Request              | The server could not understand the request              |
| 401  | Unauthorized             | Authentication is required                               |
| 403  | Forbidden                | The client does not have access rights                   |
| 404  | Not Found                | The server cannot find the requested resource            |
| 500  | Internal Server Error    | The server encountered an unexpected error               |

## How HTTP Works (Request/Response Cycle)

1. **Client** (browser/script) sends an HTTP **request** to the server
2. The request includes: method, URL, headers, and optionally a body
3. **Server** processes the request
4. **Server** sends back an HTTP **response** with: status code, headers, and optionally a body
5. **Client** processes the response

## HTTP Request Structure

```
GET /posts HTTP/1.1
Host: jsonplaceholder.typicode.com
Accept: application/json
```

## HTTP Response Structure

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 1234

[{"id": 1, "title": "..."}]
```
