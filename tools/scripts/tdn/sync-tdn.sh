#!/usr/bin/env bash
# Atalho: sincronizar TDN (após auth-tdn)
cd "$(dirname "$0")/../../.."
exec .venv/bin/python tools/sync.py sync --source tdn-fluig "$@"
