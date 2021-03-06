#!/usr/bin/python3
# -*- coding: utf-8 -*-
# geo-coding is licensed under the Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#     http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
# PURPOSE.
# See the Mulan PSL v2 for more details.
# Create: 2021-8-13

import geocoding


class TestDatasets(object):
    def test_china_provincial_level_administrative_region(self):
        data = geocoding.datasets.china_provincial_level_administrative_region()
        print(data)

    def test_china_prefecture_level_administrative_region(self):
        data = geocoding.datasets.china_prefecture_level_administrative_region()
        print(data)

    def test_county_provincial_level_administrative_region(self):
        data = geocoding.datasets.china_county_level_administrative_region()
        print(data)

    def test_china_higher_education_college(self):
        data = geocoding.datasets.china_higher_education_college()
        print(data)

    def test_china_higher_education_university(self):
        data = geocoding.datasets.china_higher_education_university()
        print(data)
