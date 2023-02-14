import sys
import git
from datetime import datetime

from .tasks.markdown import PageTask, SlidesTask

from .processor import Processor
from .tasks import copy, compress, sass, markdown

processor = Processor()

if '--no-cache' in sys.argv:
    processor.cache_dict.clear()

processor.register(sass.SassTask())
processor.register(compress.CompressTask())
processor.register(markdown.SlidesTask())
processor.register(markdown.PageTask())
processor.register(copy.CopyTask())


repo = git.Repo()
processor.environment['git_sha'] = repo.git.rev_parse(repo.head.object.hexsha)
processor.environment['timestamp'] = repo.head.commit.committed_datetime

processor.run()

sys.exit()