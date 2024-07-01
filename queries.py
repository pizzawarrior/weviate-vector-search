from dotenv import load_dotenv
import weaviate.classes as wvc
from open_db_connection import client
from data.query_vector import query_vector


load_dotenv()

try:
    client.connect()
    questions = client.collections.get("Question")

    response = questions.query.near_vector(
        near_vector=query_vector,
        limit=2,
        return_metadata=wvc.query.MetadataQuery(certainty=True)
    )

    # print(response)
    for o in response.objects:
        print(f"Question: {o.properties['question']}")
        print(f"Answer: {o.properties['answer']}")

finally:
    client.close()  # Close client gracefully
