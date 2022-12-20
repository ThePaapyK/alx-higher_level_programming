#!/bin/bash
# Take in URL, send POST request setting some params, display body
curl -sX POST -d "email=test@gmail.com&subject=I will always be there for PLD" "$1"
