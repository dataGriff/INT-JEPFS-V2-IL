# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Fizz Buzz Test
# MAGIC
# MAGIC The Fizz-Buzz test was invted by Imran Ghory to test candiates applying for various software development roles.
# MAGIC
# MAGIC You can find out more about the history of this test by reading the article
# MAGIC <a href="http://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/" target="_blank">Using FizzBuzz to Find Developers who Grok Coding</a></br>
# MAGIC which dates back to January 24, 2007.
# MAGIC
# MAGIC The test, and your challenge, reads as follows:
# MAGIC
# MAGIC > Write a program that prints the numbers from 1 to 100. But for  
# MAGIC > multiples of three print “Fizz” instead of the number and for the  
# MAGIC > multiples of five print “Buzz”. For numbers which are multiples  
# MAGIC > of both three and five print “FizzBuzz”."  
# MAGIC
# MAGIC A couple of hints:
# MAGIC * You will need a for-loop that itereates over the numbers 0 to 100 inclusive.
# MAGIC * Inside the loop, you will need a combination of **`if`**, **`elif`** and **`else`** statements.
# MAGIC * The modulo (**`%`**) operator will give you the cleanest method for testing for divisability by 3 and 5.
# MAGIC * Start with a short list, say 1 to 15, during your initial development and then scale out to 100 when you think you are ready.
# MAGIC * Don't worry about how pretty your code is - there are many different ways of completing this challenge - all of them are correct, if the output is correct.

# COMMAND ----------

# TODO

for x in range(1,100+1):
  fizz = (x % 3 ==0)
  buzz = (x % 5 ==0)
  if (fizz and buzz):
    print(x,"FizzBuzz")
  elif (fizz):
    print(x,"Fizz")
  elif (buzz):
    print(x,"Buzz")
  else:
    print(x)
  

# COMMAND ----------

# TODO

for x in range(1,100+1):
  output=""
  if(x % 3 ==0):
    output = "Fizz"
  if(x % 5 ==0):
    output += "Buzz"
  if(output == ""):
    output = x
  print(output)
    

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>
