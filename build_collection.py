import weaviate.classes as wvc
from open_db_connection import client

# Create the collection. Weaviate's autoschema feature will infer properties when importing.
questions = client.collections.create(
    "Question",
    vectorizer_config=wvc.config.Configure.Vectorizer.none(),
)
