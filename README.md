# Switchboard

A microservices and API platform: a gateway that routes, authenticates and rate-limits traffic across a set of services.

> **Status: planned.** This repository is a skeleton. The plan is below; work starts at M1.

## What it will do

- Runs a small set of services behind a single API gateway.
- Handles authentication (JWT), per-client rate limiting and request validation at the edge.
- Traces requests end to end across services with OpenTelemetry.
- Verifies service contracts in CI so changes cannot silently break consumers.

## Planned stack

Python · FastAPI · Postgres · Redis · Docker Compose · OpenTelemetry

## Milestones

- [x] **M0**: repository skeleton and CI
- [ ] **M1**: Two services and a gateway with routing, in Docker Compose
- [ ] **M2**: Authentication, rate limiting and request validation
- [ ] **M3**: Distributed tracing and metrics
- [ ] **M4**: Contract tests and a CI pipeline per service

## Layout

```
src/switchboard/   package source
tests/             unit tests
```

## Getting started

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m unittest discover -s tests -v
```

---

Part of [Sagar Arora's data engineering projects](https://github.com/sagararora492).
