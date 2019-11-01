#!/usr/bin/env python3
import os
import shutil
import pathlib
import requests
import argparse

parser = argparse.ArgumentParser(description='Runs Kattis problem through their test cases')
parser.add_argument('--id', type=str, default='_NONE_', help='id of problem to fetch')
args = parser.parse_args()
qid = args.id

if qid == '_NONE_':
    qid = input('Enter ID: ')
qdir = os.getcwd() + '/' + qid
ilen = int((len([name for name in os.listdir(qdir) if os.path.isfile(os.path.join(qdir, name))]) -1) / 2)

os.system('g++ ' + qdir + '/_' + qid + '.cpp')

for i in range(ilen):
    print('TEST CASE ' + str(i+1))
    output = os.popen('cat ' + qdir + '/input' + str(i+1) + ' | ./a.out').read().rstrip()
    if output == open(qdir + '/output' + str(i+1)).read().rstrip():
        print('PASSED')
    else:
        print('FAILED')