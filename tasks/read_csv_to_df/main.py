from oocana import Context
import pandas as pd
# "in", "out" is the default node key. 
# Redefine the name and type of the node, change it manually below.
# Click on the gear(⚙) to configure the input output UI
def main(inputs: dict, context: Context):
  # input.get("in") -> help you get node input value
  file = inputs.get("csv")
  df = pd.read_csv(file)
  context.preview(df)

  return { "df": df }