# HLRN-Slurm: A tool for submitting jobs with singularity on the HLRN Cluster :hammer:



## Features :star:

- Automatic generation of SBATCH scripts based on a given `.yaml` configuration file and/or command-line options :white_check_mark:
- Submission of multiple jobs with one command :white_check_mark:
- Automatic start of a singularity container with bindings based on the configuartion file :white_check_mark:
- Execute a given runscript in the container... :white_check_mark:
- ... or create an idle container to connect to interactively :white_check_mark:
- Generate a hyperparameter sweep (grid-search) based on a single experiment-config and execute each generated config as a separate job :white_check_mark:


## Usage :rocket:
First, you need to install the package via pip:
```bash
    $ pip install hlrn-slurm
```


Then starting a job is very simple. 

Running an experiment can be as simple as:

```bash
    $ hlrn-slurm --cfg ~/prod_config.yaml --run_args "--experiment <my_experiment>"
```
In this case, I have a set of slurm configurations that I want applied for every experiment and the only thing that changes for each run is the experiment specification that is passed to the runscript through `--run_args`.

Starting a container for development (i.e. a container that allows an interactive from outside) is even simpler:

```bash
    $ hlrn-slurm --cfg ~/dev_config.yaml
```
Once the container is started, using it for development (e.g. through VS-Code) is easily possible, but requires some prior setup.
A detailed guide on how to set this up is documented [here](https://www.hlrn.de/doc/display/PUB/VS+Code) (note that starting the container is already taken care of by `hlrn-slurm`).

## Config :wrench:
Example configuration files can be found [here](./bin/example_configs/). 
The available options and default values can be inspected via `$ hlrn-slurm --help`.

## Sweep :chart_with_upwards_trend:
The sweep option expects that you provide a sweep file. This is a `.yaml` file that contains the sweep options on top of your normal experiment configuration. 
This could look something like this:
```yaml
dataset:
    dataset_cls: ImageNet
    batch_size: 128
model:
    _sweep_model_cls: [resnet18, resnet50]
trainer:
    max_epochs: 200 
    optimizer:
        name: Lion
        _sweep_lr: [0.0001, 0.001, 0.0005]
        weight_decay: 0.05
```
Important here is the keyword `_sweep_` in front of keys that should be included in the sweep. 
The tool will generate configs and start jobs for every combination of hyperparameters that is provided through this way.
In the example, we would get six configs, one of them would be:
```yaml
dataset:
    dataset_cls: ImageNet
    batch_size: 128
model:
    model_cls: resnet18
trainer:
    max_epochs: 200 
    optimizer:
        name: Lion
        lr: 0.001
        weight_decay: 0.05
```








