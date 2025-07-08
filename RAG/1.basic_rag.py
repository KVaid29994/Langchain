import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir,"GEN_AI.pdf")
# print (file_path)

persistent_directory = os.path.join(current_dir, "db", "chroma_db")

if not os.path.exists(persistent_directory):
    print("Persistent directory does not exist. Initializing vector store...")

 # Ensure the text file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please check the path."
        )
    

loader = PyPDFLoader(file_path)
pages = []
for page in loader.load():
    pages.append(page)

text_splitter =CharacterTextSplitter(chunk_size = 100, chunk_overlap = 50)
docs = text_splitter.split_documents(pages)
print (docs[1])


# Display information about the split documents
print("\n--- Document Chunks Information ---")
print(f"Number of document chunks: {len(docs)}")


 # Create embeddings
print("\n--- Creating embeddings ---")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
if os.path.exists(persistent_directory):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma(persist_directory=persistent_directory, embedding_function = embeddings)
else:
    db = Chroma.from_documents(docs, embedding=embeddings, persist_directory=persistent_directory)

print("\n--- Finished creating vector store ---")

query = "what is the first question"

docs = db.similarity_search(query)
print (docs)