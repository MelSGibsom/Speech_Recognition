import os
import subprocess

import psutil
import psutil as ps

import speech_recogn

# print(ps.pids())
for proc in psutil.process_iter():
    print(proc.name())

    # if 'Viber' in proc.name():
    #     print(proc.name())
# ps.Popen('chrome')

# subprocess.Popen(['io.elementary.mail'])
# os.system('/home/alexandr/scripts/text_capture.sh')
# subprocess.call(['wmctrl', '-a', 'Viber'])
# subprocess.Popen(['/opt/viber/Viber'])
# subprocess.Popen(['/opt/viber/Viber', '--style', 'Fusion'])
# subprocess.call(['wmctrl', '-a', '/home/alexandr'])
# subprocess.call(['wmctrl', '-a', 'Новий документ'])
print(speech_recogn.processes)