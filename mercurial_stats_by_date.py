import sys
from mercurial import hg, ui
from datetime import datetime
from collections import defaultdict


repo = hg.repository(ui.ui(), sys.argv[1])
changes = repo.changelog
revs = repo.revs('date(-30)')

revs_by_dates = defaultdict(int)


def order_by_date_items(revs):
    return sorted(
        revs.items(),
        cmp=lambda a, b: cmp(datetime.strptime(a[0], '%Y-%m-%d'), datetime.strptime(b[0], '%Y-%m-%d'))
    )

for rev in revs:
    revision = changes.revision(rev)
    info = revision.split('\n')
    hash, commiter, timestamp = info[:3]
    seconds, tzshift = timestamp.split(' ')[:2]
    date = datetime.fromtimestamp(int(seconds)).strftime('%Y-%m-%d')
    revs_by_dates[date] += 1

print 'date\tcommits'
print '\n'.join(('{:s}\t{:d}'.format(*item) for item in order_by_date_items(revs_by_dates)))
