import pandas as pd
import re


def clean(str):
  return re.sub(r'[^\w\s]', '', str.strip().lower())

df = pd.read_parquet('trivia_questions.parquet')

'''
new_df = df.drop(columns=['question_id', 'question_source', 'entity_pages', 'search_results'])
new_df = new_df.rename(columns={'answer': 'answer_aliases'})
new_df['answers'] = new_df['answer_aliases'].apply(lambda x: x["value"])
new_df['answer_aliases'] = new_df['answer_aliases'].apply(lambda x: x["aliases"])

print(new_df.columns)
new_df.to_csv("trivia_formatted.csv")
'''

first_250 = df.head(250)
first_250 = first_250.drop(columns=['question_id', 'question_source', 'entity_pages', 'search_results'])
first_250 = first_250.rename(columns={'answer': 'answer_aliases'})
first_250['answers'] = first_250['answer_aliases'].apply(lambda x: x["value"])
first_250['answer_aliases'] = first_250['answer_aliases'].apply(lambda x: x["aliases"])
first_250['answers_norm'] = first_250['answers'].apply(lambda x: clean(x))
first_250["aliases_norm"] = first_250['answer_aliases'].apply(lambda x: [clean(word) for word in x])

first_250.to_csv("trivia_small_batch.csv")
