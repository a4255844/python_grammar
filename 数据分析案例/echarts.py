from pyecharts.charts import Line
from pyecharts import options as opts
from main import _data

# 定义数据
x_data = list(_data.keys())
y_data = _data.values()
print(x_data, y_data)
# 创建折线图对象
line = Line(init_opts=opts.InitOpts(width='97vw', height='900px'))

# 添加数据和配置项
line.add_xaxis(x_data)
line.add_yaxis("Series A", y_data)
line.set_global_opts(title_opts=opts.TitleOpts(title="My Line Chart"))
# 生成图表
line.render("line_chart.html")

