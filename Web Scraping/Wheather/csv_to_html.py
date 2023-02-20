import pandas as pd
import html
with open('file.html','w') as wf:
    df1=pd.read_csv('file.csv')
    df1.encoding='utf-8'
    print('data is this')
    print(df1)
    html_output=df1.to_html()
    print('Proper Output')
    print(html_output)
    wf.write(html_output)