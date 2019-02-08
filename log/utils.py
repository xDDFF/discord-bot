import time
import os
from subprocess import call

t = time.localtime(time.time())
PATH = '/home/user/discord-bot/log/git.log'
DATE = ('[' + str(t.tm_mon) + '-' + str(t.tm_mday) + '-' + str(t.tm_year) + ']')
TIME = ('[' + str(t.tm_hour) + ':' + str(t.tm_min) + ']')

def check_log_file():
	if(os.path.exists(PATH) == False):
        	print('LOG file does not exists....')
        	print('Creating file [%s]' % (PATH))
        	f = open(PATH, 'w+')
        	f.write('############ git.log #############\n')
        	f.close()
	
def write_log(arg):
	f = open(PATH, 'a+')
	f.write(DATE + ' ' + TIME + '-- [commit submitted] ' + '[' + arg + ']\n')
	f.close()

