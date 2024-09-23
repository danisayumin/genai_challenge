import time
import sys

def snake_loader(curr, max_total, max_bar):
  step_size = max_total // max_bar
  norm_curr = curr // step_size
  return ' '*max_bar if norm_curr == 0 else ((('='*(norm_curr-1)) + '>') + ' '*(max_bar-norm_curr))

def    ft_progress(lst):
    total = len(lst)
    start = time.time()

    for i, item in enumerate(lst):
        elapsed_time = time.time() - start
        percent = (i + 1) / total
        if i + 1 > 0:
            eta = (elapsed_time / (i + 1)) * (total - (i + 1))
        else:
            eta = 0

        bar_length = 10
        #filled_length = int(bar_length * percent)
        #bar = '=' * filled_length + ' ' * (bar_length - filled_length)

        print(f"ETA: {eta:.2f}s [{percent * 100:.2f}%] [{snake_loader(i, total, bar_length)}] [{i + 1}/{total}] | elapsed time {elapsed_time:.2f}s", end="\r")
        yield item

if __name__ == "__main__":
    example_list = range(100)
    for item in ft_progress(example_list):
        time.sleep(0.05)