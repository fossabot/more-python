#!/usr/bin/env bash
bash -c "bash <(curl -s https://codecov.io/bash) -t ${$CODECOV_TOKEN}"