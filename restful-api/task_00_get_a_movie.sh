#!/bin/bash
# Fetch a movie from the OMDb-like public API using curl
curl -s "https://api.tvmaze.com/search/shows?q=breaking+bad" | python3 -m json.tool
