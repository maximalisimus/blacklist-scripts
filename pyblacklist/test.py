#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import pathlib
import sys

class Arguments:
	''' Class «Arguments».
	
		Info: A class designed to store command-line values 
				by entering parameters through the «Argparse» module.
		
		Variables: All parameters are entered using the «createParser()» 
					method.
		
		Methods: 
			__getattr__(self, attrname):
				Access to a non-existent variable.
				Used when trying to get a parameter that does not exist. 
				In this case, «None» is returned to the user, instead 
				of an error.
			
			__str__(self):
				For STR Function output paramters.
			
			__repr__(self):
				For Debug Function output paramters.
	'''
	
	__slots__ = ['__dict__']
	
	def __getattr__(self, attrname):
		''' Access to a non-existent variable. '''
		return None

	def __str__(self):
		''' For STR Function output paramters. '''
		except_list = ['']
		#return '\t' + '\n\t'.join(tuple(map(lambda x: f"{x}: {getattr(self, x)}" if not x in except_list else f"", tuple(filter( lambda x: '__' not in x, dir(self))))))
		return '\t' + '\n\t'.join(f"{x}: {getattr(self, x)}" for x in dir(self) if not x in except_list and '__' not in x)
	
	def __repr__(self):
		''' For Debug Function output paramters. '''
		except_list = ['']
		return f"{self.__class__}:\n\t" + \
				'\n\t'.join(f"{x}: {getattr(self, x)}" for x in dir(self) if not x in except_list and '__' not in x)
				#'\n\t'.join(tuple(map(lambda x: f"{x}: {getattr(self, x)}" if not x in except_list else f"", tuple(filter( lambda x: '__' not in x, dir(self))))))

class AppendBool(argparse.Action):
	
	def __init__(self,
                 option_strings,
                 dest,
                 nargs=None,
                 const=None,
                 default=None,
                 type=None,
                 choices=None,
                 required=False,
                 help=None,
                 metavar=None):
		super(AppendBool, self).__init__(option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            const=const,
            default=default,
            type=type,
            choices=choices,
            required=required,
            help=help,
            metavar=metavar)
	
	def __call__(self, parser, namespace, values, option_string=None):
		def on_copy_items(items):
			if items is None:
				return []
			if type(items) is list:
				return items[:]
			import copy
			return copy.copy(items)
		items = getattr(namespace, self.dest, None)
		items = on_copy_items(items)
		if len(values) == 0:
			items.append(self.const)
		else:
			for elem in values:
				val = str(elem[0].upper() + elem[1:].lower())
				if str(self.const) == val:
					items.append(self.const)
				else:
					items.append(not self.const)
		setattr(namespace, self.dest, items)

def expand_params(lst1: list, lst2: list, value):
	if len(lst1) < len(lst2):
		for k in range(len(lst1), len(lst2)):
			lst1.append(value)

def main():
	args = Arguments()
	parser = argparse.ArgumentParser()
	parser.add_argument("-R", "-regex", '--regex', metavar='REGEX', type=str, default=[], nargs='+', help='Regular expression.')
	parser.add_argument("-M", "-maxcount", '--maxcount', metavar='MAXCOUNT', type=int, default=[], nargs='+', help='Stop after the specified NUMBER of matched rows')
	parser.add_argument ('-I','-ignorecase', '--ignorecase', action=AppendBool, const=True, type=str, nargs='*', default=[], help='Ignore the case of the string.')
	parser.add_argument ('-v','-invert', '--invert', action=AppendBool, const=True, type=str, nargs='*', default=[], help='Select unsuitable lines.')
	parser.add_argument ('-O','-only', '--only', action=AppendBool, const=True, type=str, nargs='*', default=[], help='Show only matched non-empty parts of strings')
	parser.parse_args(namespace=Arguments)
	expand_params(args.maxcount, args.regex, 0)
	expand_params(args.ignorecase, args.regex, False)
	expand_params(args.invert, args.regex, False)
	expand_params(args.only, args.regex, False)
	print(args)

if __name__ == '__main__':
	main()
