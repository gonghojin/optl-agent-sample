// Copyright The OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Sample contains a simple http server that exports to the OpenTelemetry agent.
package main

import (
	"math/rand"
	"net/http"
	"os"
	"time"

	"go.elastic.co/apm/module/apmhttp/v2"
)

var rng = rand.New(rand.NewSource(time.Now().UnixNano()))

// Initializes an OTLP exporter, and configures the corresponding trace and
// metric providers.

func main() {
	os.Setenv("ELASTIC_APM_SERVICE_NAME", "demo-server-es")
	handler := http.HandlerFunc(func(w http.ResponseWriter, req *http.Request) {
		//  random sleep to simulate latency
		var sleep int64
		switch modulus := time.Now().Unix() % 5; modulus {
		case 0:
			sleep = rng.Int63n(2000)
		case 1:
			sleep = rng.Int63n(15)
		case 2:
			sleep = rng.Int63n(917)
		case 3:
			sleep = rng.Int63n(87)
		case 4:
			sleep = rng.Int63n(1173)
		}
		time.Sleep(time.Duration(sleep) * time.Millisecond)
		w.Write([]byte("Hello World"))
	})
	wrappedHandler := apmhttp.Wrap(handler)

	// serve up the wrapped handler
	http.Handle("/hello", wrappedHandler)
	http.ListenAndServe(":7090", nil)
}
