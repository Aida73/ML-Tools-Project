from llama_index import StorageContext, load_index_from_storage
import os
import openai
from dotenv import load_dotenv
from unidecode import unidecode

# Load environment variables from .env file
load_dotenv()




def getEptInfos(question):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    # Rebuild storage context
    print(1)
    storage_context = StorageContext.from_defaults(persist_dir="ept_index")

    # Load index from the storage context
    print(2)
    new_index = load_index_from_storage(storage_context)
    print(3)
    new_query_engine = new_index.as_query_engine()
    print(4)
    try:
        response = new_query_engine.query(question)
        print(5)
        return unidecode(response.response).replace("\n", "")#encode().decode("unicode_escape")
    except Exception as e:
        print(f"An error occurred: {e}")
        return str(e)


