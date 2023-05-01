import subprocess

import psutil
import psutil as ps

# print(ps.pids())
for proc in psutil.process_iter():
    #
    if 'mail' in proc.name():
        print(proc.name())
# ps.Popen('chrome')

subprocess.Popen(['io.elementary.mail'])