import os

import google.generativeai as genai
from dotenv import load_dotenv
from pinecone import Pinecone, QueryResponse, ServerlessSpec

# ---------------------------
# 1. CONFIGURAÇÃO
# ---------------------------
load_dotenv()

GEMINI_APIKEY = os.getenv("GEMINI_API_KEY")
PINECONE_APIKEY = os.getenv("PINECONE_API_KEY")

# Configure Gemini API key compatibly (avoids "configure" export/type issues)
if GEMINI_APIKEY:
    os.environ["GOOGLE_API_KEY"] = GEMINI_APIKEY
    _configure = getattr(genai, "configure", None)
    if callable(_configure):
        _configure(api_key=GEMINI_APIKEY)

# Fix: use the correct variable name for Pinecone API key
pc = Pinecone(api_key=PINECONE_APIKEY)

INDEX_NAME = "exemplo-embeddings"

# ---------------------------
# 2. FUNÇÃO PARA GERAR EMBEDDINGS (GEMINI)
# ---------------------------
def gerar_embedding(texto: str):
    response = genai.embed_content(
        model="text-embedding-004",
        content=texto
    )
    return response["embedding"]

# ---------------------------
# 3. CRIAR ÍNDICE NO PINECONE (DIMENSÃO DINÂMICA)
# ---------------------------

# Obtém a dimensão do embedding do modelo Gemini dinamicamente
_dim = len(gerar_embedding("Inicializando índice"))

# cria índice apenas se não existir, com dimensão compatível
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=_dim,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(INDEX_NAME)

# ---------------------------
# 4. ARMAZENAR DOCUMENTOS NO PINECONE
# ---------------------------

documentos = {
    "doc1": "Carros precisam de manutenção preventiva.",
    "doc2": "Python é uma ótima linguagem para IA.",
    "doc3": "Trocar o óleo regularmente aumenta a vida útil do motor.",
}

vetores = []

for doc_id, conteudo in documentos.items():
    vec = gerar_embedding(conteudo)
    vetores.append({
        "id": doc_id,
        "values": vec,
        "metadata": {"texto": conteudo}
    })

index.upsert(vectors=vetores)
print("Documentos armazenados no Pinecone!")

# ---------------------------
# 5. CONSULTA POR SIMILARIDADE
# ---------------------------

def buscar_similaridade(consulta: str, k: int = 3) -> QueryResponse:
    embedding_consulta = gerar_embedding(consulta)
    
    resultado = index.query(
        vector=embedding_consulta,
        top_k=k,
        include_metadata=True
    )
    return resultado  # pyright: ignore[reportReturnType]

# ---------------------------
# 6. TESTANDO CONSULTA
# ---------------------------

consulta = "Como fazer manutenção em um motor?"
resultado = buscar_similaridade(consulta)

print("\nResultados da busca:\n")
for match in resultado.matches:
    print(f"ID: {match.id} — Score: {match.score:.4f}")
    print(f"Texto: {match.metadata['texto']}\n")
