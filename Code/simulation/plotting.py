from seaborn import heatmap
from numpy import linspace
from matplotlib.pyplot import plot, legend, xlabel, ylabel, savefig, close, title, axhline, style, fill_between

style.use('default')

def heat_map(name: str, x_range: tuple, y_range: tuple, values: list, *, x_n: int = 10, y_n: int = 10) -> None:
  '''
  Prints a beautiful heatmap given a matrix of values through space and time.
  ...
  '''
  image = heatmap(values.transpose(), cmap = 'jet', xticklabels = False)

  x_ticks = linspace(0, values.shape[0], x_n)
  x_labels = linspace(*x_range, x_n)
  x_labels = x_labels.astype(int)

  y_ticks = linspace(0, values.shape[1], y_n)
  y_labels = linspace(*y_range, y_n)
  y_labels = y_labels.astype(int)

  image.set_xticks(x_ticks)
  image.set_xticklabels(x_labels)

  image.set_yticks(y_ticks)
  image.set_yticklabels(reversed(y_labels))

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
  title('Variation of the modality coefficents w. r. t. time')
  savefig(f'./results/{name}.png')
  close()

def confidence_plot(name: str, confidence_intervals: list, peaks: list, gammas: list) -> list:
  '''
  '''
  for i in range(len(peaks)):
    lower = confidence_intervals[:, i, 0]
    mean = confidence_intervals[:, i, 1]
    upper = confidence_intervals[:, i, 2]
    plot(gammas, mean,'-', label = f'k = {peaks[i]}')
    fill_between(gammas, upper, lower, alpha = 0.15)

  xlabel('Noise intensity')
  ylabel('Average modality powers')
  title('Variation of the average modality w. r. t. noise intensity')
  legend()
  savefig(f'./results/{name}.png')
  close()
