from seaborn import heatmap
from numpy import linspace
from matplotlib.pyplot import plot, legend, xlabel, ylabel, savefig, close, title, axhline

def heat_map(name: str, x_range: tuple, y_range: tuple, values: list, *, x_n: int = 10, y_n: int = 10) -> None:
  '''
  Prints a beautiful heatmap given a matrix of values through space and time.

  Parameters
  ---------
  ...
  '''
  image = heatmap(values.transpose(), cmap = 'jet', xticklabels = False)

  x_ticks = linspace(0, values.shape[0], y_n)
  x_labels = linspace(*y_range, y_n)
  x_labels = x_labels.astype(int)

  y_ticks = linspace(0, values.shape[1], x_n)
  y_labels = linspace(*x_range, x_n)
  y_labels = y_labels.astype(int)

  image.set_xticks(x_ticks)
  image.set_xticklabels(x_labels)

  image.set_yticks(y_ticks)
  image.set_yticklabels(y_labels)

  xlabel('Time')
  ylabel('Space')
  title('Variation of the density through space and time')

  savefig(f'./results/{name}.png')
  close()

def coefficients_plot(name: str, time: list, values: list, peaks: list) -> None:
  '''
  ...
  '''
  labels = [f'$k = ${x}' for x in peaks]
  axhline(y = 0, color = 'black', linestyle = '--')
  plot(time, values, label = labels)
  legend()
  xlabel('Time')
  ylabel('Coefficents')
  title('Variation of the modality coefficents in time')
  savefig(f'./results/{name}.png')
  close()
