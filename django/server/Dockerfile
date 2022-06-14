FROM python:3.9
RUN mkdir /app
COPY . ./app
WORKDIR /app
RUN pip install -r requirements.txt
#RUN chmod +x start.sh
#RUN ./start.sh &
CMD opentelemetry-instrument --service_name django-server-demo --resource_attributes "service.instance.id=550e8400-e29b-41d4-a716-446655440000" --exporter_otlp_traces_endpoint ${OTEL_EXPORTER_OTLP_ENDPOINT} --exporter_otlp_insecure True python manage.py runserver 0.0.0.0:8000 --noreload