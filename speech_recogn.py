import os
import subprocess
import time
import psutil as psutil
import speech_recognition


def run_browser(processes):
    if 'google-chrome-stable' not in processes:
        # subprocess.Popen(['google-chrome-stable'])
        # processes.append(psutil.Process().pid)
        is_running = False
        for proc in psutil.process_iter():
            if proc.name() == 'chrome':
                is_running = True
                break
        if is_running:
            subprocess.call(['wmctrl', '-a', 'Google Chrome'])
        else:
            subprocess.Popen(['google-chrome-stable'])
            processes.append('google-chrome-stable')
    # else:
    #     subprocess.call(['wmctrl', '-a', 'Google Chrome'])


def run_code(processes):
    if 'io.elementary.code' not in processes:
        subprocess.Popen(['io.elementary.code'])
        processes.append('io.elementary.code')
        is_running = False
        for proc in psutil.process_iter():
            if proc.name() == 'io.elementary.code':
                is_running = True
                break
        if is_running:
            subprocess.call(['wmctrl', '-a', 'Новий документ'])
        else:
            subprocess.Popen(['io.elementary.code'])
            processes.append('io.elementary.code')


def run_files(processes):
    if 'io.elementary.files' not in processes:
        # subprocess.Popen(['io.elementary.files'])
        # processes.append('io.elementary.files')
        is_running = False
        for proc in psutil.process_iter():
            if proc.name() == 'io.elementary.files':
                is_running = True
                break
        if is_running:
            subprocess.call(['wmctrl', '-a', '/home/alexandr'])
        else:
            subprocess.Popen(['io.elementary.files'])
            processes.append('io.elementary.files')
    # else:
    #     subprocess.call(['wmctrl', '-a', '/home/alexandr'])


def run_timeshift(processes):
    if 'timeshift-launcher' not in processes:
        # subprocess.Popen(['timeshift-launcher'])
        # processes.append('timeshift-launcher')
        is_running = False
        for proc in psutil.process_iter():
            if proc.name() == 'timeshift-launc2':
                is_running = True
                break
        if is_running:
            subprocess.call(['wmctrl', '-a', 'Timeshift'])
        else:
            subprocess.Popen(['timeshift-launcher'])
            processes.append('timeshift-launcher')
    # else:
    #     subprocess.call(['wmctrl', '-a', 'Запит автентифікації'])


def run_settings(processes):
    if 'io.elementary.switchboard' not in processes:
        # subprocess.Popen(['io.elementary.switchboard'])
        # processes.append('io.elementary.switchboard')
        is_running = False
        for proc in psutil.process_iter():
            if proc.name() == 'io.elementary.switchboard':
                is_running = True
                break
        if is_running:
            subprocess.call(['wmctrl', '-a', 'Налаштування системи'])
        else:
            subprocess.Popen(['io.elementary.switchboard'])
            processes.append('io.elementary.switchboard')
    # else:
    #     subprocess.call(['wmctrl', '-a', 'Налаштування системи'])


def text_recognition(processes):
    if 'text_capture.sh' not in processes:
        os.system('/home/alexandr/scripts/text_capture.sh')
        processes.append('text_capture.sh')
    else:
        subprocess.call(['wmctrl', '-a', 'Tiny Beast (online)'])


def run_app_center(processes):
    if 'io.elementary.appcenter' not in processes:
        # subprocess.Popen(['io.elementary.appcenter'])
        # processes.append('io.elementary.appcenter')
        is_running = False
        for proc in psutil.process_iter():
            if proc.name() == 'io.elementary.appcenter':
                is_running = True
                break
        if is_running:
            subprocess.call(['wmctrl', '-a', 'Центр застосунків'])
        else:
            subprocess.Popen(['io.elementary.appcenter'])
            processes.append('io.elementary.appcenter')
    # else:
    #     subprocess.call(['wmctrl', '-a', 'Центр застосунків'])


def run_search(processes):
    if 'fsearch' not in processes:
        # subprocess.Popen(['fsearch'])
        # processes.append('fsearch')
        is_running = False
        for proc in psutil.process_iter():
            if proc.name() == 'fsearch':
                is_running = True
                break
        if is_running:
            subprocess.call(['wmctrl', '-a', 'FSearch'])
        else:
            subprocess.Popen(['fsearch'])
            processes.append('fsearch')
    # else:
    #     subprocess.call(['wmctrl', '-a', 'FSearch'])


def run_snapstore(processes):
    if 'snap-store' not in processes:
        # subprocess.Popen(['snap-store'])
        # processes.append('snap-store')
        is_running = False
        for proc in psutil.process_iter():
            if proc.name() == 'snap-store':
                is_running = True
                break
        if is_running:
            subprocess.call(['wmctrl', '-a', 'Програми'])
        else:
            subprocess.Popen(['snap-store'])
            processes.append('snap-store')
    # else:
    #     subprocess.call(['wmctrl', '-a', 'Програми'])


def run_terminal(processes):
    if 'io.elemenatary.terminal' not in processes:
        # subprocess.Popen(['io.elementary.terminal'])
        # processes.append('io.elementary.terminal')
        is_running = False
        for proc in psutil.process_iter():
            if proc.name() == 'io.elementary.terminal':
                is_running = True
                break
        if is_running:
            subprocess.call(['wmctrl', '-a', 'alexandr@IdeaPad-3-14ITL6-6394927f'])
        else:
            subprocess.Popen(['io.elementary.terminal'])
            processes.append('io.elementary.terminal')
    # else:
    #     subprocess.call(['wmctrl', '-a', 'alexandr@IdeaPad-3-14ITL6-6394927f'])


def run_telegram(processes):
    if '/home/alexander/Загрузки/Telegram/Telegram' not in processes:
        # subprocess.Popen(['/home/alexandr/Загрузки/Telegram/Telegram'])
        # processes.append('/home/alexandr/Загрузки/Telegram/Telegram')
        is_running = False
        for proc in psutil.process_iter():
            if proc.name() == 'Telegram':
                is_running = True
                break
        if is_running:
            subprocess.call(['wmctrl', '-a', 'Telegram (84233)'])
        else:
            subprocess.Popen(['/home/alexandr/Загрузки/Telegram/Telegram'])
            processes.append('/home/alexandr/Загрузки/Telegram/Telegram')
    # else:
    #     subprocess.call(['wmctrl', '-a', 'Telegram (84233)'])
def run_mail(processes):
    if 'io.elementary.mail' not in processes:
        subprocess.Popen(['io.elementary.mail'])
        # processes.append('io.elementary.mail')
        is_running = False
        for proc in psutil.process_iter():
            if proc.name() == 'io.elementary.mail':
                is_running = True
                break
        if is_running:
            subprocess.call(['wmctrl', '-a', 'Пошта'])
        else:
            subprocess.Popen(['io.elementary.mail'])
            processes.append('io.elementary.mail')
    # else:
    #     subprocess.call('wmctrl', '-a', 'Пошта')


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

processes = []  # список запущенных процессов

while True:
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        try:
            query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
            print(f"Вы сказали: {query}")
            if query == 'открой браузер':
                run_browser(processes)
            elif query == 'открой блокнот':
                run_code(processes)
            elif query == 'открой файлы':
                run_files(processes)
            elif query == 'создать точку восстановления':
                run_timeshift(processes)
            elif query == 'открой настройки':
                run_settings(processes)
            elif query == 'скопируй':
                text_recognition(processes)
            elif query == 'открой центр приложений':
                run_app_center(processes)
            elif query == 'открой поиск':
                run_search(processes)
            elif query == 'открой снэп':
                run_snapstore(processes)
            elif query == 'открой терминал':
                run_terminal(processes)
            elif query == 'открой telegram':
                run_telegram(processes)
            elif query== 'почта':
                run_mail(processes)


        except:
            print("Ошибка при распознавании голоса")
            time.sleep(1)
    # Удаляем процессы, которые уже закрыты
    for p in processes:
        if p not in [proc.name() for proc in psutil.process_iter()]:
            processes.remove(p)

    time.sleep(1)
