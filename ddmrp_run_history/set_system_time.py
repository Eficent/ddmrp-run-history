import subprocess
import shlex
from datetime import datetime


def change_local_system_time(date=False):

    if not date:
        d = raw_input("Enter future date ('YYYY-MM-DD'): ")

    else:
        d = datetime.strptime(date, '%Y-%m-%d')

    # time.strftime("%b %d %Y %H:%M:%S", d)
    subprocess.call(shlex.split("timedatectl set-ntp false"))
    subprocess.call(shlex.split("sudo date -s '%s'" % d))
    # 2 OCT 2006 18:00:00
    subprocess.call(shlex.split("sudo hwclock -w"))

