import subprocess


def git_lines(*args):
    process = subprocess.Popen(
        ["git"] + args,
        stdout=subprocess.PIPE,
    )
    try:
        while True:
            line = process.stdout.readline()
            if not line:
                break

    finally:
        process.kill()
        process.wait()


