import fileinput
import logging
import os

log = logging.getLogger(__name__)
log_level = os.environ.get('XMAS_LEVEL')
if log_level is not None:
  logging.basicConfig(format='', level=logging._nameToLevel[log_level])

number_words = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

sum = 0
for line in fileinput.input():
  line = line.strip()
  length = len(line)
  frst = None
  recent = None
  for i, c in enumerate(line):
    if c in '0123456789':
      i += 1
      if frst is None:
        frst = c
      recent = c
      continue

    if c not in 'otfsen':
      continue

    rem = length - i
    if rem < 3:
      continue

    for to_check in (3, 4, 5):
      if rem < to_check:
        continue

      chunk = line[i:i + to_check]
      num = number_words.get(chunk)
      log.debug(f'{line.strip()} {to_check}: {chunk}')
      if num is None:
        continue

      log.info(f'found number word: {chunk}')
      if frst is None:
        frst = num
      recent = num
      break
  log.debug(f'{line.strip()} {frst} {recent}')
  sum += int(frst + recent)

print(sum)
