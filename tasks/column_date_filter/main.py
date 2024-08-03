from oocana import Context
import pandas as pd

# "in", "out" is the default node key.
# Redefine the name and type of the node, change it manually below.
# Click on the gear(⚙) to configure the input output UI

def main(inputs: dict, context: Context):
  # inputs.get("in") -> help you get node input value
  df = inputs.get("df")
  name = inputs.get("column_name")
  df[name] = pd.to_datetime(df[name])
  start_date = pd.to_datetime(inputs.get("start_date"))
  end_date = pd.to_datetime(inputs.get("end_date"))
  filtered_df_range = df[(df[name] >= start_date) & (df[name] <= end_date)]
  # context.preview(filtered_df_range)

  preview_df = filtered_df_range
  preview_df[name] = preview_df[name].dt.strftime('%Y-%m-%d %H:%M:%S')
  context.preview(preview_df)
  return { "df": filtered_df_range }