from llama_index.core import SimpleDirectoryReader


documents = SimpleDirectoryReader("data/").load_data()
print(documents)
