from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").getOrCreate()

Products = spark.createDataFrame([
    ('1', 'product_1'),
    ('2', 'product_2'),
    ('3', 'product_3'),
    ('4', 'product_4'),
    ('5', 'product_5'), ],
    ['key', 'nameProduct'])
Products.createOrReplaceTempView("Products")

Categories = spark.createDataFrame([
    ('1', 'category_1'),
    ('2', 'category_2'),
    ('3', 'category_3'),
    ('4', 'category_4'),
    ('5', 'category_5'), ],
    ['key', 'nameCategory'])
Categories.createOrReplaceTempView("Categories")

Dependencies = spark.createDataFrame([
    ('1', '1'),
    ('1', '2'),
    ('2', '2'),
    ('2', '3'),
    ('3', '3'),
    ('3', '4'),
    ('4', '4'),
    ('4', '5')],
    ['keyProduct', 'keyCategory'])
Dependencies.createOrReplaceTempView("Dependencies")

spark.sql(""" SELECT Products.nameProduct, Categories.nameCategory
              FROM Products 
                  LEFT JOIN Dependencies 
                      ON Products.key=Dependencies.keyProduct
                  LEFT JOIN Categories 
                      ON Categories.key=Dependencies.keyCategory
                  ORDER BY Products.nameProduct; """) \
     .show()