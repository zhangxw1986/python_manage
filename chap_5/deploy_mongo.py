#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import shutil
import tarfile
import subprocess


def execute_cmd(cmd):
    p = subprocess.Popen(
        cmd,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout


def unpackge_mongo(package, package_dir):
    unpackage_dir = os.path.splitext(package)[0]
    if os.path.exists(unpackage_dir):
        shutil.rmtree(unpackage_dir)
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    t = tarfile.open(package, 'r:gz')
    t.extractall('.')

    shutil.move(unpackage_dir, package_dir)


def create_datadir(datadir):
    if os.path.exists(datadir):
        shutil.rmtree(datadir)
    os.mkdir(datadir)


def format_mongo_command(pack_dir, data_dir, logfile):
    mongod = os.path.join(pack_dir, 'bin', 'mongod')
    mongod_format = '{0} --fork --dbpath {1} --logpath {2}'
    return mongod_format.format(mongod, data_dir, logfile)


def start_mongod(cmd):
    returncode, out = execute_cmd(cmd)
    if returncode != 0:
        raise SystemExit('execute {0} error: {1}'.format(cmd, out))
    else:
        print('execute cmd ({0}) successful.'.format(cmd))


def main():
    package = 'mongodb-linux-x86_64-rhel62-4.0.10.tgz'
    cur_dir = os.path.abspath('.')
    package_dir = os.path.join(cur_dir, 'mongo')
    data_dir = os.path.join(cur_dir, 'mongodata')
    logfile = os.path.join(data_dir, 'mongod.log')

    if not os.path.exists(package):
        raise SystemExit('{0} not found.'.format(package))

    unpackge_mongo(package, package_dir)
    create_datadir(data_dir)
    start_mongod(format_mongo_command(package_dir, data_dir, logfile))


if __name__ == "__main__":
    main()
