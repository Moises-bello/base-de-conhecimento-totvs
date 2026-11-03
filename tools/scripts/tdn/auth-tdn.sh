#!/usr/bin/env bash
# Atalho: autenticar no TDN (uma vez)
cd "$(dirname "$0")/../../.."
exec .venv/bin/python tools/sync.py auth-tdn "$@"
