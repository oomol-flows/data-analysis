from oocana import Context

# "in", "out" is the default node key.
# Redefine the name and type of the node, change it manually below.
# Click on the gear(⚙) to configure the input output UI

def main(inputs: dict, context: Context):
  # inputs.get("in") -> help you get node input value
  df = inputs.get("df")
  name = inputs.get("column_name")
  min_threshold = inputs.get("min_threshold")
  max_threshold = inputs.get("max_threshold")
  filtered_df = df[(df[name] > min_threshold) & (df[name] < max_threshold)]
  # context.send_message({
  #   # type can be "image", "video", "audio", "markdown"
  #   "type": "image",
  #   # data can be file path, base64
  #   "data": "",
  # })
  context.preview(filtered_df)
  return { "df": filtered_df }