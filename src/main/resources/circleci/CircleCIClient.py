#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import json
from xlrelease.HttpRequest import HttpRequest

class CircleCiClient(object):
    def __init__(self, http_connection, token=None):
        self.http_request = HttpRequest(http_connection, token)

    @staticmethod
    def create_client(http_connection, token=None):
        return CircleCiClient(http_connection, token)

    def get_user(self):
        get_user_endpoint = "/me"
        get_user_response = self.http_request.get(get_user_endpoint, contentType='application/json')
        if not get_user_response.isSuccessful():
            raise Exception("Failed to get user information. Server return [%s], with content [%s]" % (get_user_response.status, get_user_response.response))
        return json.loads(get_user_response.getResponse())
