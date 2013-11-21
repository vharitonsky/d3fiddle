import sys
from mercurial import hg, ui
from collections import defaultdict


repo = hg.repository(ui.ui(), sys.argv[1])
changes = repo.changelog
revs = repo.revs('date(-30)')

revs_by_commiter = defaultdict(int)


def order_by_commit_no_items(revs):
    return sorted(
        revs.items(),
        cmp=lambda a, b: cmp(a[1], b[1])
    )[:-15]

for rev in revs:
    revision = changes.revision(rev)
    info = revision.split('\n')
    hash, commiter, timestamp = info[:3]
    revs_by_commiter[commiter] += 1

print 'commiter\tcommits'
print '\n'.join(('{:s}\t{:d}'.format(*item) for item in order_by_commit_no_items(revs_by_commiter)))
