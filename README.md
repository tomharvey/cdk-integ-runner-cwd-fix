# CDK integ-runner CWD Fix

[![PyPI version](https://badge.fury.io/py/cdk-integ-runner-cwd-fix.svg)](https://badge.fury.io/py/cdk-integ-runner-cwd-fix)

When running integ-test on python, the CWD is set to the directory which
contains your test file - not the directory youre running your tests from.

It also changes PYTHONPATH, so your test file has no access to the stacks you create.
Instead, you get a lot of ModuleNotFoundError when you try to import your stacks into
the test case.

That also breaks the lambda (and likely other) builds which rely on a path.
So, if you're using `Code.from_asset("./lambda")` you should start using
`Code.from_asset(f"{os.getcwd()}/lambda")` instead, after using this fix.

This realtive path issue is likely to be applicable to other constructs that rely on
a relative path and you can use a similar fix to work around it.

This is a workaround to fix the CWD and PYTHONPATH so that your test file
can import your stacks and run the integ tests.

Maybe at some point this will be fixed in the CDK integ-runner, but for now this will get you
up and running. integ-runner is a developer preview, so it's expected to have weirdnesses.

## Usage

### Installation

``` bash
pip install cdk-integ-runner-cwd-fix
```


### In your code

Then, in your test file, add the following lines:

```python
from cdk_integ_runner_cwd_fix import fix_cwd

fix_cwd()

# You can now import your stack
from my_cdk_project.my_stack import MyStack

# And write your test code here
app = cdk.App()
stack = MyStack(app, "TestStack")

app.synth()
```

### Running tests

You'll need to set the project path in the environment variable `CDK_INTEG_RUNNER_CWD`:

The below will set it to your current directory - which is likely to be what you need:

```bash
export CDK_INTEG_RUNNER_CWD=$(pwd)
```

or to be explicit, or to set it to something other than the path you're currently in:

```bash
export CDK_INTEG_RUNNER_CWD=/path/to/your/cdk/project
```

Then, run your tests as usual:

```bash
integ-runner
```