import os
import sys

def fix_cwd(prepend_to_sys_path: bool = True):
    required_cwd = _get_required_cwd()

    os.chdir(required_cwd)

    if prepend_to_sys_path:
        sys.path.insert(0, required_cwd)


def _get_required_cwd() -> str:
    try:
        return os.environ['CDK_INTEG_RUNNER_CWD']
    except KeyError:
        raise KeyError('CDK_INTEG_RUNNER_CWD environment variable is not set')