import datetime
import time

from digits import DIGIT, SEPARATOR
from generator import counter
from print_clock import print_clock, clrscr


if __name__ == '__main__':
    symbol = []
    cntr = counter(2)
    while True:
        clrscr()
        current_time = datetime.datetime.now().strftime('%H%M%S')
        separ = SEPARATOR[next(cntr)]
        # Printing clock
        symbol.append(DIGIT[int(current_time[0])])
        symbol.append(DIGIT[int(current_time[1])])
        symbol.append(separ)
        symbol.append(DIGIT[int(current_time[2])])
        symbol.append(DIGIT[int(current_time[3])])
        symbol.append(separ)
        symbol.append(DIGIT[int(current_time[4])])
        symbol.append(DIGIT[int(current_time[5])])
        print_clock(symbol[::1])
        # Delay
        time.sleep(0.5)
        symbol = []
