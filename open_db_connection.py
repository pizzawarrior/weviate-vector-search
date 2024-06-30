import weaviate
import os
from dotenv import load_dotenv


load_dotenv()

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_API_KEY")),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_APIKEY"]  # Replace with your inference API key
    }
)
print(client.is_ready())
