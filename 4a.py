import fileinput
import logging
import os

log = logging.getLogger(__name__)
log_level = os.environ.get('XMAS_LEVEL')
if log_level is not None:
  logging.basicConfig(format='', level=logging._nameToLevel[log_level])

total = 0
for line in fileinput.input():
  line = line.strip()
  _, cards = line.split(':')
  winning, ours = cards.split('|')
  winning_nums = set(n for n in winning.split(' ') if n != '')
  our_nums = [n for n in ours.split(' ') if n != '']

  score = None
  for num in our_nums:
    if num in winning_nums:
      if score is None:
        score = 1
      else:
        score *= 2
      log.debug('found match (%s), new score is: %s', num, score)

  total += score if score is not None else 0

print(total)
