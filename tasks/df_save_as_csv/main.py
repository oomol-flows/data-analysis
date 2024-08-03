from oocana import Context

# "in", "out" is the default node key.
# Redefine the name and type of the node, change it manually below.
# Click on the gear(⚙) to configure the input output UI

def main(inputs: dict, context: Context):
  # inputs.get("in") -> help you get node input value
  df = inputs.get("df")
  dir = inputs.get("csv_address")
  name = inputs.get("name")
  result = dir + "/" + name + ".csv"
  df.to_csv(result, sep=';', index=False, header=True)
  # context.send_message({
  #   # type can be "image", "video", "audio", "markdown"
  #   "type": "image",
  #   # data can be file path, base64
  #   "data": "",
  # })
  context.preview(df)
  return { "df": df }