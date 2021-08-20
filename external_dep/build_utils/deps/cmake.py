from build_utils import execute

_CMAKE = 'cmake'

def build(**options):
    """
    Builds CMake project

    Parameters:
        cmake: optional cmake path
        source: CMake project path
        dest: build destination folder
        defines: optional CMake defines for the project

    Returns:
        build(): none
    """

    cmake: str = '"%s"' %(options.get('cmake', _CMAKE))
    source: str = options.get('source')
    dest: str = options.get('dest')

    defines: list = options.get('defines', [])
    defines_str: str = ' '.join(map(lambda d: f'-D{d}', defines))

    cmake_options: str = f'{defines_str}'

    config_cmd: str = f'{cmake} -S {source} -B {dest} {cmake_options}'
    build_cmd: str = f'{cmake} --build {dest}'

    execute(config_cmd)
    execute(build_cmd)
