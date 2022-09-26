import pyspark
from pyspark.sql import SparkSession
import findspark
findspark.init()

session = SparkSession.builder.appName('app').getOrCreate()
print(session)
session

<pyspark.sql.session.SparkSession object at 0x0000026534839220>
SparkSession - in-memory

SparkContext

Spark UI

Version
v3.3.0
Master
local[*]
AppName
app

dept = [("Finance",10),("Marketing",20),("Sales",30),("IT",40),("Admin",50),("Security",60),("MgMT",70),("HR",80)]
rdd = session.sparkContext.parallelize(dept)
print(type(rdd))
#print(rdd.collect())
print(rdd.take(2))

<class 'pyspark.rdd.RDD'>
[('Finance', 10), ('Marketing', 20)]

print("RDD Count:", rdd.count())
print(rdd.countByKey())
result = (rdd.filter(lambda x: x[1] > 20).collect())
print(result)
rdd1 = session.sparkContext.parallelize(result)
result2 = (rdd1.filter(lambda x: x[1] > 30).collect())
print(result2)

RDD Count: 8
defaultdict(<class 'int'>, {'Finance': 1, 'Marketing': 1, 'Sales': 1, 'IT': 1, 'Admin': 1, 'Security': 1, 'MgMT': 1, 'HR': 1})
[('Sales', 30), ('IT', 40), ('Admin', 50), ('Security', 60), ('MgMT', 70), ('HR', 80)]
[('IT', 40), ('Admin', 50), ('Security', 60), ('MgMT', 70), ('HR', 80)]

dept = [("Finance",10),("Marketing",20),("Sales",30),("IT",40),("Admin",50),("Security",60),("MgMT",70),("HR",80)]
rdd = session.sparkContext.parallelize(dept)
print(type(rdd))
print(rdd.collect())
print(rdd.take(2))
print('RDD Count:', rdd.count())
print('RDD Count by key:', rdd.countByKey())
print('RDD Collect as map:',  rdd.collectAsMap())
print('RDD Num Partitions:', rdd.getNumPartitions())
print(rdd.filter(lambda x: x[1] > 20).collect())
rdd2 = rdd.coalesce(2)
print('RDD Num Partitions:', rdd2.getNumPartitions())

<class 'pyspark.rdd.RDD'>
[('Finance', 10), ('Marketing', 20), ('Sales', 30), ('IT', 40), ('Admin', 50), ('Security', 60), ('MgMT', 70), ('HR', 80)]
[('Finance', 10), ('Marketing', 20)]
RDD Count: 8
RDD Count by key: defaultdict(<class 'int'>, {'Finance': 1, 'Marketing': 1, 'Sales': 1, 'IT': 1, 'Admin': 1, 'Security': 1, 'MgMT': 1, 'HR': 1})
RDD Collect as map: {'Finance': 10, 'Marketing': 20, 'Sales': 30, 'IT': 40, 'Admin': 50, 'Security': 60, 'MgMT': 70, 'HR': 80}
RDD Num Partitions: 8
[('Sales', 30), ('IT', 40), ('Admin', 50), ('Security', 60), ('MgMT', 70), ('HR', 80)]
RDD Num Partitions: 2

a = rdd.toDF()
print(a)
print(type(a))

DataFrame[_1: string, _2: bigint]
<class 'pyspark.sql.dataframe.DataFrame'>

a.show(truncate=False)
columns = ["Name", "id"]
a = session.createDataFrame(data=dept,schema=columns)
a.filter(a.id == 10).show(truncate=False)
a.coalesce(2)
a.rdd.getNumPartitions()
#a.repartitions(8)

+---------+---+
|_1       |_2 |
+---------+---+
|Finance  |10 |
|Marketing|20 |
|Sales    |30 |
|IT       |40 |
|Admin    |50 |
|Security |60 |
|MgMT     |70 |
|HR       |80 |
+---------+---+

+-------+---+
|Name   |id |
+-------+---+
|Finance|10 |
+-------+---+

8

data = session.read.option('header', 'true').csv(f"C:\spark\datasets-master\\titanic.csv")
data.show()
print(type(data))

+-----------+--------+------+--------------------+------+----+-----+-----+----------------+-------+-----+--------+
|PassengerId|Survived|Pclass|                Name|   Sex| Age|SibSp|Parch|          Ticket|   Fare|Cabin|Embarked|
+-----------+--------+------+--------------------+------+----+-----+-----+----------------+-------+-----+--------+
|          1|       0|     3|Braund, Mr. Owen ...|  male|  22|    1|    0|       A/5 21171|   7.25| null|       S|
|          2|       1|     1|Cumings, Mrs. Joh...|female|  38|    1|    0|        PC 17599|71.2833|  C85|       C|
|          3|       1|     3|Heikkinen, Miss. ...|female|  26|    0|    0|STON/O2. 3101282|  7.925| null|       S|
|          4|       1|     1|Futrelle, Mrs. Ja...|female|  35|    1|    0|          113803|   53.1| C123|       S|
|          5|       0|     3|Allen, Mr. Willia...|  male|  35|    0|    0|          373450|   8.05| null|       S|
|          6|       0|     3|    Moran, Mr. James|  male|null|    0|    0|          330877| 8.4583| null|       Q|
|          7|       0|     1|McCarthy, Mr. Tim...|  male|  54|    0|    0|           17463|51.8625|  E46|       S|
|          8|       0|     3|Palsson, Master. ...|  male|   2|    3|    1|          349909| 21.075| null|       S|
|          9|       1|     3|Johnson, Mrs. Osc...|female|  27|    0|    2|          347742|11.1333| null|       S|
|         10|       1|     2|Nasser, Mrs. Nich...|female|  14|    1|    0|          237736|30.0708| null|       C|
|         11|       1|     3|Sandstrom, Miss. ...|female|   4|    1|    1|         PP 9549|   16.7|   G6|       S|
|         12|       1|     1|Bonnell, Miss. El...|female|  58|    0|    0|          113783|  26.55| C103|       S|
|         13|       0|     3|Saundercock, Mr. ...|  male|  20|    0|    0|       A/5. 2151|   8.05| null|       S|
|         14|       0|     3|Andersson, Mr. An...|  male|  39|    1|    5|          347082| 31.275| null|       S|
|         15|       0|     3|Vestrom, Miss. Hu...|female|  14|    0|    0|          350406| 7.8542| null|       S|
|         16|       1|     2|Hewlett, Mrs. (Ma...|female|  55|    0|    0|          248706|     16| null|       S|
|         17|       0|     3|Rice, Master. Eugene|  male|   2|    4|    1|          382652| 29.125| null|       Q|
|         18|       1|     2|Williams, Mr. Cha...|  male|null|    0|    0|          244373|     13| null|       S|
|         19|       0|     3|Vander Planke, Mr...|female|  31|    1|    0|          345763|     18| null|       S|
|         20|       1|     3|Masselmani, Mrs. ...|female|null|    0|    0|            2649|  7.225| null|       C|
+-----------+--------+------+--------------------+------+----+-----+-----+----------------+-------+-----+--------+
only showing top 20 rows

<class 'pyspark.sql.dataframe.DataFrame'>

rdd3 = data.filter(data.Pclass == 3).show(truncate=False)

data = [("James","","Smith","36636","M",60000),
("Michael","Rose","","40288","M",70000),
("Robert","","Williams","42114","",400000),
("Maria","Anne","Jones","39192","F",500000),
("Jen","Mary","Brown","","F",0)]

+-----------+--------+------+---------------------------------------------------------+------+----+-----+-----+----------------+-------+-----+--------+
|PassengerId|Survived|Pclass|Name                                                     |Sex   |Age |SibSp|Parch|Ticket          |Fare   |Cabin|Embarked|
+-----------+--------+------+---------------------------------------------------------+------+----+-----+-----+----------------+-------+-----+--------+
|1          |0       |3     |Braund, Mr. Owen Harris                                  |male  |22  |1    |0    |A/5 21171       |7.25   |null |S       |
|3          |1       |3     |Heikkinen, Miss. Laina                                   |female|26  |0    |0    |STON/O2. 3101282|7.925  |null |S       |
|5          |0       |3     |Allen, Mr. William Henry                                 |male  |35  |0    |0    |373450          |8.05   |null |S       |
|6          |0       |3     |Moran, Mr. James                                         |male  |null|0    |0    |330877          |8.4583 |null |Q       |
|8          |0       |3     |Palsson, Master. Gosta Leonard                           |male  |2   |3    |1    |349909          |21.075 |null |S       |
|9          |1       |3     |Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)        |female|27  |0    |2    |347742          |11.1333|null |S       |
|11         |1       |3     |Sandstrom, Miss. Marguerite Rut                          |female|4   |1    |1    |PP 9549         |16.7   |G6   |S       |
|13         |0       |3     |Saundercock, Mr. William Henry                           |male  |20  |0    |0    |A/5. 2151       |8.05   |null |S       |
|14         |0       |3     |Andersson, Mr. Anders Johan                              |male  |39  |1    |5    |347082          |31.275 |null |S       |
|15         |0       |3     |Vestrom, Miss. Hulda Amanda Adolfina                     |female|14  |0    |0    |350406          |7.8542 |null |S       |
|17         |0       |3     |Rice, Master. Eugene                                     |male  |2   |4    |1    |382652          |29.125 |null |Q       |
|19         |0       |3     |Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)  |female|31  |1    |0    |345763          |18     |null |S       |
|20         |1       |3     |Masselmani, Mrs. Fatima                                  |female|null|0    |0    |2649            |7.225  |null |C       |
|23         |1       |3     |"McGowan, Miss. Anna ""Annie"""                          |female|15  |0    |0    |330923          |8.0292 |null |Q       |
|25         |0       |3     |Palsson, Miss. Torborg Danira                            |female|8   |3    |1    |349909          |21.075 |null |S       |
|26         |1       |3     |Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)|female|38  |1    |5    |347077          |31.3875|null |S       |
|27         |0       |3     |Emir, Mr. Farred Chehab                                  |male  |null|0    |0    |2631            |7.225  |null |C       |
|29         |1       |3     |"O'Dwyer, Miss. Ellen ""Nellie"""                        |female|null|0    |0    |330959          |7.8792 |null |Q       |
|30         |0       |3     |Todoroff, Mr. Lalio                                      |male  |null|0    |0    |349216          |7.8958 |null |S       |
|33         |1       |3     |Glynn, Miss. Mary Agatha                                 |female|null|0    |0    |335677          |7.75   |null |Q       |
+-----------+--------+------+---------------------------------------------------------+------+----+-----+-----+----------------+-------+-----+--------+
only showing top 20 rows