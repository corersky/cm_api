#! /usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

from sys import version_info
if version_info[:2] > (2, 5):
    install_requires = []
else:
    install_requires = ['simplejson >= 2.0.0']

setup(
  name = 'cm_api',
  version = '1.0.0',    # Compatible with API v1
  packages = find_packages('src'),
  package_dir = {'cm_api': 'src/cm_api'},

  # Project uses simplejson, so ensure that it gets installed or upgraded
  # on the target machine
  install_requires = install_requires,

  author = 'Cloudera, Inc.',
  description = 'Cloudera Manager API client',
  license = 'Apache License 2.0',
  url = 'https://github.com/cloudera/cm_api',
)
