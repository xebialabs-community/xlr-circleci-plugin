#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from circleci.CircleCIClient import CircleCiClient


class CircleCiClientUtil(object):

    @staticmethod
    def create_circle_ci_client(container, token):
        client = CircleCiClient.create_client(container, token)
        return client
