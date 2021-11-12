import plotly.graph_objects as go
import plotly.io as pio

pio.templates["custom"] = pio.templates["plotly_white"]

pio.templates['custom']['layout']['paper_bgcolor'] = '#EDEDED'
pio.templates['custom']['layout']['plot_bgcolor'] = '#EDEDED'
pio.templates['custom']['layout']['coloraxis']['showscale'] = False
pio.templates['custom']['layout']['title']['x'] = 0.5
pio.templates['custom']['layout']['title']['font']['family'] = "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
pio.templates['custom']['layout']['font']['size'] = 14
pio.templates['custom']['layout']['font']['family'] = "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
pio.templates['custom']['layout']['margin'] = {'b': 10, 'l': 0, 'r': 10}
pio.templates['custom']['layout']['xaxis']['visible'] = False

if __name__ == "__main__":
    print(pio.templates['custom'])
