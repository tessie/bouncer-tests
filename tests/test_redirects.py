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


@pytest.mark.skip_selenium
@pytest.mark.nondestructive
class TestRedirects(Base):

    @pytest.mark.parametrize('url', ["http://download.allizom.org/", "https://download.allizom.org/"])
    def test_that_checks_incorrect_values(self, url):
        param = {
            'product': 'firefox-16.0b6',
            'lang': 'test_kity',
            'os': 'stella'
        }

        response = self._get_redirect(url, params=param)

        Assert.equal(response.status_code, requests.codes.not_found)

        parsed_url = urlparse(response.url)
        Assert.equal(parsed_url.scheme, 'https')
        Assert.equal(parsed_url.netloc, urlparse(url).netloc)
        Assert.equal(parsed_url.query, urlencode(param))
