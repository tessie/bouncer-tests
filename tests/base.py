#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import requests
import socket
from bs4 import BeautifulSoup


class Base:

    _user_agent_firefox = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:10.0.1) Gecko/20100101 Firefox/10.0.1'

    def _head_request(self, url, user_agent=_user_agent_firefox, locale='en-US', params=None):

        headers = {'user-agent': user_agent,
                   'accept-language': locale}

        return requests.head(url, headers=headers, verify=False, timeout=9, params=params, allow_redirects=True)

    def _parse_response(self, content):
        return BeautifulSoup(content)

    def response_info_failure_message(self, url, param, response):
        return 'Failed on %s \nUsing %s.\n %s' % (url, param, self.response_info(response))

    def response_info(self, response):
        url = response.url
        x_backend_server = response.headers['X-Backend-Server']
        return 'Response URL: %s\n X-Backend-Server: %s' % (url, x_backend_server)
