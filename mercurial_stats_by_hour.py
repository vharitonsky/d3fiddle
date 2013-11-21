import sys
from mercurial import hg, ui
from datetime import datetime


repo = hg.repository(ui.ui(), sys.argv[1])
changes = repo.changelog
revs = repo.revs('date(-30)')

revs_by_hours = {i: 0 for i in range(24)}


def order_by_hour_items(revs):
    return sorted(
        revs.items(),
        cmp=lambda a, b: cmp(a[0], b[0])
    )

for rev in revs:
    revision = changes.revision(rev)
    info = revision.split('\n')
    hash, commiter, timestamp = info[:3]
    seconds, tzshift = timestamp.split(' ')[:2]
    revs_by_hours[datetime.fromtimestamp(int(seconds)).hour] += 1

print 'hour\tcommits'
print '\n'.join(('{:d}\t{:d}'.format(*item) for item in order_by_hour_items(revs_by_hours)))
