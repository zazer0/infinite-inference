from sglang.test.test_utils import is_in_ci

#if is_in_ci():
#    from patch import launch_server_cmd
#else:
from sglang.utils import launch_server_cmd

from sglang.utils import wait_for_server, print_highlight, terminate_process

PORT=31111

server_process, port = launch_server_cmd(
    "python3 -m sglang.launch_server --model-path IlyaGusev/gemma-2-2b-it-abliterated --context-length 1024 --host 0.0.0.0 --mem-fraction-static 0.3 --attention-backend flashinfer", port=PORT
)

wait_for_server(f"http://localhost:{PORT}")
print(f"Server started on http://localhost:{PORT}")
