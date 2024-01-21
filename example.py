import os
import vanna
from vanna.remote import VannaDefault


def main():
    api_key = vanna.get_api_key(os.environ.get("EMAIL"))

    vanna_model_name = "chinook"  # This is the name of the RAG model. This is typically associated with a specific dataset.
    vn = VannaDefault(model=vanna_model_name, api_key=api_key)
    vn.connect_to_sqlite("https://vanna.ai/Chinook.sqlite")
    vn.ask("What are the top 5 artists by sales?")


if __name__ == "__main__":
    main()
