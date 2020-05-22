"""Generate pyi files from pyi.in files"""
from pathlib import Path
import json

from tools.code_template import CodeTemplate

WARNING_STR = """# ========================================================= #
#      This file has been generated automatically!!!!
#                     DO NOT EDIT IT!
# ========================================================= #
"""


def main() -> None:
    variables_path = Path(".") / "matplotlib-stubs" / "shared.json"
    pattern_path = Path(".") / "matplotlib-stubs" / "pyplot.pyi.in"
    output_path = Path(".") / "matplotlib-stubs" / "pyplot.pyi"

    generator = CodeTemplate.from_file(pattern_path)
    with variables_path.open("r") as fp:
        variables = json.load(fp)
    with output_path.open("w") as fp:
        fp.write(WARNING_STR + generator.substitute(variables))


if __name__ == "__main__":
    main()
