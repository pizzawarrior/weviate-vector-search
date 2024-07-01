import weaviate
import os
from dotenv import load_dotenv


load_dotenv()

URL = os.getenv("WCD_URL")
APIKEY = os.getenv("WCD_API_KEY")

client = weaviate.connect_to_wcs(
    cluster_url=URL,
    auth_credentials=weaviate.auth.AuthApiKey(APIKEY),
)

print(client.is_ready())

# questions = client.collections.get("Question")
# print(questions)
