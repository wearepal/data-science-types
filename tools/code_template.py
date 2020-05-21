"""Code taken from pytorch

https://github.com/pytorch/pytorch/blob/385165ec674b764eb42ffe396f98fadd08a513eb/aten/src/ATen/code_template.py
"""
from __future__ import annotations

from pathlib import Path
import re
from typing import Optional, Dict, Union, List


ReplacementType = Union[str, int, List[Union[str, int]]]


class CodeTemplate:
    """Match $identifier or ${identifier} and replace with value in env

    If this identifier is at the beginning of whitespace on a line and its value is a list then it
    is treated as block subsitution by indenting to that depth and putting each element of the list
    on its own line. If the identifier is on a line starting with non-whitespace and a list
    then it is comma separated. ${,foo} will insert a comma before the list. If this list is not
    empty and ${foo,} will insert one after.
    """

    # Python 2.7.5 has a bug where the leading (^[^\n\S]*)? does not work,
    # workaround via appending another [^\n\S]? inside

    substitution_str = r"(^[^\n\S]*[^\n\S]?)?\$([^\d\W]\w*|\{,?[^\d\W]\w*\,?})"

    # older versions of Python have a bug where \w* does not work,
    # so we need to replace with the non-shortened version [a-zA-Z0-9_]*
    # https://bugs.python.org/issue18647

    substitution_str = substitution_str.replace(r"\w", r"[a-zA-Z0-9_]")

    subtitution = re.compile(substitution_str, re.MULTILINE)

    @classmethod
    def from_file(cls, filename: Path) -> CodeTemplate:
        with filename.open("r") as f:
            return cls(f.read())

    def __init__(self, pattern: str):
        self.pattern = pattern

    @staticmethod
    def indent_lines(indent: str, v: List[Union[str, int]], after: str) -> str:
        return "\n".join([indent + l + after for e in v for l in str(e).splitlines()])  # .rstrip()

    def substitute(
        self, env: Optional[Dict[str, ReplacementType]] = None, /, **kwargs: ReplacementType
    ) -> str:
        env_ = env or {}

        def replace(match: re.Match) -> str:
            indent = match.group(1)
            key = match.group(2)
            comma_before = ""
            comma_after = ""
            if key[0] == "{":
                key = key[1:-1]
                if key[0] == ",":
                    comma_before = ", "
                    key = key[1:]
                if key[-1] == ",":
                    comma_after = ", "
                    key = key[:-1]

            # lookup
            v = kwargs[key] if key in kwargs else env_[key]

            if indent is not None:
                if not isinstance(v, list):
                    v = [v]
                return self.indent_lines(indent, v, comma_after.rstrip())
            elif isinstance(v, list):
                middle = ", ".join([str(x) for x in v])
                if len(v) == 0:
                    return middle
                return comma_before + middle + comma_after
            else:
                return str(v)

        return self.subtitution.sub(replace, self.pattern)


if __name__ == "__main__":
    pattern = """\
    def plot($text_args, $label_args)
    def bar(
        $text_args
        $label_args
    )
    def scatter(
        ${text_args,}
        ${label_args,}
    )
    """
    c = CodeTemplate(pattern)
    print(
        c.substitute(
            text_args=["fontsize: int", "tickness: float"],
            label_args=["size: float", "color: str"],
        )
    )
