import dotenv
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI()

def create_embedding(text):
    response = client.embeddings.create(
        model='text-embedding-3-small',
        input=text,
    )

    return response.data[0].embedding