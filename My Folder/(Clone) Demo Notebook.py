# Databricks notebook source
print('Hello World!')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello world from SQL"

# COMMAND ----------

# MAGIC %run ./Setup

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')
display(files)

# COMMAND ----------


