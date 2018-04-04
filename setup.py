#!/usr/bin/env python3
#
# This file is part of rasa-teld.
#
# rasa-teld is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rasa-teld is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rasa-teld.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(name='warwick.rasa.telescope',
      version='0',
      packages = ['warwick.rasa.telescope'],
      author='Paul Chote',
      description='Common code for the SuperWASP upgrade prototype mount controller',
      license='GNU GPLv3',
      author_email='p.chote@warwick.ac.uk',
      url="https://github.com/warwick-one-metre/rasa-teld",
)
