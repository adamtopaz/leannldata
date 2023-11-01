from fastapi import FastAPI
import weaviate
import openai
from pydantic import BaseModel
import json
import os

class Query(BaseModel):
    query: str
    results: int

openai.api_key = os.getenv("OPENAI_API_KEY")
client = weaviate.Client("http://weaviate:8080")

app = FastAPI()

@app.get("/")
def read_root(query : Query):
    vec = openai.Embedding.create(
        model="text-embedding-ada-002",
        input = query.query,
        encoding_format = "float")['data'][0]['embedding']
    results = (client.query
               .get("Types",["type","name","module"])
               .with_near_vector({"vector":vec})
               .with_limit(query.results)
               .with_additional(["distance"])
               .do()
               )
    return results['data']['Get']['Types']

