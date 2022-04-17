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

from sys import argv

from requests import get

from opentelemetry import trace
from opentelemetry.propagate import inject
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)

from opentelemetry.exporter.otlp.proto.grpc._metric_exporter import (
    OTLPMetricExporter,
)

from opentelemetry.sdk.resources import Resource

resource = Resource(attributes={
    "service.name": "service"
})

otlp_exporter = OTLPSpanExporter(
    # optional
    # credentials=ChannelCredentials(credentials),
    # headers=(("metadata", "metadata")),
)

tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer_provider().get_tracer(__name__)

span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor)

# trace.get_tracer_provider().add_span_processor(
#     BatchSpanProcessor(ConsoleSpanExporter())
# )


with tracer.start_as_current_span("client"):

    with tracer.start_as_current_span("client-server"):
        headers = {}
        inject(headers)
        requested = get(
            "http://localhost:8000",
            params={"param": argv[1]},
            headers=headers,
        )

        assert requested.status_code == 200

metric_exporter = OTLPMetricExporter()
metrics.set_meter_provider(MeterProvider())
meter = metrics.get_meter(__name__)