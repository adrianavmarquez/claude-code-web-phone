# claude-code-web-phone

## Composio setup

> **Note:** The official one-line installer
> (`curl -fsSL https://composio.dev/install | bash`) does **not** work in this
> environment. Outbound HTTPS is filtered by an egress proxy, and the
> `composio.dev` download host is not on the allowlist (it returns HTTP 403).
> The standalone Composio CLI binary is only distributed from that host, so it
> cannot be installed here.

Instead, install the Composio Python SDK from PyPI (which **is** allowlisted):

```bash
python3 -m venv .composio-venv
.composio-venv/bin/pip install --upgrade pip setuptools wheel
.composio-venv/bin/pip install -r requirements.txt
```

Verify:

```bash
.composio-venv/bin/python -c "import composio; print(composio.__version__)"
```

The pinned version lives in [`requirements.txt`](./requirements.txt). The
`.composio-venv/` directory is git-ignored — recreate it with the commands
above on a fresh checkout.
