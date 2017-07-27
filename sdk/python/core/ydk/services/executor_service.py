#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------
import inspect
from ydk.ext.services import ExecutorService as _ExecutorService
from ydk.errors import YPYServiceError as _YPYServiceError
from ydk.errors.error_handler import handle_runtime_error as _handle_error


class ExecutorService(_ExecutorService):
    """ Python wrapper for ExecutorService
    """
    def __init__(self):
        self._es = _ExecutorService()

    def execute_rpc(self, session, entity, top_entity=None):
        if None in (session, entity):
            raise _YPYError("session and entity cannot be None")

        with _handle_error():
            return self._es.execute_rpc(session, entity, top_entity)
