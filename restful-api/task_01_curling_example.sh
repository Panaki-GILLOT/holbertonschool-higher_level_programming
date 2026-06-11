#!/bin/bash
# Consume data from a public API using curl

# Fetch all posts
echo "=== Fetching all posts ==="
curl -s https://jsonplaceholder.typicode.com/posts | python3 -c "
import sys, json
posts = json.load(sys.stdin)
for post in posts[:5]:
    print(f\"ID: {post['id']} - {post['title']}\")
print(f'Total posts: {len(posts)}')
"

# Fetch a single post
echo ""
echo "=== Fetching post #1 ==="
curl -s https://jsonplaceholder.typicode.com/posts/1 | python3 -m json.tool

# POST request - create a new post
echo ""
echo "=== Creating a new post ==="
curl -s -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "My New Post", "body": "This is the body.", "userId": 1}' \
  | python3 -m json.tool

# DELETE request
echo ""
echo "=== Deleting post #1 ==="
curl -s -X DELETE https://jsonplaceholder.typicode.com/posts/1
echo "Deleted successfully"
