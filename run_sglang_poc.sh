#!/bin/bash 

if [ ! -f "./.venv/bin/activate" ]; then
    echo "Need a venv with pyproject toml installed!" && exit 1
fi

source .venv/bin/activate

MODEL=IlyaGusev/gemma-2-2b-it-abliterated

echo "Venv sourced! Launching SgLang to serve ${MODEL}, with default args!"

python3 -m sglang.launch_server --port 31111 --host 0.0.0.0 \
    --attention-backend flashinfer \
    --model-path "${MODEL}" \
    --context-length 1024 \
    --mem-fraction-static 0.3
