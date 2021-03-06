EXAMPLE_DIR = /user/$(USER)/ols1d/
INPUT_DIR   = $(EXAMPLE_DIR)/input
OUTPUT_DIR  = $(EXAMPLE_DIR)/output
PIG_OUTPUT_DIR  = $(EXAMPLE_DIR)/pig-output
OUTPUT_FILE = $(OUTPUT_DIR)/part-00000

TOOLLIBS_DIR=$(HADOOP_PREFIX)/share/hadoop/tools/lib/

run: inputs 
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	hadoop jar $(TOOLLIBS_DIR)/hadoop-streaming-$(HADOOP_VERSION).jar \
		-files ./map.py,./combine.py,./reduce.py \
		-mapper ./map.py \
		-combiner ./combine.py \
		-reducer ./reduce.py \
		-input $(INPUT_DIR) \
		-output  $(OUTPUT_DIR) 
	hdfs dfs -cat $(OUTPUT_FILE)

runpig: inputs input/data.dat
	-hdfs dfs -rm -f -r $(PIG_OUTPUT_DIR)
	pig ols.pig
	hdfs dfs -cat $(PIG_OUTPUT_DIR)/part-r-00000

directories:
	hdfs dfs -test -e $(EXAMPLE_DIR) || hdfs dfs -mkdir $(EXAMPLE_DIR)
	hdfs dfs -test -e $(INPUT_DIR) || hdfs dfs -mkdir $(INPUT_DIR)
	hdfs dfs -test -e $(OUTPUT_DIR) || hdfs dfs -mkdir $(OUTPUT_DIR)

input/data.dat: data.py
	./data.py --npts=1000000 > $@

input/small-data.dat: data.py
	./data.py --npts=1000 > $@

inputs: directories input/data.dat
	hdfs dfs -test -e $(INPUT_DIR)/data.dat \
	  || hdfs dfs -put input/data.dat $(INPUT_DIR)/data.dat

clean:
	-hdfs dfs -rm -f -r $(INPUT_DIR)
	-hdfs dfs -rm -f -r $(OUTPUT_DIR)
	-hdfs dfs -rm -f -r $(EXAMPLE_DIR)
	-hdfs dfs -rm -f -r $(PIG_OUTPUT_DIR)
	-rm -f input/*

.PHONY: directories inputs clean run runpig
