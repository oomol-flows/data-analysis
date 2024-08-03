from oocana import Context

# "in", "out" is the default node key.
# Redefine the name and type of the node, change it manually below.
# Click on the gear(⚙) to configure the input output UI

def main(inputs: dict, context: Context):
  # inputs.get("in") -> help you get node input value
  df = inputs.get("df")
  column_name = inputs.get("column_name")
  new_df = df.drop(columns=[column_name])
  context.preview(new_df)
  return { "df": new_df }