"""Generate pyi files from pyi.in files"""
from pathlib import Path
import json

from tools.code_template import CodeTemplate


def main() -> None:
    variables_path = Path(".") / "matplotlib-stubs" / "shared.json"
    pattern_path = Path(".") / "matplotlib-stubs" / "pyplot.pyi.in"
    output_path = Path(".") / "matplotlib-stubs" / "pyplot.pyi"

    generator = CodeTemplate.from_file(pattern_path)
    with variables_path.open("r") as fp:
        variables = json.load(fp)
    with output_path.open("w") as fp:
        fp.write(generator.substitute(variables))


if __name__ == "__main__":
    main()
