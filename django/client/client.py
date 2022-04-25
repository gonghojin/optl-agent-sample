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
import os, time

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.propagate import inject
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
)
from requests import get
from sys import argv

resource = Resource(attributes={
    "service.name": "demo-python-client-tracer"
})

endpoint_ip = os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT', 'localhost:9095')
serverIp = os.getenv('PYTHON_DEMO_SERVER_ENDPOINT', 'http://localhost:8002')
otlp_exporter = OTLPSpanExporter(
    endpoint=endpoint_ip,
    insecure=True)

tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer_provider().get_tracer(__name__)

span_processor_otlp = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor_otlp)

while True:
    with tracer.start_as_current_span("demo-python-client"):
        with tracer.start_as_current_span("demo-python-client-server"):
            headers = {}
            inject(headers)
            requested = get(
                serverIp,
                params={"param": argv[1]},
                headers=headers,
            )

        assert requested.status_code == 200
        time.sleep(10000)
