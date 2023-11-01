import requests
import weaviate
from weaviate.util import generate_uuid5
import json

if __name__ == "__main__":
    data_url = "https://embedded-lean-data.s3.ca-central-1.amazonaws.com/current_type_data_emb"
    class_name = "Types"
    batch_size = 1000
    client = weaviate.Client("http://weaviate:8080")
    if client.schema.exists(class_name):
        print(f"{class_name} class exists...")
        quit()
    else:
        print(f"Creating class {class_name}")
        client.schema.create_class({"class" : class_name})

    print(f"Populating {class_name} class...")

    client.batch.configure(batch_size=1000)

    response = requests.get(data_url, stream=True)

    counter = 0
    with client.batch as batch:
        for line in response.iter_lines():
            data_object = json.loads(line)
            vector = data_object.pop('embedding')
            batch.add_data_object(
                class_name = class_name,
                uuid = generate_uuid5(data_object['type']),
                data_object = data_object,
                vector = vector
            )
            counter += 1
            if counter % 1000 == 0:
                print(f"Processed {counter} entries so far...")
