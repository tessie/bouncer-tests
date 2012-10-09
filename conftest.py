#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import py
LOCALES = ['ach', 'af','ak','ar', 'as', 'ast', 'be', 'bg', 'bn-BD', 'bn-IN', 'br', 'bs', 'ca', 'cs', 'csb', 'cy', 'da', 'de', 'el', 'en-GB',
           'en-ZA', 'eo', 'es-AR', 'es-CL', 'es-ES', 'es-MX', 'et', 'eu', 'fa', 'ff', 'fi', 'fr', 'fy-NL', 'ga-IE', 'gd', 'gl', 'gu-IN',
           'he', 'hi-IN', 'hr', 'hu', 'hy-AM', 'id', 'is', 'it', 'ja', 'kk', 'km', 'kn', 'ko', 'ku', 'lg', 'lij', 'lt', 'lv', 'mai', 'mk',
           'ml', 'mn', 'mr', 'nb-NO', 'nl', 'nn-NO', 'nso', 'or', 'pa-IN', 'pl', 'pt-BR', 'pt-PT', 'rm', 'ro', 'ru', 'si', 'sk', 'sl',
           'son', 'sq', 'sr', 'sv-SE', 'sw', 'ta', 'ta-LK', 'te', 'th', 'tr', 'uk', 'vi', 'zh-CN', 'zh-TW', 'zu']

OS = ['win',  'linux',  'osx']

def pytest_generate_tests(metafunc):
    if 'lang' in metafunc.funcargnames:
        metafunc.parametrize('lang',  LOCALES)

    if 'os' in metafunc.funcargnames:
        metafunc.parametrize('os',  OS)
