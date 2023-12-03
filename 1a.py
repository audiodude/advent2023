import fileinput
import logging
import os

log = logging.getLogger(__name__)
log_level = os.environ.get('XMAS_LEVEL')
if log_level is not None:
  logging.basicConfig(format='', level=logging._nameToLevel[log_level])

sum = 0
for line in fileinput.input():
  first = None
  recent = None
  for chr in line:
    if chr in '0123456789':
      if first is None:
        first = chr
      recent = chr

  log.debug(f'{line.strip()} {first} {recent}')
  sum += int(first + recent)

print(sum)
