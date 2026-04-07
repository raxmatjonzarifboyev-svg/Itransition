import re 
import json 
from pyspark.sql.types  import StructType, StructField, StringType 

path=r'/Volumes/itransition/default/first_tast/task1_d.json'

with open(path,'r') as f:
    df=f.read()

df=re.sub(r':(\w+)',r'"\1"',df)
context=df.replace("=>",':')

context=json.loads(context)
group_name=context[0].keys()

schema=StructType([StructField(col,StringType(),True) for col in group_name])

frane=spark.createDataFrame(context,schema=schema)

frane.write.mode('overwrite').saveAsTable('itransition.default.first_tast')
print('saved as table')




