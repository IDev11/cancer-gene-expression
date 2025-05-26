import unittest
from pyspark.sql import SparkSession
from src.ingestion import load_data

class TestIngestion(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder.appName("TestIngestion").getOrCreate()
        self.test_file = "/data/sample_data.csv"

    def test_load_data(self):
        df = load_data(self.test_file)
        self.assertIsNotNone(df)
        self.assertGreater(df.count(), 0)

    def tearDown(self):
        self.spark.stop()

if __name__ == "__main__":
    unittest.main()