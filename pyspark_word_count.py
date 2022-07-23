# Reading file
file_obj = spark.sparkContext.textFile("test.txt")
# Slip the lines via space(" ")
rdd2 = file_obj.flatMap(lambda x: x.split(" "))
# Count each word as one. Key is word and value is 1 
rdd3 = rdd2.map(lambda x: (x,1))
# Aggregating total count of a word. Key is word
rdd4 = rdd3.reduceByKey(lambda a,b: a+b)
# Sort by key 
rdd5 = rdd4.map(lambda x: (x[1],x[0])).sortByKey()
# Get all data
print(rdd5.collect())
