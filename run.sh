#!/bin/bash
podman build -t dyn .
podman run -it --rm -p 5000:5000 dyn