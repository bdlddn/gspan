#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  for_test.py
#  
#  Copyright 2017 masai <masai@masaideMacBook-Air.local>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from graph_data import GraphData

class Dog():
	"""测试专用"""
	
	x = 'this is x'
	sx = [1, 2, 3, 4]
	
	def __init__(self):
		self.y = 'this is y'
		self.sy = [5, 6, 7, 8]
	
	def set_x(self, x):
		self.x = x
	
	def get_x(self):
		return self.x
	
	def set_sx(self,sx):
		self.sx = sx
	
	def get_sx(self):
		return self.sx
		
	def set_sy(self,sy):
		self.sy = sy
	
	def get_sy(self):
		return self.sy
	
	def print_dog(self):
		print(self.x)
		print(self.sy)
	

if __name__ == '__main__':
	#~ dog = Dog()
	#~ dog.print_dog()
	#~ dog.set_x('this is reset x')
	#~ dog.get_sy().append(9)
	#~ dog.print_dog()
	#~ dog.set_sy([2,3,4])
	#~ dog.print_dog
	#~ dog = Dog()
	#~ dog.set_x('this is reset x')
	#~ dog.print_dog()
	#~ i = 0
	#~ while i < 1:
		#~ dog = Dog()
		#~ dog.print_dog()
		#~ i += 1
	#~ b = []
	#~ if a[0] == '1':
		#~ print("true")
	#~ if b == None:
		#~ print("none")
	
	gd = GraphData()
	gd.get_node_labels().append('0')
	gd.get_node_labels().append('1')
	gd.get_node_labels().append('20')
	
	#~ if gd is not None:
		#~ print(gd)
	x = ''
	if  not gd.get_node_labels() :
		print('None')
	if not '1' in gd.get_node_labels():
		print('contains "1"')
		print(int(gd.get_node_labels()[2]))

		
