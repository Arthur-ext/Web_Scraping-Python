
# import pandas as pd
# import requests as rqs
# from bs4 import BeautifulSoup

# try: 
#     req = rqs.get('https://www.basketball-reference.com/leagues/NBA_2018_totals.html')

#     if req.status_code == 200:
#         print("Requisição bem sucedida!")
#         content = req.content
#     else: 
#         raise Exception("ops, houve um erro na requisição")
# except Exception as ex:
#     print(ex)
#     raise
# soup = BeautifulSoup(content, 'html.parser')
# table = soup.find(name="table")

# table_str = str(table)
# df = pd.read_html(table_str)[0]
# print(df)