# Opentelemetry python agent 

---

## auto-instrument
### elasticsearch[https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-elasticsearch]
1. elasticsearch instrumentation 설치
```
❯ pip install opentelemetry-instrumentation-elasticsearch
```

2. python root 파일에 해당 클래스 생성 및 호출
```
./elastic.py

...
ElasticsearchInstrumentor().instrument()
...
```