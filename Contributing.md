## **Information about pre-commit** currently not active

If you want to contribute to the project, do not forget to pre-format your code with the help of pre-commit, for this you must install the configurations by typing
the following command:

```bash
pre-commit install
```

The above will ensure that before your commit is loaded, it will verify that your implemented code complies with certain standards and rules.


If you want to check all the code

```bash
pre-commit run --all-files
```

if you want to commit him without pre-commit Warning

```bash
git commit -m "fix: lakdsljflaksjdlkf"  --no-verify
```