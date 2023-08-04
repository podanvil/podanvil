def generate_functions(functions, filename):
    with open(filename, 'w') as f:
        for function in functions:
            f.write(f"def {function}():\n")
            f.write("    # TODO: implement this function\n")
            f.write("    pass\n\n")

pod_functions = ["deploy_pod", "get_pod_url", "is_accessible"]
general_functions = ["generate_name", "get_active_node"]

generate_functions(pod_functions, 'pod_utils.py')
generate_functions(general_functions, 'general_utils.py')

