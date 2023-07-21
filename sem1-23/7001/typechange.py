import pandas as pd

excel_file = pd.read_excel('newdata.xlsx')

csv_file = excel_file.to_csv('newdata.csv', index=False)

print("CSV 文件已创建。")


