import json
import sys

from {{module_name}} import {{function_name}}

def run_lambda(data_packet):
    return {{function_name}}(data_packet)

if __name__ == "__main__":
    data_string = sys.argv[1:]
    data_packet = json.loads(data_string)

    run_lambda(data_packet)