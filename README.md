# MCP-Remote

A simple FastMCP server exposing calculator tools over HTTP, deployable to any cloud (Prefect, Railway, Render, etc.).

## Tools

| Tool | Description |
|---|---|
| `add(a, b)` | Add two integers |
| `random_number(min, max)` | Random int in range (default 1–100) |
| `info://server` | Resource: server name & version |

---

## Deploy to FastMCP Cloud

FastMCP Cloud hosts your MCP server and gives you a public SSE/HTTP endpoint in one command.

### 1. Install FastMCP CLI

```bash
pip install fastmcp
```

### 2. Authenticate

```bash
fastmcp auth login
```

### 3. Deploy

```bash
fastmcp deploy main.py
```

FastMCP will build, push, and return a public URL like:
```
https://<your-server>.fastmcp.com/mcp
```

### 4. Connect from Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "calculator": {
      "url": "https://<your-server>.fastmcp.com/mcp"
    }
  }
}
```

---

## Run Locally

```bash
# Install dependencies (uv recommended)
uv sync
uv run main.py
# Server at http://localhost:8000/mcp
```

Or with pip:

```bash
pip install fastmcp
python main.py
```

---

## Deploy to Prefect (self-hosted flow trigger)

Use Prefect to trigger/schedule the MCP server as a long-running process.

### 1. Install

```bash
pip install prefect
```

### 2. Create a flow wrapper

```python
# prefect_deploy.py
import subprocess
from prefect import flow

@flow
def run_mcp_server():
    subprocess.run(["python", "main.py"], check=True)

if __name__ == "__main__":
    run_mcp_server.serve(name="mcp-server")
```

### 3. Start worker & run

```bash
prefect worker start --pool default-agent-pool &
python prefect_deploy.py
```

> **Note:** For production, run `main.py` inside a Docker container and use Prefect's Docker infrastructure block to deploy it as a persistent service.

---

## Requirements

- Python ≥ 3.13
- `fastmcp >= 3.4.2`
