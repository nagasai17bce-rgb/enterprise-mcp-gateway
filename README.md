# Enterprise MCP Gateway

Tool gateway with authorization, audit events, and controlled invocation.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

POST `{"value":"demo"}` to `/v1/run`.

## Architecture

Client -> FastAPI -> domain service -> policy/state logic -> structured response.

The project is intentionally credential-free and runnable locally. Production deployment should add authentication, durable storage, secrets management, observability, distributed queues, and provider-specific adapters where applicable.
