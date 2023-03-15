import sys
import git

from .processor import Processor
from .tasks import copy, compress, sass, markdown, source

processor = Processor()

if '--no-cache' in sys.argv:
    processor.cache_dict.clear()

processor.register(sass.SassTask())
processor.register(compress.CompressTask())
processor.register(markdown.SlidesTask())
processor.register(source.SourceTask()) 
processor.register(copy.CopyTask())
processor.register(markdown.PageTask())

repo = git.Repo()
processor.environment['git_sha'] = repo.git.rev_parse(repo.head.object.hexsha)
processor.environment['timestamp'] = repo.head.commit.committed_datetime

processor.run()

sys.exit()