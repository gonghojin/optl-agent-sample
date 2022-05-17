import os
from typing import Iterable
from opentelemetry._metrics import get_meter_provider, set_meter_provider
#from opentelemetry._metrics.measurement import Measurement
from opentelemetry.instrumentation.system_metrics import SystemMetricsInstrumentor
from opentelemetry.exporter.otlp.proto.grpc._metric_exporter import (
    OTLPMetricExporter,
)
from opentelemetry.sdk._metrics import MeterProvider
from opentelemetry.sdk._metrics.export import (PeriodicExportingMetricReader, ConsoleMetricExporter)

# exporter = OTLPMetricExporter(endpoint="host.docker.internal:9095", insecure=True)
endpoint_ip = os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT', 'host.docker.internal:9095')
#endpoint_ip = os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT', 'localhost:9095')
exporter = OTLPMetricExporter(endpoint=endpoint_ip, insecure=True)
console_reder = ConsoleMetricExporter()
reader = PeriodicExportingMetricReader(exporter, 10000)
reader2 = PeriodicExportingMetricReader(console_reder, 10000)
provider = MeterProvider(metric_readers=[reader, reader2])
set_meter_provider(provider)
SystemMetricsInstrumentor().instrument()
meter = get_meter_provider().get_meter("demo-python-server-meter")
