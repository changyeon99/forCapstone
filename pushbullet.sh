#!/bin/bash

API="o.vaPPxpIea8K6JRg7yHk1rap8OV1jPISU"
MSG="$1"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="WARNING" -d body="$MSG"
