"""
The MIT License (MIT)

Copyright (c) 2022-present The Master

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._types import Readable, Writable


__all__ = ("BF",)


class IncrementingCells(list):
    def __getitem__(self, index: int) -> int:
        while index >= len(self):
            self.append(0)
        return super().__getitem__(index)

    def __setitem__(self, index: int, value: int) -> None:
        while index >= len(self):
            self.append(0)
        super().__setitem__(index, value)


class BF:
    def __init__(self, stdin: "Readable" = sys.stdin, stdout: "Writable" = sys.stdout):
        self.cells = IncrementingCells()
        self._index = 0

        self.stdin = stdin
        self.stdout = stdout

    def run(self, code: str) -> None:
        iterator = iter(enumerate(code))

        for pos, char in iterator:
            if char == ">":
                self._index += 1
            elif char == "<":
                if self._index <= 0:
                    self.cells.insert(0, 0)
                else:
                    self._index -= 1
            elif char == "+":
                self.cells[self._index] += 1
            elif char == "-":
                self.cells[self._index] -= 1
            elif char == ",":
                char = self.stdin.read(1)
                self.cells[self._index] = ord(char)
            elif char == ".":
                char = chr(self.cells[self._index])
                self.stdout.write(char)
            elif char == '[':
                end = -1
                for next_pos, next_char in enumerate(code[pos:]):
                    if next_char == ']':
                        end = pos + next_pos
                if end == -1:
                    raise RuntimeError('Unclosed bracket')

                pos += 1
                while self.cells[self._index] != 0:
                    self.run(code[pos:end])

                while pos < end:
                    pos, _ = next(iterator)

    def run_file(self, filename: str) -> None:
        with open(filename, "r") as file:
            code = file.read()
        self.run(code)