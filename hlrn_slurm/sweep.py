import argparse
from itertools import permutations
import yaml
from pathlib import Path
import copy

def find_sweep_params(sweep_config):
    sweep_params = {} 
    for k,v in sweep_config.items():
        if k.startswith("_sweep_"):
            sweep_params[k] = v
        elif isinstance(v, dict):
            sub_params = find_sweep_params(v)
            if sub_params:
                sweep_params[k] = sub_params
    return sweep_params

def flatten_dict(d):
    out = {}
    for k, v in d.items():
        if isinstance(v, dict):
            sub_dict = flatten_dict(v)
            for sub_k, sub_v in sub_dict.items():
                out[f"{k}.{sub_k}"] = sub_v
        else:
            out[k] = v
    return out

def generate_sweep(sweep_config, sweep_path):
    sweep_path = Path(sweep_path)
    # strip file ending from sweep_path and add "_sweep_" to the end
    sweep_path = sweep_path.with_suffix("")
    # sweep_path = sweep_path.with_name(f"{sweep_path.name}_sweep")
    if sweep_path.exists():
        print(f"Sweep directory {sweep_path} already exists. Running only existing sweep configs.")
        return list(sweep_path.glob("*.yaml"))
    # create sweep directory
    sweep_path.mkdir(parents=True, exist_ok=False)

    # find all parameters that start with "_sweep_" and generate a list of all possible combinations
    # recursively find all parameters that start with "_sweep_"
    sweep_params = find_sweep_params(sweep_config)
    # flatten the dictionary
    sweep_params = flatten_dict(sweep_params) 
    
    # generate all possible combinations of parameters
    import itertools
    keys, values = zip(*sweep_params.items())
    sweep_combinations = [dict(zip(keys, v)) for v in itertools.product(*values)]

    # create new config for each combination
    config_files = []
    for i, sweep_combination in enumerate(sweep_combinations):
        new_config = copy.deepcopy(sweep_config)
        for k, v in sweep_combination.items():
            # find the key in the config
            sub_dict = new_config
            keys = k.split(".")
            for key in keys[:-1]:
                sub_dict = sub_dict[key]

            # strip "_sweep_" from the key and set the value
            key = keys[-1]
            del sub_dict[key] 
            key = key.replace("_sweep_", "")
            sub_dict[key] = v
        # write config to file
        yaml_file = Path(f"{sweep_path}/sweep_{i}.yaml")
        yaml_file.write_text(yaml.dump(new_config))
        config_files.append(yaml_file)
    return config_files
