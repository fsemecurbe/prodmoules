import duckdb
from fastapi import FastAPI

def init_db():
    conn = duckdb.connect(database="production_conchylicole.duckdb", read_only=False)
    conn.execute("CREATE TABLE IF NOT EXISTS conchyliculture (siret TEXT, commune TEXT, espece TEXT, tonnes DOUBLE)")
    conn.close()

init_db()

app = FastAPI(title="Production conchylicole", version="0.1")

@app.get("/")
def read_root():
    return {"message": "API production conchylicole v0.1"}

@app.post("/declarationProduction")
def create_producer(siret: str = "123456789", commune: str = "29019", espece: str = "Mytilus edulis", tonnes: float = 1000):
    conn = duckdb.connect(database="production_conchylicole.duckdb", read_only=False)
    query = f"INSERT INTO conchyliculture (siret, commune, espece, tonnes) VALUES (?, ?, ?, ?)"
    conn.execute(query, (siret, commune, espece, tonnes))
    conn.close()
    return {"message": f"Merci pour votre dépot de données siret : {siret}"}
