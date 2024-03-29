import os, sys
from vanna.openai.openai_chat import OpenAI_Chat
from vanna.chromadb.chromadb_vector import ChromaDB_VectorStore
from vanna.flask import VannaFlaskApp


class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)


def connect_vn():
    vn = MyVanna(
        config={
            "api_key": os.environ.get("OPENAI_ACCESS_TOKEN"),
            "model": "gpt-3.5-turbo-1106",
        }
    )

    vn.connect_to_sqlite("chinook.db")
    return vn


def train():
    print("******** Training...")
    vn = connect_vn()
    with open("chinook_structure.sql", "r") as f:
        sql = f.read()
        vn.train(ddl=sql)


def trainint_data():
    vn = connect_vn()
    training_data = vn.get_training_data()
    return training_data


def ask(question):
    print("******** Asking question: ", question)
    vn = connect_vn()
    return vn.ask(question=question)


def launch_ui():
    vn = connect_vn()
    app = VannaFlaskApp(vn)
    app.run()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("argument required. please specify [train|ask|training_data|ui].")
        sys.exit(1)

    if sys.argv[1] == "train":
        train()
    elif sys.argv[1] == "ask":
        print(ask(sys.argv[2]))
    elif sys.argv[1] == "training_data":
        print(trainint_data())
    elif sys.argv[1] == "ui":
        launch_ui()
    else:
        print("invalid argument. please specify [train|ask|training_data|ui].")
        sys.exit(1)
