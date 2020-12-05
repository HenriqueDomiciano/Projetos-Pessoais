import pandas as pd 

df = pd.read_csv(r'C:\Users\Dell\Desktop\stack_survey\Data\survey_results_public.csv')
df_rows,df_columns = df.shape
df_colunms_data_types = df.info()

#pd.set_option('display.max_columns',85)

schema_df=pd.read_csv(r'C:\Users\Dell\Desktop\stack_survey\Data\survey_results_schema.csv')

#pd.set_option("display.max_rows",85)

#print(df.head(5))

print(df[''])