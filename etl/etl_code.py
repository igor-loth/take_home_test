import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, weekofyear, count, sum as spark_sum
from pyspark.sql.window import Window
import pyspark.sql.functions as F

# Config do Spark
class SparkETL:
    def __init__(self, dataset_path):
        self.spark = SparkSession.builder \
            .appName("taxi_trips_ETL") \
            .getOrCreate()
        self.dataset_path = dataset_path

    # Carrega todos os arquivos JSON que estão na pasta dataset
    def load_data(self):
        return self.spark.read.json(f"{self.dataset_path}/*.json")


    # Processamento das transformações conforme requisitos
    def transform(self, df):

        # Extrai ano e semana da data de pickup
        df = df.withColumn("year", year(col("pickup_datetime"))) \
               .withColumn("week", weekofyear(col("pickup_datetime")))

        ## Vendor que mais viajou por ano, utilizando o critério de desempate
        vendor_trips = df.groupBy("vendor_id", "year") \
            .agg(count("*").alias("trip_count"), spark_sum("trip_distance").alias("total_distance"))

        # Critério de desempate: quem percorreu o maior percurso, ordem alfabética dos nomes
        window_spec = Window.partitionBy("year").orderBy(col("trip_count").desc(), col("total_distance").desc(), col("vendor_id").asc())
        top_vendors = vendor_trips.withColumn("rank", F.rank().over(window_spec)).filter(col("rank") == 1)

        ## Semana com mais viagens por ano
        week_trips = df.groupBy("year", "week").agg(count("*").alias("weekly_trip_count"))
        max_week = week_trips.withColumn("max_week", F.rank().over(Window.partitionBy("year").orderBy(col("weekly_trip_count").desc()))).filter(col("max_week") == 1)

        ## Quantas viagens o vendor com mais viagens fez na semana mais movimentada do ano
        result = max_week.join(top_vendors, "year").join(df, ["year", "week", "vendor_id"]) \
                         .groupBy("year", "vendor_id", "week").agg(count("*").alias("vendor_weekly_trips"))

        return result

    # Exporta o DataFrame para CSV
    def export(self, df, output_path):
        df.coalesce(1).write.option("header", "true").option("sep", ",").csv(output_path, mode="overwrite")


# Execução do processo ETL
if __name__ == "__main__":
    etl = SparkETL(dataset_path="/home/igorloth/take_home_test/etl/code/dataset")
    
    # Carregamento e processamento dos dados
    df = etl.load_data()
    result = etl.transform(df)
    
    # Exportando os resultados
    etl.export(result, "/home/igorloth/take_home_test/etl/code/output/")
