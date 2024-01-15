# PyLint Extension - Trailing Commas

Adds a consistent format to force commas at the end of lines, even for the last items.  It makes your code look a bit like Golang, if you're into that kind of thing.


## What It Does

The [extension](trailing_commas.py) is a single Python file that works with PyLint to identify places in your code where you lack a trailing comma on list-like expressions.

It encourages a coding style like:

```python
def my_func(
        arg_1,
        arg_2,
):
    # Lists, tuples, dictionaries, sets, and function arguments, if multi-line,
    # need to include a comma after the last item.
    x = [
        "a",
        "b-c",
        "d-e-f",
    ]
    # list constructor expressions are recognized and don't need a comma.
    y = [
        value.upper()
        for value in x
    ]
    if (
        # if, elif, and other multi-line statements that aren't lists are
        # identified as such, and don't need a trailing comma
        len(arg_1) > 1 and
        len(arg_2) < 10
    ):
        return x
    # Returning items on the same line is fine, and you can use the option
    # 'comma-always-after-last-tuple' to require tuples to have a final
    # comma.
    return (len(x), len(y), "string-value",)
```

This has two options that can be set:

* `comma-always-after-last-tuple` : set to "y" or "n".  If set, then a comma is always required after the last item in a tuple, regardless of whether it is multi-line or not.  The linter makes a best effort to discover whether a parenthetical expression is a tuple or not.
* `one-item-per-line` : set to "y" or "n".  If set, then the extension reports a problem if a multi-line list has more than one item on a line.


## How To Use

*For those using PyLint version 2, use the `pylint-v2` branch.*

You need to add the directory where you store the [extension](trailing_commas.py) into your `PYTHONPATH` environment variable, and load the plugin with the PyLint execution.

To load it through a command-line argument:

```bash
python3 -m pylint \
    --load-plugins trailing_commas \
    my_packages to_lint
```

If you can't easily add it to the `PYTHONPATH`, then use (replace `build-src` with the directory containing this file):

```bash
python3 -m pylint \
     '--init-hook=sys.path.append("build-src")' \
     --load-plugins trailing_commas \
     my_packages to_lint
```

These can be added to your `pylintrc` file:

```ini
[MASTER]
load-plugins=trailing_commas
init-hook=sys.path.append("build-src")

# To set the extension's options, these can also be set in the rc file
[trailing_commas]
comma-always-after-last-tuple=n
```


## Filing a Bug

If you find a bug, please file it in the issues section.  It's even better if you include a sample of the code in question that should cause the specific output but doesn't.  Even better if you include a pull request that includes the test for the failure.


## Contributing

If you would like to contribute code to the project, you must first accept that the contribution will be under the [license](#license).  Then, you must ensure you have proper test coverage.

Please note that the project aims to keep the extension to a single file, to make usage much easier.


## Releasing

Releases of the project involves:

1. Ensure all tests pass and the code style works as expected.
2. Changing the version number in the [extension](trailing_commas.py) file's comment.
3. Creating a release in the GitHub project with a correspondingly named tag (vA.B)
4. Include the [extension](trailing_commas.py) as a release artifact with the release.


## License

Because this directly references the PyLint code, which is itself under the GPL v2 license, this must be released under the [GPLv2 license](LICENSE).

Under this license, this extension applies the GPL to the extension itself, which is only used when run as part of PyLint.  Therefore, it can be included in your project without triggering the viral clause.


## A Bit of History

This started out as a bit of code stuck into a Gist, but the need for samples to test against quickly out-grew the scope of a Gist.  So, here we are.
