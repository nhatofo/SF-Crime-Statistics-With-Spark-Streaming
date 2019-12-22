## SF Crime Statistics with Spark Streaming

### Objective
This project is to analyse Francisco crime incidents, and we will provide statistical analyses of the data using Apache Spark Structured Streaming. 

### Development Environment:

Spark 2.4.3
Scala 2.11.x
Java 1.8.x
Kafka build with Scala 2.11.x
Python 3.6.x or 3.7.x

### Environment Setup:

##### Download Spark from https://spark.apache.org/downloads.html. Choose  Apache Hadoop 2.7 or later
Unpack Spark on desired folder.
Download Scala from the official site(version 2.11.x)
Run below to verify correct versions

java -version
scala -version

Make sure your ~/.bash_profile looks like below (might be different based on your directory)
export SPARK_HOME=/Users/dev/spark-2.3.0-bin-hadoop2.7
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home
export SCALA_HOME=/usr/local/scala/
export PATH=$JAVA_HOME/bin:$SPARK_HOME/bin:$SCALA_HOME/bin:$PATH
Running this project

### 1. Starting the Project
Install requirements using ./start.sh if you use conda for Python. If you use pip rather than conda, then use pip install -r requirements.txt.

Use the commands below to start the Zookeeper and Kafka servers. You can find the bin and config folder in the Kafka binary that you have downloaded and unzipped.

bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

You can start the bootstrap server using this Python command: python producer_server.py.


### 2. Build the Kafka server
To build a simple Kafka server you can follow this steps, using the command bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <your-topic-name> --from-beginning to see the output.

### 3. Runing Apache Spark
In data_stream.py use this command:

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.0 --master local data_stream.py