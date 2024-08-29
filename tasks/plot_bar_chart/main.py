import io
import base64

from PIL import Image
from oocana import Context
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')
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


  plt.figure(figsize=(10, 6))
  plt.bar(df[x_column], df[y_column], color=color)
  plt.xlabel(x_column)
  plt.ylabel(y_column)
  plt.title(title)
  plt.xticks(rotation=90)
  plt.tight_layout()

  # plt.clf()
  plt.show()
  return { "df": df }