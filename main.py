from pathlib import Path
import duckdb
from fastapi import FastAPI, HTTPException

DB_PATH = Path(__file__).parent / "prodmoules.duckdb"

app = FastAPI(title="Producteurs de moules", version="0.1")

def get_db():
    return duckdb.connect(database=str(DB_PATH), read_only=False)

def init_db():
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS producersIn (
            siret TEXT,
            commune TEXT,
            products TEXT,
            tonnes DOUBLE
        )
        """
    )
    conn.close()

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def read_root():
    return {"message": "API Producteurs de moules", "version": "0.1"}

@app.post("/producersin")
def create_producer(siret: str = "123456789", commune: str = "29019", products: str = "Moules de bouchot", tonnes: float = 1000.0):
    conn = get_db()
    conn.execute(
        'INSERT INTO producersIn (siret, commune, products, "values") VALUES (?, ?, ?, ?)',
        (
            siret,
            commune,
            products,
            tonnes,
        ),
    )
    conn.close()