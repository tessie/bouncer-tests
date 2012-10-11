#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from urlparse import urlparse
from urllib import urlencode
from unittestzero import Assert

from base import Base


class TestRedirects(Base):

    @pytest.mark.parametrize('url', ["http://download.allizom.org/", "https://download.allizom.org/"])
    def test_that_checks_redirect_using_incorrect_query_values(self, url):
        param = {
            'product': 'firefox-16.0b6',
            'lang': 'kitty_language',
            'os': 'stella'
        }

        response = self._head_request(url, params=param)

        Assert.equal(response.status_code, requests.codes.not_found, 'Failed on %s \nUsing %s' % (url, param))

        parsed_url = urlparse(response.url)
        Assert.equal(parsed_url.scheme, 'https', 'Failed on %s \nUsing %s' % (url, param))
        Assert.equal(parsed_url.netloc, urlparse(url).netloc, 'Failed on %s \nUsing %s' % (url, param))
        Assert.equal(parsed_url.query, urlencode(param), 'Failed on %s \nUsing %s' % (url, param))

    def test_that_checks_redirect_using_locales_and_os(self, testsetup, lang, os):

        url = testsetup.base_url

        # Ja locale has a special code for mac
        if lang == 'ja' and os == 'osx':
            lang = 'ja-JP-mac'

        param = {
            'product': 'firefox-16.0b6',
            'lang': lang,
            'os': os
        }

        response = self._head_request(url, params=param)

        parsed_url = urlparse(response.url)

        Assert.equal(response.status_code, requests.codes.ok, 'Failed on %s \nUsing %s' % (url, param))
        Assert.equal(parsed_url.scheme, 'http', 'Failed on %s \nUsing %s' % (url, param))

    @pytest.mark.xfail(reason='there currently is not a stub installer -- xfailing until one lands in the wild')
    def test_stub_installer_redirect_for_en_us_and_win(self, testsetup):
        url = testsetup.base_url
        param = {
            'product': testsetup.product,
            'lang': 'en-US',
            'os': 'win'
        }

        response = self._head_request(url, params=param)

        parsed_url = urlparse(response.url)

        Assert.equal(response.status_code, requests.codes.ok, 'Failed on %s \nUsing %s' % (url, param))
        Assert.equal(parsed_url.scheme, 'https', 'Failed on %s \nUsing %s' % (url, param))
        Assert.equal(parsed_url.netloc, 'download-installer.cdn.mozilla.net', 'Failed on %s \nUsing %s' % (url, param))

    @pytest.mark.parametrize('product_alias', [
        {'product_name': 'firefox-aurora-latest', 'lang': 'en-US'},
        {'product_name': 'firefox-beta-latest', 'lang': 'en-US'},
        {'product_name': 'firefox-latest-euballot', 'lang': 'en-GB'},
        {'product_name': 'firefox-latest', 'lang': 'en-US'},
        {'product_name': 'firefox-nightly-latest', 'lang': 'en-US'}])
    def test_redirect_for_firefox_aliases(self, testsetup, product_alias):
        url = testsetup.base_url
        param = {
            'product': product_alias['product_name'],
            'os': 'win',
            'lang': product_alias['lang']
        }

        response = self._head_request(url, params=param)

        parsed_url = urlparse(response.url)

        Assert.equal(response.status_code, requests.codes.ok, 'Failed on %s \nUsing %s' % (url, param))
        Assert.equal(parsed_url.scheme, 'http', 'Failed on %s \nUsing %s' % (url, param))
        Assert.equal(parsed_url.netloc, 'download.cdn.mozilla.net', 'Failed on %s \nUsing %s' % (url, param))
        if (
            product_alias['product_name'] != 'firefox-nightly-latest' and
            product_alias['product_name'] != 'firefox-aurora-latest' and
            product_alias['product_name'] != 'firefox-latest-euballot'
        ):
            Assert.contains('/%s/' % 'win32', parsed_url.path)
