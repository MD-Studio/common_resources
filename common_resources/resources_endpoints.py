from mdstudio.api.endpoint import endpoint
from mdstudio.component.session import ComponentSession


class Common_resources(ComponentSession):
    """
    """
    def authorize_request(self, uri, claims):
        return True

    @endpoint('path_file', 'path_file_request', 'path_file_response')
    def call_path_file(self, request, claims):
        """
        echo a `file_path` object.
        """
        path = request("path_file")
        print("object name: ", path['name'])
        print("object encoding: ", path['encoding'])
        print("object extension: ", path['extension'])

        return {'status': 'completed', 'file': path}
