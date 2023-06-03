#!/bin/bash

API="o.vaPPxpIea8K6JRg7yHk1rap8OV1jPISU"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="화재 경보!" -d body="화재가 발생했습니다"
