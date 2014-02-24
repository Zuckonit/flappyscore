#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import optparse
import flappyscore

def opt(arg):
    parser = optparse.OptionParser(usage="usage: %prog -s score [-f] [save_file]")
    parser.add_option( "-s", "--score", dest="score", type="long", help="the score to be generated")
    parser.add_option( "-o", "--output", dest="output", type="string", help="the image to be saved")
    (options, args) = parser.parse_args(arg)
    if len(arg) == 0 or options.score is None:
        parser.error('score required')
    flappyscore.generate(options.score, options.output)

if __name__ == '__main__':
    opt(sys.argv)
