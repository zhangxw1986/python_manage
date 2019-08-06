#! /usr/bin/env python
# -*- coding:utf-8 -*-

from collections import namedtuple

str = '''major_number minor_number device_name read_count read_merged_count read_sections
         time_spent_reading write_count write_merged_count write_sections time_spent_write io_requests
         time_spent_doing_io weighted_time_spent_doing_io
        '''
Disk = namedtuple('diskinfo', str)


def get_task_info(device):
    with open('/proc/diskstats') as f:
        for line in f:
            if device in line.split()[2]:
                yield Disk(*(line.split()))
    raise RuntimeError("device ({0}) not found !".format(device))


def main():
    for disk_info in get_task_info("sda"):
        print(disk_info)
        print('磁盘写次数：{0}'.format(disk_info.write_count))
        print('磁盘写字节数：{0}'.format(int(disk_info.write_sections)*512))
        print('磁盘写延时：{0}'.format(disk_info.time_spent_write))


if __name__ == "__main__":
    main()
