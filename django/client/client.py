# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import sys
import time
from sys import argv
import platform
import socket

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.sdk.resources import (Resource,ResourceAttributes)
from opentelemetry.propagate import inject
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor, ConsoleSpanExporter,
)
from requests import get

# import metric

auto_resource = {
    "service.name": "python-client-tracer-demo",
    "prcoess.uuid" :"550e8400-e29b-41d4-a716-446655442222",
}
sys
resource = Resource.create({
    "service.name": "python-client-tracer-demo",
    "prcoess.uuid" :"550e8400-e29b-41d4-a716-446655442222",
    ResourceAttributes.HOST_NAME: socket.gethostname(),
    ResourceAttributes.PROCESS_COMMAND_ARGS: argv[1],
    ResourceAttributes.PROCESS_EXECUTABLE_NAME: "client",
    ResourceAttributes.PROCESS_EXECUTABLE_PATH: sys.executable,
    ResourceAttributes.PROCESS_OWNER: os.uname()[0],
    ResourceAttributes.PROCESS_PID: os.getpid(),
    ResourceAttributes.PROCESS_RUNTIME_DESCRIPTION: ResourceAttributes.PROCESS_RUNTIME_DESCRIPTION,
    ResourceAttributes.PROCESS_RUNTIME_NAME: argv[0],
    ResourceAttributes.PROCESS_RUNTIME_VERSION: ResourceAttributes.PROCESS_RUNTIME_VERSION,
})

os.environ.setdefault(
    "OTEL_RESOURCE_ATTRIBUTES", "service.name=demo-python-client-tracer,prcoess.uuid=550e8400-e29b-41d4-a716-446655442222"
)

endpoint_ip = os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT', 'localhost:9095')
serverIp = os.getenv('PYTHON_DEMO_SERVER_ENDPOINT', 'http://localhost:8002')
otlp_exporter = OTLPSpanExporter(
    endpoint=endpoint_ip,
    insecure=True)

otlp_exporter_collector = OTLPSpanExporter(
    endpoint='192.168.10.123:9095',
    insecure=True)

tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer_provider().get_tracer(__name__)

span_processor_otlp = BatchSpanProcessor(otlp_exporter)
#span_processor_otlp = BatchSpanProcessor(otlp_exporter)
span_processor_otlp_expoter = BatchSpanProcessor(otlp_exporter_collector)
tracer_provider.add_span_processor(span_processor_otlp)
tracer_provider.add_span_processor(span_processor_otlp_expoter)
# tracer_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

while 1:
    with tracer.start_as_current_span("python-client-demo"):
        with tracer.start_as_current_span("python-client-server-demo"):
            headers = {}
            inject(headers)
            requested = get(
                serverIp,
                params={"param": argv[1]},
                headers=headers,
            )

        assert requested.status_code == 200
        print(requested)
        time.sleep(10)

