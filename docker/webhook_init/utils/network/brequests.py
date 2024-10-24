# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-10-22 10:25:16
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-10-22 14:11:26
# @github: https://github.com/longfengpili


import requests

import logging
brequestlogger = logging.getLogger(__name__)


class BRequests:

    def __init__(self):
        self.response = None

    def _get(self, url: str, params: dict = None, headers: dict = None, **kwargs):
        res = requests.get(url, params=params, headers=headers)
        return res

    def _post(self, url: str, params: dict = None, headers: dict = None, data: dict = None):
        res = requests.post(url, params=params, headers=headers, data=data)
        return res

    def request_api(self, method: str, url: str, params: dict = None, headers: dict = None, data: dict = None, retries: int = 3):
        attempt = 0
        while attempt < retries:
            mrequest = self._post if method == 'post' else self._get
            response = mrequest(url, params, headers=headers, data=data)
            if response.status_code in (200, 204):
                self.response = response
                # print(response.request.headers)
                break

            attempt += 1
            brequestlogger.error(f"[{method}] {url}, Attempt {attempt}, status_code: {response.status_code}")

        try:
            result = response.json()
        except:
            result = response.text
        return result
