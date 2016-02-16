#!/bin/python
# -*- coding: utf-8 -*-
# ####################################################################
# gofed-ng - Golang system
# Copyright (C) 2016  Fridolin Pokorny, fpokorny@redhat.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# ####################################################################

import sys
import logging

class LoggerSingleton(object):
	_instance = None

	def __init__(self):
		pass

	def init(self, configfile = None, verbose = False):
		if LoggerSingleton._instance is None:
			level = logging.INFO if verbose is True else logging.WARNING
			if configfile is not None:
				logging.basicConfig(level = level, filename = configfile)
			else:
				# use the default stream
				logging.basicConfig(level = level)
			LoggerSingleton._instance = logging.getLogger(__name__)

	def __getattr__(self, attr):
		if attr == 'init':
			return self.init
		elif attr == 'close':
			return self.shutdown

		if LoggerSingleton._instance is None:
			self.init()
		return getattr(self._instance, attr)

	def close(self):
		logging.shutdown()


log = LoggerSingleton()

if __name__ == '__main__':
	sys.exit(1)

