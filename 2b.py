import fileinput
import logging
import os

from functools import reduce

log = logging.getLogger(__name__)
log_level = os.environ.get('XMAS_LEVEL')
if log_level is not None:
  logging.basicConfig(format='', level=logging._nameToLevel[log_level])

color_to_idx = {
    'red': 0,
    'green': 1,
    'blue': 2,
}


def find_min(maxes, grab):
  log.debug(f'{maxes}, {grab}')
  for comp in grab.split(','):
    sub_parts = comp.split(' ')
    log.debug(sub_parts)

    num = int(sub_parts[1])
    color = sub_parts[2]
    log.debug(f'{num} {color}')

    idx = color_to_idx[color]
    if maxes[idx] is None or num > maxes[idx]:
      maxes[idx] = num
  return maxes


sum_ = 0
for line in fileinput.input():
  line = line.strip()
  parts = line.split(':')

  id_ = int(parts[0].split(' ')[1])
  all_valid = False
  maxes = reduce(find_min, parts[1].split(';'), [None, None, None])

  power = maxes[0] * maxes[1] * maxes[2]
  sum_ += power

print(sum_)
