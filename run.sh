#!/bin/bash

scripts=(
    "single_thread.py"
    "multi_thread_share.py"
    "multi_thread_share_lock.py"
    "multi_thread_private.py"
)

run_scripts_with_gil() {
    local gil_value=$1
    export PYTHON_GIL=$gil_value
    echo "Running scripts with PYTHON_GIL=$PYTHON_GIL"
    for script in "${scripts[@]}"; do
        echo "===== Running $script ====="
        uv run "./$script"
        echo -e "===== Finished  =====\n\n"
    done
}

run_scripts_with_gil 1
run_scripts_with_gil 0
