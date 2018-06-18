from mdstudio.deferred.chainable import chainable
from mdstudio.component.session import ComponentSession
from mdstudio.runner import main
import os

cwd = os.path.dirname(os.path.abspath(__file__))
path_test_file = os.path.join(cwd, "files/input.mol2")

with open(path_test_file, 'r') as f:
    content = f.read()

dict_path_file = {
    'content': content, 'path': path_test_file, 'extension': '.mol2'}


class Run_test_resources(ComponentSession):

    def authorize_request(self, uri, claims):
        return True

    @chainable
    def on_run(self):
        with self.group_context('mdgroup'):
            yield self.call(
                "mdgroup.common_resources.endpoint.file_path",
                {'file': dict_path_file})


if __name__ == "__main__":
    main(Run_test_resources)
