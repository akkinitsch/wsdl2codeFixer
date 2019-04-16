#!/usr/bin/env python

import argparse
import re

regex_seperated_line = re.compile(r'\+')

def read_input_file(inputfile):
    f = open(inputfile, 'r')
    return f.readlines()

def write_output_file(outputfile, lines):
    o = open(outputfile, 'w')
    o.writelines(lines)
    o.close()

def fix_seperated_lines(lines):
    counter = 0
    result = []
    counter_lines = len(lines)
    while counter < counter_lines:
        if re.search('.*\+', lines[counter]):
            tmp = lines[counter].rstrip() + lines[counter+1]
            result.append(tmp)
            counter = counter + 2
        else:
            result.append(lines[counter])
            counter = counter + 1
    return result

def replace_reply_action(line):
    l = line
    m = re.search('\[.*Attribute\(Action="(.+?)"( \+        \"\")*, ReplyAction="\*"\)\]', l)
    if m:
        found = m.group(1)
        l = l.replace('ReplyAction="*"', 'ReplyAction="' + found + '"')
    return l

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputfile", help="Inputfile that should be fixed.", required=True)
    parser.add_argument("--outputfile", help="Outputfile that should be written.", default = None)
    args = parser.parse_args()
    lines = read_input_file(args.inputfile)
    seperate_lines_fixed = fix_seperated_lines(lines)
    result = []
    for line in seperate_lines_fixed:
        result.append(replace_reply_action(line))
    if args.outputfile:
        write_output_file(args.outputfile, result)
    else:
        write_output_file(args.inputfile, result)
