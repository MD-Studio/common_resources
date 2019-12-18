# -*- coding: utf-8 -*-

from mdstudio.api.endpoint import endpoint
from mdstudio.component.session import ComponentSession


class Common_resources(ComponentSession):
    """
    """
    def authorize_request(self, uri, claims):
        return True

    @endpoint('call_path_file', 'path_file_request', 'path_file_response')
    def call_path_file(self, request, claims):
        """
        echo a `file_path` object.
        """
        path_file = request["path_file"]
        print("object original path: ", path_file['path'])
        print("object encoding: ", path_file['encoding'])
        print("object extension: ", path_file['extension'])

        return {'status': 'completed', 'path_file': path_file}
