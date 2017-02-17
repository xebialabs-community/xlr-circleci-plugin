#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from circleci.CircleCIClientUtil import CircleCiClientUtil


circle_ci_client = CircleCiClientUtil.create_circle_ci_client(server, token)

result = circle_ci_client.trigger_build(vcs, username, project, branch, wait, waitInterval)
buildNumber = result["build_num"]
buildResult = result["status"]
