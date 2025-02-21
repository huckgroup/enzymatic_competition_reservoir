from typing import NamedTuple
import matplotlib as mpl
from matplotlib.colors import ListedColormap
import seaborn as sns

nord_categorical = [
    "#5e81ac",
    "#d08770",
    "#a3be8c",
    "#bf616a",
    "#b48ead",
    "#ebcb8b",
    "#88c0d0",
] # colors for distinct elements

class nord_base(NamedTuple):
  # colors for background, faces and text
    light=[
        "#eceff4",
        "#e5e9f0",
        "#d8dee9",
    ]
    dark=[
        "#2e3440",
        "#3b4252",
        "#434c5e",
        "#4c566a",
    ]

def shades(main_color, n: int):
    """ Produces #n shade variations (light to dark) of main_color """
    rgb = sns.palettes._color_to_rgb(main_color, input='rgb')
    light = sns.light_palette(main_color,6)[1]
    dark = sns.dark_palette(main_color,6)[2]
    if n % 2:
        return sns.color_palette(sns.blend_palette([light, rgb, dark], n+2)[:n])
    else:
        return sns.color_palette(sns.blend_palette([light, rgb, dark], n+1)[:n])

def set_style():
    mpl.colormaps.unregister('nord')
    mpl.colormaps.register(ListedColormap(nord_categorical, name='nord', N=7))

    sns.set_theme(
        style="ticks",
        context="paper",
        # font_scale=0.7,
        rc={
            "axes.linewidth": 0.5,
            "grid.linewidth": 0.5,
            # "axes.facecolor": "#eceff4",
            "axes.facecolor": "#ffffff",
            "axes.edgecolor": "#2e3440",
            "axes.labelcolor": "#2e3440",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "text.color": "#2e3440",
            "xtick.color": "#2e3440",
            "ytick.color": "#2e3440",
            "xtick.major.size": 2.5,
            "ytick.major.size": 2.5,
            "xtick.major.pad": 2.5,
            "ytick.major.pad": 2.5,
            "xtick.major.width": 0.5,
            "ytick.major.width": 0.5,
            "xtick.minor.size": 1,
            "ytick.minor.size": 1,
            "xtick.minor.width": 0.5,
            "ytick.minor.width": 0.5,
            "lines.linewidth": 1.0,
            'patch.linewidth': 0.5,
            "font.family": "Arial",
            "font.size": 8,
            'axes.labelsize': 6.0,
            'axes.labelpad': 4,
            'axes.titlesize': 6.0,
            'xtick.labelsize': 6.0,
            'ytick.labelsize': 6.0,
            'legend.fontsize': 6.0,
            'legend.title_fontsize': 6.0,
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
        },
    )

    sns.set_palette('nord', 7, color_codes=True)



