import fileinput
import logging
import os

log = logging.getLogger(__name__)
log_level = os.environ.get('XMAS_LEVEL')
if log_level is not None:
  logging.basicConfig(format='', level=logging._nameToLevel[log_level])

symbols = set()
numbers = {}
digits = ''


def process_char(x, y, char):
  global digits
  if char.isdigit():
    digits += char
    return

  if digits != '':
    log.debug('pending digits: %s', digits)
    num = int(digits)
    for i in range(x - len(digits), x):
      numbers[(i, y)] = (num, (x - len(digits), y))
    digits = ''

  if char != '.':
    symbols.add((x, y))


y = 0
for line in fileinput.input():
  x = 0
  line = line.strip()
  digits = ''
  for char in line:
    process_char(x, y, char)
    x += 1
  process_char(x, y, '.')
  y += 1

sum_ = 0
seen_nums = set()
for coord in symbols:
  for dx in (-1, 0, 1):
    for dy in (-1, 0, 1):
      if dx == 0 and dy == 0:
        continue

      ix = coord[0] + dx
      iy = coord[1] + dy

      num_with_coord = numbers.get((ix, iy))
      if num_with_coord is None:
        continue

      if num_with_coord[1] not in seen_nums:
        log.debug('%s: found - %s %s', coord, *num_with_coord)
        sum_ += num_with_coord[0]
        seen_nums.add(num_with_coord[1])
      else:
        log.debug('%s: skipping - %s %s', coord, *num_with_coord)

print(sum_)
