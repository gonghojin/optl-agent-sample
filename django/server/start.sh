opentelemetry-instrument --service_name django-server-demo --resource_attributes "service.instance.id=550e8400-e29b-41d4-a716-446655440000" --exporter_otlp_traces_endpoint "localhost:9095" --exporter_otlp_insecure True python manage.py runserver --noreload

