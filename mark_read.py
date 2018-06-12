#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

# please install pytg and telegram-cli before running this script
# pytg: https://github.com/luckydonald/pytg
# telegram-cli: https://github.com/vysheng/tg

import threading
from pytg.sender import Sender
threading.stack_size(65536)

def mark_read(print_name, sender):
    print(">>> Processing " + print_name)
    try:
        sender.mark_read(str(print_name), result_timeout=99999)
    except:
        raise ValueError
    print(">>> Done for " + print_name)

def main():
    sender = Sender(host="localhost", port=4458)
    count = 0
    threads = []
    for i in sender.dialog_list(1000, result_timeout=999999999):
        if str(i.print_name) != '':
            try:
                threads.insert(count, threading.Thread(target=mark_read, args=(i.print_name, sender)))
                threads[count].start()
            except KeyboardInterrupt:
                break
            except:
                pass
            count += 1
    for i in threads:
        i.join()
    print(">>> Total " + str(count + 1) + " dialogs processed.")

if __name__ == '__main__':
    main()
