from oocana import Context
import pandas as pd
import plotly.express as px
# "in", "out" is the default node key.
# Redefine the name and type of the node, change it manually below.
# Click on the gear(⚙) to configure the input output UI

def main(inputs: dict, context: Context):
  # inputs.get("in") -> help you get node input value
  # print(inputs.get("in"))



  df = inputs.get("df")
  color = inputs.get("color")

  title = inputs.get("title")
  x_column = inputs.get("x_column")
  y_column = inputs.get("y_column")

    # 使用 Plotly 创建柱状图
  fig = px.bar(df, x=x_column, y=y_column,
                 title=title, color_discrete_sequence=[color])

  # plt.clf()
  fig.show()
  return { "df": df }