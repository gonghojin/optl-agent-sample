# otlpcollector_example.py

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from opentelemetry.sdk.resources import Resource

resource = Resource(attributes={
    "service.name": "service"
})

span_exporter = OTLPSpanExporter(
    # optional
    endpoint="192.168.10.123:9090",
    insecure=True
    # credentials=ChannelCredentials(credentials),
    # headers=(("metadata", "metadata")),
)
tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)
span_processor = BatchSpanProcessor(span_exporter)
tracer_provider.add_span_processor(span_processor)



# Configure the tracer to use the collector exporter
tracer = trace.get_tracer_provider().get_tracer(__name__)

with tracer.start_as_current_span("foo"):
    print("Hello world!")
