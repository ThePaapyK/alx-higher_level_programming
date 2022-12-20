#!/bin/bash
# Takes in URL, sends GET request setting a header variable, display body
curl -sX "GET" -H "X-School-User-Id: 98" "$1"
