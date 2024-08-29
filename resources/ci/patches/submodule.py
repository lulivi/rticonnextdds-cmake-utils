#!/usr/bin/env python3
#
# (c) 2024 Copyright, Real-Time Innovations, Inc.  All rights reserved. RTI
# grants Licensee a license to use, modify, compile, and create derivative
# works of the Software.  Licensee has the right to distribute object form only
# for use with RTI products.  The Software is provided "as is", with no
# warranty of any type, including any warranty for fitness for any purpose. RTI
# is under no obligation to maintain or support the Software.  RTI shall not be
# liable for any incidental or consequential damages arising out of the use or
# inability to use the software.
"""Apply the submodule patch.

Script parameters:

- ``--cmake-utils-root``: rticonnextdds-cmake-utils repository root directory.
- ``--examples-root``: rticonnextdds-examples repository root directory.
"""

import argparse
import shutil
from pathlib import Path
import subprocess


def main():
    args: argparse.Namespace = parse_args()

    print("Applying submodule patch:")

    print(
        "- Dump the contents of the rticonnextdds-cmake-utils repository into its submodule"
        " location inside the rticonnextdds-examples repository"
    )
    copy_tree(
        source=args.cmake_utils_root,
        target=args.examples_root.joinpath("resources", "cmake", "rticonnextdds-cmake-utils"),
    )

    print("- Apply a minor git patch to the file `ConnextDdsConfigureCmakeUtils.cmake`")
    subprocess.run(
        [
            "git",
            "-C",
            str(args.examples_root),
            "apply",
            str(Path(__file__).resolve().with_suffix(".diff")),
        ]
    )


def parse_args() -> argparse.Namespace:
    """Parse the CLI options."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cmake-utils-root",
        type=Path,
        required=True,
        help="Path to the rticonnextdds-cmake-utils repository",
    )
    parser.add_argument(
        "--examples-root",
        type=Path,
        required=True,
        help="Path to the rticonnextdds-examples repository",
    )
    args = parser.parse_args()
    args.cmake_utils_root = args.cmake_utils_root.resolve()
    args.examples_root = args.examples_root.resolve()

    return args


def copy_tree(source: Path, target: Path) -> None:
    def copy_file(source_file: Path, target_dir: Path) -> None:
        target_file = target_dir.joinpath(source_file.name)

        if target_file.exists():
            target_file.unlink()

        shutil.copy(source_file, target_file)

    target.mkdir(parents=True, exist_ok=True)

    if source.is_file():
        copy_file(source_file=source, target_dir=target)
        return

    for child in filter(lambda child: child.name != ".git", source.iterdir()):
        if child.is_file():
            copy_file(source_file=child, target_dir=target)
        else:
            copy_tree(source=child, target=target.joinpath(child.name))


if __name__ == "__main__":
    main()
