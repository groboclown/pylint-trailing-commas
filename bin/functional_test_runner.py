# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/groboclown/pylint-trailing-commas/blob/main/LICENSE
# Copyright (c) https://github.com/groboclown/pylint-trailing-commas/blob/main/CONTRIBUTORS.txt

"""Functional full-module tests for PyLint trailing-commas."""
import sys
from pathlib import Path
from typing import Union

import pytest
from _pytest.config import Config
from _pytest.recwarn import WarningsRecorder

from pylint import testutils
from pylint.testutils import UPDATE_FILE, UPDATE_OPTION
from pylint.testutils.functional import (
    FunctionalTestFile,
    LintModuleOutputUpdate,
    get_functional_test_files_from_directory,
)

sys.path.append(str(Path(__file__).parent.parent.resolve()))

FUNCTIONAL_DIR = Path(__file__).parent.resolve() / '..' / "functional_tests"

TESTS = [
    t
    for t in get_functional_test_files_from_directory(FUNCTIONAL_DIR)
]
TESTS_NAMES = [t.base for t in TESTS]


@pytest.mark.parametrize("test_file", TESTS, ids=TESTS_NAMES)
def test_functional(
    test_file: FunctionalTestFile, recwarn: WarningsRecorder, pytestconfig: Config
) -> None:
    __tracebackhide__ = True  # pylint: disable=unused-variable
    pytestconfig.option.minimal_messages_config = True
    if UPDATE_FILE.exists():
        lint_test: Union[
            LintModuleOutputUpdate, testutils.LintModuleTest
        ] = LintModuleOutputUpdate(test_file, pytestconfig)
    else:
        lint_test = testutils.LintModuleTest(test_file, pytestconfig)
    lint_test.setUp()
    lint_test.runTest()
    warning = None
    try:
        # Catch <unknown>:x: DeprecationWarning: invalid escape sequence,
        # so, it's not shown during tests
        warning = recwarn.pop()
    except AssertionError:
        pass
    if warning is not None:
        if sys.version_info.minor > 5:
            assert issubclass(warning.category, DeprecationWarning)
            assert "invalid escape sequence" in str(warning.message)


if __name__ == "__main__":
    if UPDATE_OPTION in sys.argv:
        UPDATE_FILE.touch()
        sys.argv.remove(UPDATE_OPTION)
    try:
        pytest.main(sys.argv)
    finally:
        if UPDATE_FILE.exists():
            UPDATE_FILE.unlink()
