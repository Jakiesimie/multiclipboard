#!/usr/bin/python
# multiclipboard.pyw
#-*- coding: utf-8 -*-
#
#
# Author: Wojciech Dudek
# e-mail: wdudek82@.gmail.com

import sys
import pyperclip
import shelve


# Displays short decription of multiclipboard
# and every available option
def mcb_help():
	print '{0}\nMultiClipboard v0.1\n{0}'.format('='*19)
	print '\nTool for storing multiple clipboards\n{}'.format('='*36)
	print '\n{:>4}...short decription...\n'.format('')
	print 'Synppsis:\n'
	print '{:>4}mcb [option] [key name]'.format('')
	print '\nOptions:\n'
	print '{:>4}help - blablabla\n'.format('')
	print '{:>4}save - saves current clipboard under auto-generated key-name...\n'.format('')
	print '{:>4}save [name] - saves current clipboard under choosen key-name...\n'.format('')
	print '{:>4}[name] - load saved clipboard\n'.format('')
	print '{:>4}list - lists every saved clipboard in mcb.dat file\n'.format('')
	print '{:>4}delete - remove selected key-name from mcb.dat...\n'.format('')
	print '{:>4}clear - remove all keys from mcb.dat...\n'.format('')

# Lists every saved clipboard in mcb.dat file
def list_mcb(file):
	print '\nSaved clipboards:\n{0}\n'.format('-' * 17)

	for i, k in enumerate(file.keys()):
		print '{:>4}. {}'.format(i+1, k)

	if not file.keys():
		print '{:>4}- none -'.format('')

	print

# Saves current clipboard under choosen key-name.
# If key-name was not specified, it prompts user to
# type one or use generated number.
def save_mcb(file):
	# If there is none sys.argv[2], then key-name is generated
	# by concatenating 'clipboard' with number from 1 to 100
	try:
		key = sys.argv[2]
	except IndexError:
		for i in xrange(1, 100):
			name = '{:02d}'.format(i)
			if name not in file:
				key = name
				break

	try:
		file[key] = pyperclip.paste()
		print '* Clipboard saved as "{}"\n'.format(key)
	except UnboundLocalError:
		print '* No more spare auto-generated clipboard names!\n'
		print '* Delete some entries or use custom names.'

# Loads choosen clipboard from mcb.dat if such selected key exists
def load_mcb_item(file, item):
	try:
		pyperclip.copy(file[item])
		print '* Clipboard "{}" was loaded successfully!\n'.format(item)

		# Just for test!!
		print file[item]
	except KeyError:
		print '* Clipboard "{}" was not found...\n'.format(item)

# Remove selected key-name from mcb.dat
def delete_mcb_item(file, item):
	del_item = file.pop(item, None)
	print '* Clipboard "{}" removed successfully!\n'.format(item) \
		if del_item \
		else '* Clipboard "{}" not found...\n'.format(item)

# Remove all keys from mcb.dat
def clear_mcb(file):
	prompt = raw_input('* All saved clipboards will be removed - procede? [y/n]: ') or 'space'

	while 1:
		if prompt[0].lower() == 'y':
			file.clear()
			print '* All saved clipboards were removed!\n'
			break
		elif prompt[0].lower() == 'n':
			print '* Nothing removed\n'
			break
		else:
			prompt = raw_input('Please type yes or no: ') or 'space'


def main():
	try:
		shelf_file = shelve.open('mcb.dat')
	except NameError as e:
		print e, '* Creating file mcb.dat...\n'
		shelf_file = shelve.open('mcb.dat', 'w')

	if len(sys.argv) > 1:
		try:
			options = {
				'help': 'mcb_help()',
				'list': 'list_mcb(shelf_file)',
				'save': 'save_mcb(shelf_file)',
				'del': 'delete_mcb_item(shelf_file, sys.argv[2])',
				'clear': 'clear_mcb(shelf_file)',
			}[sys.argv[1]]

			eval(options)
		except KeyError:
			load_mcb_item(shelf_file, sys.argv[1])
		except IndexError:
			print '* No clipboard name specified!\n'
	else:
		mcb_help()


	shelf_file.close()

if __name__ == '__main__':
	main()




# TODO:
# 1. saving: if chosen key exists in the dictionary - issue a warning and prompt for new name for the clipboard,
# 4. refactor this sript to OO (argparse, optparse)