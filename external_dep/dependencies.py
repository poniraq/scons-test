import SCons.Script

import shutil
import os.path

import Globals
import build_utils.deps.git
import build_utils.deps.cmake


_repos = [
    ['git@github.com:glfw/glfw.git', '3.3.4', 'deps/glfw']
]

_cmake_builds = [
    ['deps/glfw', 'deps/glfw/build_x86_Debug', {
        'defines': ['GLFW_BUILD_EXAMPLES=0', 'GLFW_BUILD_TESTS=0', 'GLFW_BUILD_DOCS=0']
    }, {
        'glfw-x86-debug': {
            'include': '#deps/glfw/include',
            'libpath': '#deps/glfw/build_x86_Debug/src/Debug',
            'lib': 'glfw3.lib'
        }
    }]
]

def _set_options():
    SCons.Script.AddOption(
        '--purge-deps',
        dest='purge_deps',
        default=False,
        action='store_true',
        help='purge repos & libs',
    )

def _fetch_repos():
    if SCons.Script.GetOption('purge_deps'):
        return

    for [repo, branch, dest] in _repos:
        if os.path.exists(dest):
            continue
        build_utils.deps.git.clone_shallow(repo, branch, dest)

def _build_cmake():
    if SCons.Script.GetOption('purge_deps'):
        return

    for [source, dest, options, exports] in _cmake_builds:
        build_utils.deps.cmake.build(
            source=source,
            dest = dest,
            **options
        )
        for [key, val] in exports.items():
            Globals.Export(key, val)

def _handle_purge():
    if not SCons.Script.GetOption('purge_deps'):
        return

    Globals.Export('purge', True)

    for [_, dest, _, _] in _cmake_builds:
        print(f'Purging {dest} ...')
        shutil.rmtree(dest, ignore_errors=True)

    for [_, _, dest] in _repos:
        print(f'Purging {dest} ...')
        shutil.rmtree(dest, ignore_errors=True)


def init():
    _set_options()
    _fetch_repos()
    _build_cmake()
    _handle_purge()