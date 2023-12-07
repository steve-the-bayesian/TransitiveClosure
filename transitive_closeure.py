import os
import glob


def AddPath(old_path, new_path):
    if isinstance(new_path, str):
        old_path.append(new_path)
    elif isinstance(new_path, list):
        old_path += new_path
    else:
        raise Exception("new_path should be either a string or a list")

    return old_path


class TransitiveClosure:

    def __init__(self):
        self._include_paths = []

    def AddIncludePath(self, include_path):
        self._include_paths = AddPath(
            self._include_paths, include_path)

    def AddSourcePath(self, source_path):
        self._source_paths = AddPath(
            self._source_paths, source_path)

    def FindClosure(self, files):
        pass
