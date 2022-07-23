'''
Running a PySpark Job in local cluster.
1- Run spark local cluster
./sbin/start-master.sh

2- Pick Master URL
INFO Master: Starting Spark master at spark://prakhars-MacBook-Air.local:7077

3- Run Worker
./sbin/start-worker.sh spark://prakhars-MacBook-Air.local:7077


Run Python Spark Job
 ./bin/spark-submit --master spark://prakhars-MacBook-Air.local:7077 /Users/divang/Desktop/PySpark/my_pyspark_first.py myFirstApp
'''
# Create SparkSession from builder
import pyspark
import sys
from pyspark.sql import SparkSession
appName=sys.argv[1]
# Creating Spark Session
spark = SparkSession.builder.appName(appName).getOrCreate()
# Get logger
log4jLogger = spark._jvm.org.apache.log4j
LOGGER = log4jLogger.LogManager.getLogger(__name__)
LOGGER.info("pyspark script logger initialized.....")
#Read a file which already exist in Spark bundle 
textFile = spark.read.text("README.md")
LOGGER.info("... total rows in file ...")
LOGGER.info(textFile.count()) 
LOGGER.info("... Print whole file ...")
LOGGER.info(textFile.collect())


