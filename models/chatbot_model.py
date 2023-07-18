from llama_index import StorageContext, load_index_from_storage
import os
import sys
import openai
from dotenv import load_dotenv
from unidecode import unidecode

# Add the parent directory of the current file to the module search path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


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
        return unidecode(response.response).replace("\n", "")
    except Exception as e:
        print(f"An error occurred: {e}")
        texte = "Il semble y avoir un probeme, veuillez réessayer plutard. Si le probleme persiste, veuillez contacter le service technique à l'adresse suivante: tech@ept.sn"
        return unidecode(texte)


