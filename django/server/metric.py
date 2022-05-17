import os

from opentelemetry._metrics import get_meter_provider, set_meter_provider
from opentelemetry.exporter.otlp.proto.grpc._metric_exporter import (
    OTLPMetricExporter,
)
# from opentelemetry._metrics.measurement import Measurement
from opentelemetry.instrumentation.system_metrics import SystemMetricsInstrumentor
from opentelemetry.sdk._metrics import MeterProvider
from opentelemetry.sdk._metrics.export import (PeriodicExportingMetricReader)

endpoint_ip = os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT', 'localhost:9095')
exporter = OTLPMetricExporter(endpoint=endpoint_ip, insecure=True)
reader = PeriodicExportingMetricReader(exporter, 10000)
provider = MeterProvider(metric_readers=[reader])
set_meter_provider(provider)
SystemMetricsInstrumentor().instrument()
meter = get_meter_provider().get_meter("demo-python-server-meter")
