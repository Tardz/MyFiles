#!/usr/bin/env python3
"""
Unit testing using asserts for lab 2

Note:
If you have downloaded the scripts from the website it might not
have the access right. To solve this run:
$ chmod +x <path_to_test_2.py>

Usage (case insensitive for parameters to --test):
$ ./test_2.py <path_to_lab>
to test whole lab 2

Initial version by Erik Hansson <erik.b.hansson@liu.se>

Updated for TDDE23 by Frans Skarman <frask812@student.liu.se>

Changelog:
 * 31/8-2016: Updated the printed traceback in case that the given file
   can not be imported.
"""

from argparse import ArgumentParser
from importlib.machinery import SourceFileLoader
from traceback import format_exc
import sys


def test_check_pnr():
    """
    Tests the check pnr function
    """
    personal_id_ok = [7, 4, 0, 2, 1, 7, 4, 8, 2, 0]
    personal_id_fail = [7, 4, 0, 2, 1, 7, 4, 8, 2, 1]

    assert (
        lab1.check_pnr(personal_id_ok) is True
    ), "expected that [7, 4, 0, 2, 1, 7, 4, 8, 2, 0] returned True got " + str(
        lab1.check_pnr(personal_id_ok)
    )
    assert (
        lab1.check_pnr(personal_id_fail) is False
    ), "expected that [7, 4, 0, 2, 1, 7, 4, 8, 2, 1] returned False got " + str(
        lab1.check_pnr(personal_id_fail)
    )
    assert (
        lab1.check_pnr([9, 5, 0, 9, 0, 8, 5, 5, 5, 2]) is True
    ), "expected that [9, 5, 0, 9, 0, 8, 5, 5, 5, 2] returned True got " + str(
        lab1.check_pnr([9, 5, 0, 9, 0, 8, 5, 5, 5, 2])
    )

    # Issue 117
    # Must have two separate declarations here so we get two separate lists!
    # One might be changed...
    orig_pnr = [9, 5, 0, 9, 0, 8, 5, 5, 5, 2]
    good_pnr = [9, 5, 0, 9, 0, 8, 5, 5, 5, 2]
    lab1.check_pnr(orig_pnr)
    assert good_pnr == orig_pnr, (
        "expected check_pnr to leave its argument unchanged, but calling "
        + "check_pnr("
        + str(orig_pnr)
        + ") changed the argument list to "
        + str(good_pnr)
    )


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("file")
    args = arg_parser.parse_args()
    if args.file.rfind("/") != -1:
        sys.path.append(args.file[: args.file.rfind("/")])
        potential_name = args.file[args.file.rfind("/") + 1 :]
    else:
        sys.path.append(".")
        potential_name = args.file
    if potential_name.rfind("."):
        name = potential_name[: potential_name.rfind(".")]
    else:
        name = potential_name
    try:
        lab1 = SourceFileLoader(name, args.file).load_module()
    except (FileNotFoundError):
        print("Could not import lab: " + args.file)
        print("See traceback for further information:")
        print()

        stack_trace = format_exc().split("\n")
        importlib_has_started = False
        importlib_has_ended = False
        for line in stack_trace:
            if (
                not importlib_has_ended
                and importlib_has_started
                and line.lstrip().startswith("File")
                and "importlib" not in line
            ):
                importlib_has_ended = True
            if importlib_has_ended:
                print(line)
            elif (
                not importlib_has_started
                and line.lstrip().startswith("File")
                and "importlib" in line
            ):
                importlib_has_started = True
        exit(1)

    test_check_pnr()

    print("The code passed all the tests")