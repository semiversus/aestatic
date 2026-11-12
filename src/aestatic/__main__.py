import sys
import git

from .processor import Processor
from .tasks import copy, compress, sass, markdown, source, code_mirror, pyodide


processor = Processor()

processor.register(sass.SassTask())
processor.register(compress.CompressTask())
processor.register(markdown.SlidesTask())
processor.register(source.SourceTask())
processor.register(copy.CopyTask())
processor.register(code_mirror.CodeMirrorTask())
processor.register(pyodide.PyodideTask())
processor.register(markdown.PageTask())

repo = git.Repo()
processor.environment["git_sha"] = repo.git.rev_parse(repo.head.object.hexsha)
processor.environment["timestamp"] = repo.head.commit.committed_datetime

processor.run()

sys.exit()
