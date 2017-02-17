#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import json, time
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

    def trigger_build(self, vcs, username, project, branch, wait, waitInterval):
        trigger_build_endpoint = "/project/%s/%s/%s/tree/%s" % (vcs, username, project, branch)
        trigger_build_response = self.http_request.post(trigger_build_endpoint, '{}', contentType='application/json')
        if not trigger_build_response.isSuccessful():
            raise Exception("Failed to trigger build for project [%s] on branch [%s]. Server return [%s], with content [%s]" % (project, branch, trigger_build_response.status, trigger_build_response.response))
        json_data = json.loads(trigger_build_response.getResponse())

        if wait:
            build_num = json_data["build_num"]
            while (True):
                build_information_endpoint = "/project/%s/%s/%s/%s" % (vcs, username, project, build_num)
                build_information_response = self.http_request.get(build_information_endpoint, contentType='application/json')
                if not build_information_response.isSuccessful():
                    raise Exception("Failed to retrieve build information for project [%s] on branch [%s] build number[%s]. Server return [%s], with content [%s]" % (project, branch, build_num, build_information_response.status, build_information_response.response))
                build_information = json.loads(build_information_response.getResponse())
                status = build_information["status"]
                # TODO: Need to obtain a better understanding of these states and what constitutes fail vs. pass from XLR perspective.
                if status == "success" or status == "fixed":
                    return build_information
                elif status == "failed" or status == "canceled" or status == "infrastructure_fail" or status == "timedout" or status == "no_tests":
                    sys.exit(1)
                else:
                    time.sleep(float(waitInterval))
        return json_data
