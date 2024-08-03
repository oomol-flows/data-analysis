from oocana import Context

# "in", "out" is the default node key.
# Redefine the name and type of the node, change it manually below.
# Click on the gear(⚙) to configure the input output UI

def main(inputs: dict, context: Context):
  # inputs.get("in") -> help you get node input value
  df = inputs.get("df")
  name = inputs.get("column_name")
  sort_type = inputs.get("sort_type")
  sorted_df = None
  if sort_type == "Ascending":
    sorted_df = df.sort_values(by=name)
  else:
     sorted_df = df.sort_values(by=name, ascending=False)
  context.preview(sorted_df)
  return { "df": sorted_df }