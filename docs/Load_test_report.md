# Load Testing Report

## Tool

k6

---

## Test Configuration

| Parameter | Value |
|-----------|-------|
| Virtual Users | 20 |
| Duration | 1 Minute |

---

## Results

| Metric | Result |
|---------|--------|
| Total Requests | 976 |
| Successful Requests | 976 |
| Failed Requests | 0 |
| Error Rate | 0% |
| Average Response Time | 238.47 ms |
| Maximum Response Time | 338.96 ms |
| 95th Percentile | 273.70 ms |
| Throughput | 15.98 Requests/sec |

---

## CloudWatch Metrics

The following metrics were monitored during the load test:

- CPU Usage
- Memory Usage
- Disk Usage

CloudWatch Dashboard showed stable system resource utilization throughout the test.

---

## Observations

- No request failures occurred.
- Response time remained stable.
- CPU usage remained low.
- Memory utilization remained stable.
- The application handled concurrent requests successfully.

---

## Suggested Optimizations

For production deployments:

- Configure Auto Scaling.
- Deploy behind an Application Load Balancer.
- Enable HTTPS using AWS Certificate Manager.
- Implement response caching where appropriate.