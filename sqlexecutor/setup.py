# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2012 Roberto Longobardi
# 
# This file is part of the Test Manager plugin for Trac.
# 
# The Test Manager plugin for Trac is free software: you can 
# redistribute it and/or modify it under the terms of the GNU 
# General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later 
# version.
# 
# The Test Manager plugin for Trac is distributed in the hope that it 
# will be useful, but WITHOUT ANY WARRANTY; without even the implied 
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with the Test Manager plugin for Trac. See the file LICENSE.txt. 
# If not, see <http://www.gnu.org/licenses/>.
#

from setuptools import setup

setup(
    name='SQLExecutor',
    version='1.0.6',
    packages=['sqlexecutor'],
    package_data={'sqlexecutor' : ['*.txt', 'templates/*.html', 'htdocs/*.*', 'htdocs/js/*.js', 'htdocs/css/*.css', 'htdocs/images/*.*']},
    author = 'Roberto Longobardi',
    author_email='otrebor.dev@gmail.com',
    license='GPL v. 3. See the file LICENSE.txt contained in the package.',
    url='http://trac-hacks.org/wiki/TestManagerForTracPlugin',
    download_url='https://sourceforge.net/projects/testman4trac/files/',
    description='Test management plugin for Trac - SQL Executor component',
    long_description='A Trac plugin to create Test Cases, organize them in catalogs and track their execution status and outcome. This module provides a generic SQL executor to help debugging your application.',
    keywords='trac plugin generic class framework persistence sql execution run test case management project quality assurance statistics stats charts charting graph',
    entry_points = {'trac.plugins': ['sqlexecutor = sqlexecutor']},
    dependency_links=['http://trac-hacks.org/wiki/TestManagerForTracPluginGenericClass'],
    install_requires=['TracGenericClass >= 1.1.1']
    )
