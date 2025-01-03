# from bokeh.plotting import figure, show
# p = figure(title="Simple Plot", x_axis_label='X', y_axis_label='Y')
# p.line([1, 2, 3, 4], [4, 6, 2, 3], legend_label="Line", line_width=2)
# show(p)

from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.models import Slider

# Create a plot
plot = figure(title="Simple Plot", x_axis_label='X', y_axis_label='Y')
plot.line([1, 2, 3, 4], [4, 6, 2, 3], legend_label="Line", line_width=2)

# Create a slider
slider = Slider(start=0, end=10, value=1, step=0.1, title="Value")

# Combine the slider and plot into a layout
layout = column(slider, plot)

# Show the layout
show(layout)
