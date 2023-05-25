#!/bin/bash

API="o.vaPPxpIea8K6JRg7yHk1rap8OV1jPISU"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="불이야" -d body="화재 경보"
