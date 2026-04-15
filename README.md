# Conchylicoles

API FastAPI simple pour collecter et stocker des informations de production des produits conchylicoles en France.



## Installation

1. Créez un environnement Python :
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Démarrage

Lancez le serveur en développement :

```bash
uvicorn main:app --reload
```

Le service sera accessible sur `http://127.0.0.1:8000`.

## Endpoints

### GET /

Renvoie un message d’accueil.

**Exemple** :

```bash
curl http://127.0.0.1:8000/
```

### POST 

Ajoute un enregistrement de production conchylicole dans la base DuckDB.

Les paramètres sont envoyés en tant que paramètres de requête POST standard.

- `siret` : numéro SIRET du producteur
- `commune` : code INSEE de la commune
- `espece` : espèce (par exemple `Mytilus edulis`)
- `tonnes` : production en tonnes

**Exemple** :

```bash
curl -X POST "http://127.0.0.1:8000/producersin?siret=12345678901234&commune=29019&espece=Mytilus%20edulis&tonnes=1000.0"
```

## Base de données

Le fichier DuckDB utilisé est `production_conchylicole.duckdb`.

La table créée automatiquement est `conchyliculture` avec les colonnes :

- `siret`
- `commune`
- `espece`
- `tonnes`

## Tests rapides

1. Démarrez l’application.
2. Envoyez une requête POST.
3. Vérifiez la création du fichier `production_conchylicole.duckdb`.

## Notes

- Le schéma est créé automatiquement au démarrage.
- DuckDB persiste les données dans le fichier `.duckdb`.
