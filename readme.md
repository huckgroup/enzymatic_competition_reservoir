# A recursive enzymatic competition network capable of multi-task molecular information processing

Repository containing all data and code/notebooks relevant to the manuscript.

## Repository structure

- `data` contains the processed data to perform the various reservoir computation tasks
- `notebooks` contains notebooks used to perform the various reservoir computation tasks and for creation of all data-related figures in the publication.
- `plots` contain all data-related figures for the main manuscript (these are generated from the notebooks in the `notebooks` directory)

## Requirements

The code in this repository requires Python 3.12 together with a few standard packages (numpy, pandas, scikit-learn, etc...). 
All packages can be installed by creating a [Conda](https://docs.conda.io/en/latest/) environment from `environment.yaml`.

In the terminal, this environment can be created by running

```conda env create -f environment.yaml```

after which the environment can be activated by running:

```conda activate enzymatic_sensor```
