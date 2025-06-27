#!/bin/bash

set -e

SERVICES=("account" "user" "analytics" "transaction")
BASE_URL="https://bankx.local"

echo "🔍 Checking health of all services at $BASE_URL"

for SERVICE in "${SERVICES[@]}"; do
    echo -n "➡️  $SERVICE: "
    STATUS=$(curl -sk -o /dev/null -w "%{http_code}" "$BASE_URL/$SERVICE/health")
    if [ "$STATUS" -eq 200 ]; then
        echo "✅ Healthy (HTTP $STATUS)"
    else
        echo "❌ Unhealthy (HTTP $STATUS)"
    fi
done

