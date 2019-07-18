# stat-perf-tests

## running tests

```bash
locust -f switch_graph_types_test.py --host=https://arendus.juhtimislauad.stat.ee/api --no-web -c 300 -r 10 --run-time 5m
```
Paremeters:
- *-c* - number of concurrent threads
- *-r* - hatch rate or how many users to spawn per second
- *--run-time* - for how long to run tests
- *--no-web* - does not create a dashboard (see below)

Alternatively leave out the above parameters and open localhost:8089 in browser and spetsify users and hatchrate manually.
