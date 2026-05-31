import time
import os
import sys
from datetime import datetime, timedelta

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_timer(minutes, seconds, phase):
    clear_screen()
    if phase == 'work':
        emoji = '>:('
        phase_name = 'УЧЕБА/КОДИНГ'
    else:
        color = '\033[94m'
        emoji = ';)'
        phase_name = 'ОТДЫХ'
    
    reset = '\033[0m'

    print(f'\n{'='*50}')
    print(f'{color}  {phase_name} {emoji}{reset}')
    print(f'{'='*50}')
    print(f'\n    Осталось времени: {color}{minutes:02d}:{seconds:02d}{reset}\n')

    # Прогресс-бар
    total_seconds = 40*60 if phase == 'work' else 10 * 60
    current_seconds = minutes*60 + seconds
    percent = (total_seconds - current_seconds)/total_seconds
    bar_length = 30
    filled = int(bar_length*percent)
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f'[{bar}]{int(percent*100)}%\n')
    print(f'{'='*50}')

def pomodoro(work_min=40, break_min=10, cycles=4):
    '''
    Запускает помидоро-таймер 
    work_min: минут работы
    break_min: минут отдыха
    cycles: количество циклов
    ''' 
    print('\n  ЗАПУСКАЕМ ПОМИДОРО-ТАЙМЕР!')
    print(f' Учеба:{work_min} мин| Отдых:{break_min}мин')
    print(f' Количество циклов:{cycles}\n')
    print('Нажми Ctrl+C для выхода в любой момент\n')

    input("Нажми Enter, чтобы начать первый цикл...")

    for cycle in range(1, cycles + 1):
        print(f'\n Цикл{cycle} из {cycles} - начинаем')

        work_seconds = work_min * 60
        for remaining in range(work_seconds, 0, -1):
            mins = remaining // 60
            secs = remaining % 60
            print_timer(mins, secs, 'work')
            time.sleep(1)

        print('\a')
        print(f'\n {work_min} минут учебы завершены')

        if cycle < cycles:
            print(f'\n перерыв {break_min} минут')
            input("нажми Enter, чтобы начать отдых...")

            break_seconds = break_min * 60
            for remaining in range(break_seconds, 0, -1):
                mins = remaining // 60
                secs = remaining % 60
                print_timer(mins, secs, 'break')
                time.sleep(1)

            print('\a')
            print(f'\n Перерыв окончен. Готов к следующему циклу?')
            input('Нажми Enter для продолжения...')
        else:
            print(f'\n Ты завершил {cycles} циклов учебы!')
            print('Так держать!\n')

if __name__ == '__main__':
    try:
        pomodoro(work_min=40, break_min=10, cycles=4)
    except KeyboardInterrupt:
        print("\n\n Пока! Таймер остановлен. Возвращайся к учебе!")
        sys.exit(0)