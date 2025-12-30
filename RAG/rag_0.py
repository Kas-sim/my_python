import chromadb
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from chromadb.utils import embedding_functions
from llama_index.core import VectorStoreIndex

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



embeddings = model.encode(
    texts,
    batch_size=32,
    show_progress_bar=True
)
print("Embeddings Shape: ", embeddings.shape)

similarities = model.similarity(embeddings, embeddings)
print(similarities)

client = chromadb.Client()

embeddings = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.create_collection(
    name="rag_docs",
    embedding_function=embeddings
)

index = VectorStoreIndex(
    nodes,
    vector_store=collection,
    embed_model=embeddings
)


