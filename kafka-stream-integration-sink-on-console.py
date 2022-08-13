'''
Prerequiste for integration with kafka Stream. Output will be written in Console.
Download: https://dlcdn.apache.org/kafka/3.2.1/kafka_2.13-3.2.1.tgz
$ tar -xzf kafka_2.13-3.2.1.tgz
$ cd kafka_2.13-3.2.1
[All commands will be run on different terminals]
$ bin/zookeeper-server-start.sh config/zookeeper.properties
$ bin/kafka-server-start.sh config/server.properties
$ bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
$ bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092 --property "key.separator=:" --property "parse.key=true"
  >car1:lag-1234,lat-5678
  >car2:lag-2234,lat-5672 	
  [Use for producing events in kafka stream topic-> quickstart-events. Events will be consumed by PySpark Streaming Consumer]
$ bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
  [dummy consumer to validate the data]

Run/Start the below code with: --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0   
./bin/pyspark --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0
./bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0  <py file name>

'''

import pyspark
from pyspark.sql import SparkSession

# Create Spark Session with Application Name-> MyFirstSparkApp
spark = SparkSession.builder.appName("Kafka-App").getOrCreate()

print("Kafka client ....")
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "quickstart-events") \
  .load()

# Write to console 
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)").writeStream.outputMode("append").format("console").start().awaitTermination()
