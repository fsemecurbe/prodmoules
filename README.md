# Conchylicoles

API FastAPI simple pour collecter et stocker des informations de production des produits conchylicoles en France.

Vous devez forker le repo puis lancer codespace.

## Installation

1. Créez un environnement Python et le configurer  :

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

## Démarrage

Lancez le serveur en développement :

```bash
uvicorn main:app --reload
```




Un nouvel onglet doit s'ouvrir, vous pouvez y aller et rajouter /docs pour obtenir le swagger




Ajoute un enregistrement de production conchylicole dans la base DuckDB.

Les paramètres sont envoyés en tant que paramètres de requête POST standard.

- `siret` : numéro SIRET du producteur
- `commune` : code INSEE de la commune
- `espece` : espèce (par exemple `Mytilus edulis`)
- `tonnes` : production en tonnes


## Base de données

Le fichier DuckDB utilisé est `production_conchylicole.duckdb`.

La table créée automatiquement est `conchyliculture` avec les colonnes :

- `siret`
- `commune`
- `espece`
- `tonnes`
- 
Vous accéder à la base de données avec le jupyter Lecture de la base


## Notes

- Le schéma est créé automatiquement au démarrage.
- DuckDB persiste les données dans le fichier `.duckdb`.
