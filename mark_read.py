#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

# please install pytg and telegram-cli before running this script
# pytg: https://github.com/luckydonald/pytg
# telegram-cli: https://github.com/vysheng/tg

from pytg.sender import Sender

def main():
    sender = Sender(host="localhost", port=4458)
    count = 0
    for i in sender.dialog_list(1000, result_timeout=999999999):
        count += 1
        if str(i.print_name) != '':
            print(">>> Processing " + i.print_name)
            try:
                sender.mark_read(str(i.print_name), result_timeout=99999)
            except KeyboardInterrupt:
                break
            except:
                pass
    print(">>> Total " + str(count) + " dialogs processed.")

if __name__ == '__main__':
    main()
