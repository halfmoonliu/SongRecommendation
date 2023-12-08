from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

def load(dataset="dbfs:/FileStore/Final/songs.csv"):
    spark = SparkSession.builder.appName("Read CSV").getOrCreate()
    # load csv and transform it by inferring schema 
    songs_df = spark.read.csv(dataset, header=True, inferSchema=True)

    # add unique IDs to the DataFrames
    songs_df = songs_df.withColumn("id", monotonically_increasing_id())

    # transform into a delta lakes table and store it 
    songs_df.write.format("delta").mode("overwrite").saveAsTable("songs_delta")
    
    num_rows = songs_df.count()
    print(num_rows)

    return "finished transform and load"

if __name__ == "__main__":
    load()