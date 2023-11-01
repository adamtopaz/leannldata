# Requirements

- An openai api key, set as an environment variable called `OPENAI_API_KEY`.
- Docker and Docker Compose.

# Usage

Clone the repo, and naviate to the root directory. 
Then run the following command:

```bash
docker-compose up -d --build
```

This will spin up the following containers:
- A container with a vector database (we use `weaviate` for this).
- A container called `manager` which will populate the database in the background.
- A container caled `api` which will serve the API, using the `FastAPI` python package. 

Populating the database may take some time, but you should still be able to use the API while it is populating.

Example usage:
```bash
curl localhost:8000 \
  -X GET \
  -H "Content-Type: application/json" \ 
  -d '{"query": "If $G$ is a finite group of order $n$ and $g$ is an element of $G$, then $g^n = 1$", "results" : 10}'
```
The above will return the 10 most relevant results for the query, as an array of JSON objects.