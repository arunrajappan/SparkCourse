import os
import sys

def setup():
    # Path for spark source folder
    # os.environ['SPARK_HOME']="c:\spark"

    # Append pyspark  to Python Path
    sys.path.append(os.environ['SPARK_HOME']+"\python")
    sys.path.append(os.environ['SPARK_HOME']+"\python\lib\py4j-0.9-src.zip")


