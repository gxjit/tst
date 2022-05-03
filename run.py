from subprocess import run
from shutil import which


if which("choco"):
    print('yoyo')
    run('choco install upx')