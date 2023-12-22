import fileinput
import logging
import os

from collections import defaultdict

log = logging.getLogger(__name__)
log_level = os.environ.get('XMAS_LEVEL')
if log_level is not None:
  logging.basicConfig(format='', level=logging._nameToLevel[log_level])

num_copies = defaultdict(lambda: 1)
num_copies[1] = 1
idx = 1
for line in fileinput.input():
  line = line.strip()
  _, cards = line.split(':')
  winning, ours = cards.split('|')
  winning_nums = set(n for n in winning.split(' ') if n != '')
  our_nums = [n for n in ours.split(' ') if n != '']

  score = 0
  for num in our_nums:
    if num in winning_nums:
      score += 1
      log.debug('found match (%s), new score is: %s', num, score)

  if score == 0:
    idx += 1
    continue

  log.debug('final score: %s, copying %s-%s', score, idx + 1, idx + score)
  for i in range(idx + 1, idx + score + 1):
    num_copies[i] += num_copies[idx]

  log.debug(f'{num_copies=}')
  idx += 1

print(sum(num_copies[i] for i in range(1, idx)))
