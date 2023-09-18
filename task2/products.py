import pyspark


def main():
    # Точка входа в Спарк сессию
    spark = pyspark.sql.SparkSession.builder.getOrCreate()

    # Данные
    products = [[1, "prod1"],
                [2, "prod2"],
                [3, "prod3"],
                [4, "prod4"]]

    categories = [[1, "categ1"],
                  [2, "categ2"],
                  [3, "categ3"],
                  [4, "categ4"],
                  [5, "categ5"]]

    # Связть между продуктами и категориями
    prod_categ = [[1, 2],
                  [1, 4],
                  [1, 5],
                  [2, 3],
                  [3, None],
                  [4, 3],
                  [4, 1]]

    # Создаем столбцы датафреймов
    columns1 = ['id', 'name']
    columns2 = ['id_product', 'id_categories']

    # Создаем датафреймы
    df_product = spark.createDataFrame(products, columns1)
    df_category = spark.createDataFrame(categories, columns1)
    df_prod_categ = spark.createDataFrame(prod_categ, columns2)

    # 1 способ решени задачи через функции датафрейма
    df_result = df_product.join(df_prod_categ.join(df_category,
                                                   df_prod_categ['id_categories'] == df_category['id']),
                                df_product['id'] == df_prod_categ['id_product'], 'outer').select(df_product.name,
                                                                                                 df_category.name)

    # 2 способ через SQL запрос
    df_product.createOrReplaceTempView("df_sql_pr")
    df_category.createOrReplaceTempView("df_sql_cat")
    df_prod_categ.createOrReplaceTempView("df_sql_pr_cat")
    sql_result = spark.sql("SELECT df_sql_pr.name, df_sql_cat.name FROM df_sql_pr LEFT JOIN "
                           "df_sql_pr_cat ON df_sql_pr.id = df_sql_pr_cat.id_product LEFT JOIN df_sql_cat ON "
                           "df_sql_pr_cat.id_categories = df_sql_cat.id")

    print(df_result.show())
    print(sql_result.show())
    spark.stop()


if __name__ == '__main__':
    main()
