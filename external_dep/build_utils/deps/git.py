import platform
import subprocess
import shutil
import stat
import os
import os.path as path

from build_utils import execute

Shell = 'powershell.exe' if platform.system() == 'Windows' else 'bash'

#from: https://stackoverflow.com/questions/4829043/how-to-remove-read-only-attrib-directory-with-python-in-windows
def _on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

def _unhide_dir(dir):
    if platform.system() != 'Windows': return
    subprocess.call(['attrib', '-H', dir])

def clone_shallow(repo, branch, dest):
    execute(f'git clone --depth 1 --branch {branch} {repo} {dest}')
    
    # unhide & remove .git folder
    # it is unnecessary + it causes problems on cleanup
    git_folder = path.join(dest, '.git')
    _unhide_dir(git_folder)
    shutil.rmtree(git_folder, onerror=_on_rm_error)