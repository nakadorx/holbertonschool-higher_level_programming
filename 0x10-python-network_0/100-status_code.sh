#!/bin/bash
# holb
curl -s -w "%{http_code}" "$1" -o /dev/null
