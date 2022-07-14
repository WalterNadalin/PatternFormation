from seaborn import heatmap
from numpy import linspace
from matplotlib.pyplot import xlabel, ylabel, savefig, close, title

def heat_map(name: str, x_range: tuple, y_range: tuple, values: list, *, x_n: int = 10, y_n: int = 10) -> None:
  image = heatmap(values, cmap = 'jet', xticklabels = False)

  x_ticks = linspace(0, values.shape[1], x_n)
  x_labels = linspace(*x_range, x_n)
  x_labels = x_labels.astype(int)

  image.set_xticks(x_ticks)
  image.set_xticklabels(x_labels)

  y_ticks = linspace(0, values.shape[0], y_n)
  y_labels = linspace(*y_range, y_n)
  y_labels = y_labels.astype(int)
  image.set_yticks(y_ticks)
  image.set_yticklabels(y_labels)

  xlabel('Space')
  ylabel('Time')
  title('Variation of the density through space and time')
  savefig(f'./results/{name}.png')
  close()
