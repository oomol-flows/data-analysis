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

  hex_color = rgb_to_hex(color)

  title = inputs.get("title")
  x_column = inputs.get("x_column")
  y_column = inputs.get("y_column")


  plt.figure(figsize=(10, 6))
  plt.bar(df[x_column], df[y_column], color=hex_color)
  plt.xlabel(x_column)
  plt.ylabel(y_column)
  plt.title(title)
  plt.xticks(rotation=90)
  plt.tight_layout()

  # plt.clf()

  context.preview({
    # type can be "image", "video", "audio", "markdown"
    "type": "image",
    # data can be file path, base64
    "data": draw_to_base64(plt),
  })
  return { "df": df }

def rgb_to_hex(rgb):
  rgb = rgb.replace("rgb(", "").replace(")", "").split(", ")
  hex_color = "#{:02x}{:02x}{:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))
  
  return hex_color

def draw_to_base64(plt):
  buffer = io.BytesIO()
  plt.savefig(buffer, format='png')
  buffer.seek(0)

  # 从缓冲区创建一个Image对象
  image = Image.open(buffer)

  # 将Image对象转换为Base64编码的字符串
  image_base64 = base64.b64encode(buffer.getvalue()).decode()

  # 清除缓冲区和关闭缓冲区
  buffer.close()

  return image_base64
