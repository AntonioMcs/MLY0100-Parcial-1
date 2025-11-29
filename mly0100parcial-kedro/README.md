# mly0100parcial_kedro

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## Overview

This is your new Kedro project, which was generated using `kedro 1.0.0`.

Take a look at the [Kedro documentation](https://docs.kedro.org) to get started.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://docs.kedro.org/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `requirements.txt` for `pip` installation.

To install them, run:

```
pip install -r requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## 🚢 Run with Docker

The repository now includes a `Dockerfile` and `docker-compose.yml` so you can run Kedro without managing Python locally.

1. Move into the project folder and build the image:
   ```bash
   cd mly0100parcial-kedro
   docker compose build
   ```
2. Execute any Kedro command inside the container (data and `conf/local` are mounted as volumes):
   ```bash
   # Run full pipeline
   docker compose run --rm kedro kedro run

   # Run a specific pipeline
   docker compose run --rm kedro kedro run --pipeline diabetes

   # Open a shell inside the container
   docker compose run --rm kedro bash
   ```
3. To launch Kedro-Viz expose the port when running:
   ```bash
   docker compose run --rm -p 4141:4141 kedro kedro viz --host 0.0.0.0 --port 4141
   ```

## ☁️ Run with Airflow

You can orchestrate the Kedro pipelines from Apache Airflow using the DAG provided in `airflow_dags/diabetes_kedro_dag.py`.

1. Copy (or mount) the entire repo under your Airflow `dags/` directory. By default, the DAG expects the project to be in `/opt/airflow/dags/mly0100parcial-kedro`.
2. Install Kedro and project dependencies inside the Airflow environment, e.g.:
   ```bash
   pip install -r requirements.txt
   ```
3. Set the environment variable `KEDRO_PROJECT_PATH` if you colocate the project elsewhere:
   ```bash
   export KEDRO_PROJECT_PATH=/path/to/mly0100parcial-kedro
   ```
4. Start Airflow:
   ```bash
   airflow db init
   airflow webserver -p 8080
   airflow scheduler
   ```
5. In the Airflow UI, enable the DAG `kedro_diabetes_pipeline`. The DAG runs `kedro run --pipeline diabetes`, then `unsupervised_learning` and `reporting`. You can also trigger it manually.

This setup lets you reuse the same Kedro commands inside Airflow, keeping observability (logs, retries, scheduling) in one place.

## How to test your Kedro project

Have a look at the files `tests/test_run.py` and `tests/pipelines/data_science/test_pipeline.py` for instructions on how to write your tests. Run the tests as follows:

```
pytest
```

You can configure the coverage threshold in your project's `pyproject.toml` file under the `[tool.coverage.report]` section.

## Project dependencies

To see and update the dependency requirements for your project use `requirements.txt`. You can install the project requirements with `pip install -r requirements.txt`.

[Further information about project dependencies](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `catalog`, `context`, `pipelines` and `session`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, you can add a hook in `.git/config` with `nbstripout --install`. This will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html)
