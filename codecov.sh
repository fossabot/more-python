#!/usr/bin/env bash
ci_env=`bash <(curl -s https://codecov.io/env)`
bash <(curl -s https://codecov.io/bash)