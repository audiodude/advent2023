import fileinput
import logging
import os

log = logging.getLogger(__name__)
log_level = os.environ.get('XMAS_LEVEL')
if log_level is not None:
  logging.basicConfig(format='', level=logging._nameToLevel[log_level])

maximums = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def validate_grab(grab):
  for comp in grab.split(','):
    sub_parts = comp.split(' ')
    log.debug(sub_parts)

    num = int(sub_parts[1])
    color = sub_parts[2]
    log.info(f'{num} {color}')

    if num > maximums[color]:
      return False
  return True


sum_ = 0
for line in fileinput.input():
  line = line.strip()
  parts = line.split(':')

  id_ = int(parts[0].split(' ')[1])
  all_valid = False
  if all(validate_grab(grab) for grab in parts[1].split(';')):
    sum_ += id_

print(sum_)
