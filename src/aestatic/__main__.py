import sys
import git
from datetime import datetime

from .tasks.markdown import task

from .processor import Processor
from .tasks import copy, compress, slides, sass

processor = Processor()

if '--no-cache' in sys.argv:
    processor.cache_dict.clear()

processor.register(sass.SassTask())
processor.register(compress.CompressTask())
processor.register(slides.SlidesTask())
processor.register(task.MarkdownTask())
processor.register(copy.CopyTask())


repo = git.Repo()
processor.environment['git_sha'] = repo.git.rev_parse(repo.head.object.hexsha)
processor.environment['timestamp'] = repo.head.commit.committed_datetime

processor.run()

sys.exit()