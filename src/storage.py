from pymongo import MongoClient

def store_results(results, db_name="gene_db", collection_name="results"):
    """
    Store analysis results in MongoDB.
    
    Args:
        results (list): List of dictionaries containing results (e.g., gene importance, model metrics).
        db_name (str): Name of the MongoDB database.
        collection_name (str): Name of the MongoDB collection.
    """
    client = MongoClient("mongodb://mongodb:27017/")
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(results)
    client.close()
    print(f"Stored {len(results)} documents in {db_name}.{collection_name}.")

if __name__ == "__main__":
    sample_results = [
        {"gene": "TP53", "importance": 0.045, "model": "RandomForest"},
        {"gene": "BRCA1", "importance": 0.038, "model": "RandomForest"}
    ]
    store_results(sample_results)