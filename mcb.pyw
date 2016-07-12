#!/usr/bin/python

import sys
import pyperclip
import shelve


def mcb_help():
	print 'Someday here may appear help section...'
	print 'MultiClipboard v0.1.\nUse:\n-h or --help\nsave [keyword]\nlist - to list keys ...\n'

def list_mcb(file):
	print 'Saved clipboards:'
	for i, k in enumerate(file.keys()):
		print '{:>2}. {}'.format(i+1, k)

def save_mcb(file, item):
	key = item if item != ''  else '-'
	file[key] = pyperclip.paste()
	print 'Clipboard saved as {}'.format(key)

def recall_mcb_item(file, item):
	print file.get(
			item,
			'No saved clipboard named "{}"'.format(item)
			)

def delete_mcb_item(file, item):
	pass

def clear_mcb(file):
	pass

def main():
	try:
		shelf_file = shelve.open('mcb.dat')
	except NameError as e:
		print e, 'Creating file mcb.dat...'
		shelf_file = shelve.open('mcb.dat', 'w')

	if len(sys.argv) > 1:
		try:
			options = {
				'help': 'mcb_help()',
				'list': 'list_mcb(shelf_file)',
				'save': 'save_mcb(shelf_file, sys.argv[2])',
				'delete': 'delete_mcb_item(shelf_file, sys.argv[2])',
				'clear': 'clear_mcb(shelf_file)',
			}[sys.argv[1]]

			eval(options)
		except KeyError:
			recall_mcb_item(shelf_file, sys.argv[1])
	else:
		mcb_help()


	shelf_file.close()

if __name__ == '__main__':
	main()




# TODO:
# 1. if chosen key exists in dictionary - issue a warning and prompt for new name for key,
# 2. if clipboard is empty while saving - issue a warning and don't save,
# 3. add new option: -d, --delete to delete keys from dictionary,
# 4. refactor this sript to class (argparse, optparse)
# 5. --clear, -c - remove all items from the dictionary





