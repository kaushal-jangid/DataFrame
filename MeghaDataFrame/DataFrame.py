#import the pandas library and aliasing as pd
#from tabulate import tabulate
import pandas as pd
# 1. Sample to Import Blank Data
#df = pd.DataFrame()
# 2. Read from CSV
df = pd.read_csv("Import.csv")
# 3. First Five entries
# df.head()
# 4. Last Five entries
# df.tail()
# 5. Pretty Print in Terminal
#print(df.to_markdown())
# 6. To Print Data
print(df)

# 7. Filter Data
df['Department']
print(df)
