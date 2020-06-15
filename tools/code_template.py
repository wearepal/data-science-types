"""Code taken from pytorch

https://github.com/pytorch/pytorch/blob/385165ec674b764eb42ffe396f98fadd08a513eb/aten/src/ATen/code_template.py
"""
from pathlib import Path
import re
from typing import Optional, Dict, Union, List


ReplacementType = Union[str, int, List[Union[str, int]]]


class CodeTemplate:
    """Match ___identifier___ and replace with value in env

    If this identifier is at the beginning of whitespace on a line and its value is a list then it
    is treated as block subsitution by indenting to that depth and putting each element of the list
    on its own line. If the identifier is on a line starting with non-whitespace and a list
    then it is comma separated. ___foo___, will insert a comma after the list, if the list is not
    empty.
    """

    # Python 2.7.5 has a bug where the leading (^[^\n\S]*)? does not work,
    # workaround via appending another [^\n\S]? inside

    substitution_str = r"(^[^\n\S]*[^\n\S]?)?___([^\d\W]\w*)___(\,?)"

    # older versions of Python have a bug where \w* does not work,
    # so we need to replace with the non-shortened version [a-zA-Z0-9_]*
    # https://bugs.python.org/issue18647

    substitution_str = substitution_str.replace(r"\w", r"[a-zA-Z0-9_]")

    subtitution = re.compile(substitution_str, re.MULTILINE)

    @classmethod
    def from_file(cls, filename: Path) -> "CodeTemplate":
        with filename.open("r") as f:
            return cls(f.read())

    def __init__(self, pattern: str):
        self.pattern = pattern

    @staticmethod
    def indent_lines(indent: str, v: List[Union[str, int]], after: str) -> str:
        return "\n".join([indent + l + after for e in v for l in str(e).splitlines()])  # .rstrip()

    def substitute(
        self, env_: Optional[Dict[str, ReplacementType]] = None, **kwargs: ReplacementType
    ) -> str:
        env = env_ or {}

        def replace(match: "re.Match") -> str:
            indent = match.group(1)
            key = match.group(2)
            trailing_comma = match.group(3)

            # lookup
            v = kwargs[key] if key in kwargs else env[key]

            if indent is not None:
                if not isinstance(v, list):
                    v = [v]
                return self.indent_lines(indent, v, trailing_comma.rstrip())
            elif isinstance(v, list):
                middle = ", ".join([str(x) for x in v])
                if len(v) == 0:
                    return middle
                return middle + trailing_comma
            else:
                return str(v)

        return self.subtitution.sub(replace, self.pattern)


if __name__ == "__main__":
    pattern = """\
    def plot(___text_args___, ___label_args___)
    def bar(
        ___text_args___
        ___label_args___
    )
    def scatter(
        ___text_args___,
        ___label_args___,
    )
    """
    c = CodeTemplate(pattern)
    print(
        c.substitute(
            text_args=["fontsize: int", "tickness: float"],
            label_args=["size: float", "color: str"],
        )
    )
