from oocana import Context
import pandas as pd

def main(inputs: dict, context: Context):
  data = pd.read_csv(inputs["csv"])
  print(data)
  return { "df": data }