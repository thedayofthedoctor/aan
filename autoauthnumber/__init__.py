# -*- coding: utf-8 -*-

"""
THIS FILE IS PART OF NETWORK FOR MWAFU LIBRARY LOVE BOOK STORE BY MATT BELFAST BROWN
__init__.py - The core part of the Author Number library.

Author: Matt Belfast Brown
Creat Date:2021-05-30
Version Date：2023-06-10
Version:1.2.2

THIS PROGRAM IS FREE FOR EVERYONE,IS LICENSED UNDER GPL-3.0
YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2021-2023 Matt Belfast Brown
Copyright (C) 2021-2023 MWAFU LOVE BOOK STORE

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import autoauthnumber.Translate_API.BaiDu_API as BaiDu_API
import autoauthnumber.Translate_API.YouDao_API as YouDao_API
import autoauthnumber.author_number as author_number
import autoauthnumber.mk_Pron as mk_Pron

__title__ = 'autoauthnumber'
__version__ = '1.2.2'
__author__ = 'Matt Belfast Brown , MWAFU LIBRARY LOVE BOOK STORE'
__license__ = 'GPL-3.0'
__copyright__ = 'Copyright (c) 2021-2023 Matt Belfast Brown , Copyright (C) 2021-2023 MWAFU LOVE BOOK STORE'
__all__ = ['author_number',
           'mk_Pron', 'Translate_API', 'BaiDu_API', 'YouDao_API']

fun_spli_name = author_number.fun_spli_name
fun_take_code = author_number.fun_take_code
get_pronouncation = mk_Pron.get_pronouncation
make_pronouncation = mk_Pron.make_pronouncation
baidu_get_translate = BaiDu_API.get_translate
youdao_get_translate = YouDao_API.get_translate
