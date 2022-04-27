# Opentelemetry 테스트 환경


Opentelemetry를 사용해서 metric & trace 데이터를 수집하고, 다양한 오픈소스 어플리케이션에서 해당 데이터를 어떤식으로 표현해주고 있는 R&D

---
## branch
+ developer
    - 테스트용 메인 브런치
  
---
## 실행 방법
+ Docker 사전 설치 후
~~~
~/nkia-optl-agent jaeger-exporter-elasticsearch 
❯ docker-compose up
~~~

정상 실행 시 다음과 같은 backend가 실행됨
- otel-collector
- Go app
  + demo-client
  + demo-server
- Django app
  + django-server-demo
  + django-client-demo
- elasticsearch
  - http://0.0.0.0:9200
- Jaeger  
  - http://0.0.0.0:16686
- Zipkin 
  - http://0.0.0.0:9411
- Prometheus
  - http://0.0.0.0:9090 