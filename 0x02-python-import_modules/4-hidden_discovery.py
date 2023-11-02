#!/usr/bin/python3

if __name__ == "__main__":
    import os
    import importlib.util

    cur_dir = os.getcwd()

    mod_name = "hidden_4.pyc"

    mod_path = os.path.join(cur_dir, mod_name)

    spec = importlib.util.spec_from_file_location("hidden_4", mod_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = [name for name in dir(module) if not name.startswith("__")]

    names.sort()

    for name in names:
        print(name)
