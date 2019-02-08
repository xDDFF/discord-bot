#!/usr/bin/env python3
import os
import sys
import subprocess

subprocess.call(['docker', 'build', '-t', 'user/discord', '.'])
subprocess.call(['docker', 'run', '-ti', 'user/discord'])

#clean up after the build
#subprocess.call(['docker', 'image', 'prune', '-af'])
subprocess.call(['docker', 'container', 'prune', '-f'])

