from time import sleep
import shutil
import os

base_dir = os.path.abspath(os.curdir)


def pull(browser_name, vers):
    os.system(f'docker pull selenoid/{browser_name}:{vers}')


def get_sh(browser_name, vers):
    os.system(f'docker run -d --rm --name test selenoid/{browser_name}:{vers}')
    sleep(1)
    os.system(f'docker cp test:/entrypoint.sh {base_dir}\\entrypoints\\entrypoint_{browser_name}{vers}.sh')
    sleep(1)
    os.system('docker stop test')
    sleep(1)


def build(browser_name, vers):
    shutil.copyfile(f'{base_dir}\\entrypoints\\entrypoint_{browser_name}{vers}.sh',
                    f'{base_dir}\\entrypoints\\entrypoint.sh')
    os.system(
        f"docker build -t kannigrand/{browser_name}:{vers} --build-arg VERSION={vers} --build-arg BROWSER={browser_name} .")
    os.remove(f'{base_dir}\\entrypoints\\entrypoint.sh')


if __name__ == '__main__':
    versions_ff = ["79.0", "80.0", "81.0", "82.0", "83.0", "84.0", "85.0", "86.0", "87.0", "88.0", "89.0"]
    versions_ch = ["80.0", "81.0", "83.0", "84.0", "85.0", "86.0", "87.0", "88.0", "89.0", "90.0", "91.0"]
    versions_op = ["72.0", "73.0", "74.0", "75.0", "76.0", "77.0"]

    for x in versions_ff:
        pull("firefox", x)

    for x in versions_ch:
        pull("chrome", x)

    for x in versions_op:
        pull("vnc_opera", x)

    # for x in versions_ff:
    #     get_sh("firefox", x)

    # for x in versions_ch:
    #     build("chrome", x)
    #
    # for x in versions_ff:
    #     build("firefox", x)
