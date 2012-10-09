#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import requests
from bs4 import BeautifulSoup
from unittestzero import Assert


class Base:

    _user_agent_firefox = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:10.0.1) Gecko/20100101 Firefox/10.0.1'

    def _get_redirect(self, url, user_agent=_user_agent_firefox, locale='en-US', params=None):

        headers = {'user-agent': user_agent,
                   'accept-language': locale}

        return requests.get(url, headers=headers, verify=False, timeout=5, params=params)

    def assert_valid_url(self, url, path, user_agent=_user_agent_firefox, locale='en-US'):
        """Checks if a URL returns a 200 OK response."""
        headers = {'user-agent': user_agent,
                   'accept-language': locale}

        # HEAD doesn't return page body.
        r = requests.head(url, headers=headers, timeout=5, allow_redirects=True, verify=False)
        return Assert.equal(r.status_code, requests.codes.ok, 'Bad URL %s found in %s' % (url, path))

    def _parse_response(self, content):
        return BeautifulSoup(content)
