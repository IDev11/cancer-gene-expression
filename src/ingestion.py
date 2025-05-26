from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("GeneExpressionIngestion") \
    .getOrCreate()

def load_data(file_path):
    """
    Load TCGA RNA-Seq data into a Spark DataFrame.
    
    Args:
        file_path (str): Path to the CSV file containing gene expression data.
    
    Returns:
        DataFrame: Spark DataFrame with gene expression data.
    """
    data = spark.read.csv(file_path, header=True, inferSchema=True)
    return data

if __name__ == "__main__":
    data_path = "/data/tcga_breast_cancer_data.csv"
    df = load_data(data_path)
    df.show(5)
    print(f"Loaded {df.count()} rows with {len(df.columns)} columns.")