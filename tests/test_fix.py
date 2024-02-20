import os
import pytest
import sys

from cdk_integ_runner_cwd_fix import fix_cwd

def test_fix_cwd_empty_env_var():
    with pytest.raises(KeyError):
        fix_cwd()

def test_fix_cwd():
    required_cwd = '/tmp'

    # Check we are not already in the required cwd
    assert os.getcwd() != required_cwd

    # Set the environment variable
    os.environ['CDK_INTEG_RUNNER_CWD'] = required_cwd
    # Call the function to set the cwd
    fix_cwd()

    # Check we are now in the required cwd
    assert os.getcwd() == required_cwd

    # Check the required cwd is at the start of sys.path
    assert sys.path[0] == required_cwd
