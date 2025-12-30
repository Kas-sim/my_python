from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from sentence_transformers import SentenceTransformer

documents = SimpleDirectoryReader("data/").load_data()

node_parser = SentenceSplitter(
    chunk_size = 512,
    chunk_overlap = 64
)

nodes = node_parser.get_nodes_from_documents(
    documents,
    show_progress=True
)

texts = [node.text for node in nodes]
print(f"Total chunks created: {len(texts)}")

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(
    texts,
    batch_size=32,
    show_progress_bar=True
)
print("Embeddings Shape: ", embeddings.shape)


similarities = model.similarity(embeddings, embeddings)
print(similarities)

