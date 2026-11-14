#!/usr/bin/env bash

set -e
# source /etc/os-release

# case "$ID" in
#     alpine)
#         echo "Running Alpine Linux"
#         apk add --no-cache \
#             python3 \
#             py3-yaml \
#             py3-jinja2
#         ;;

#     ubuntu|debian)
#         echo "Running $ID"
#         export DEBIAN_FRONTEND=noninteractive

#         apt-get update
#         apt-get install -y --no-install-recommends \
#             python3 \
#             python3-yaml \
#             python3-jinja2

#         rm -rf /var/lib/apt/lists/*
#         ;;

#     rhel|centos|rocky|almalinux|fedora)
#         echo "Running $ID"

#         if command -v dnf >/dev/null 2>&1; then
#             dnf install -y \
#                 python3 \
#                 python3-pyyaml \
#                 python3-jinja2
#         elif command -v yum >/dev/null 2>&1; then
#             yum install -y \
#                 python3 \
#                 python3-pyyaml \
#                 python3-jinja2
#         else
#             echo "No supported package manager found"
#             exit 1
#         fi
#         ;;

#     *)
#         echo "Unsupported OS: $ID"
#         exit 1
#         ;;
# esac

./scripts/helper/tool_version_checker.py
./scripts/render.py
