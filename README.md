# Ray Demo Model Serving

This repository contains the basic structure that a model serving application should have. This implementation is based on the [Ray Serve](https://docs.ray.io/en/master/serve/index.html) framework. It not only provides a simple way to deploy a model, but also provides a way to scale the model to multiple instances.

## How to run

1. Install ray serve on your machine

```bash
pip install ray[serve]
```

2. Create the head node

```bash
 ray start --head --block --dashboard-host 0.0.0.0
Usage stats collection is enabled. To disable this, add `--disable-usage-stats` to the command that starts the cluster, or run the following command: `ray disable-usage-stats` before starting the cluster. See https://docs.ray.io/en/master/cluster/usage-stats.html for more details.

Local node IP: XX.XX.XX.XX

--------------------
Ray runtime started.
--------------------

Next steps
  To connect to this Ray runtime from another node, run
    ray start --address='XX.XX.XX.XX:6379'

  Alternatively, use the following Python code:
    import ray
    ray.init(address='auto')

  To connect to this Ray runtime from outside of the cluster, for example to
  connect to a remote cluster from your laptop directly, use the following
  Python code:
    import ray
    ray.init(address='ray://<head_node_ip_address>:10001')

  If connection fails, check your firewall settings and network configuration.

  To terminate the Ray runtime, run
    ray stop

--block
  This command will now block forever until terminated by a signal.
  Running subprocesses are monitored and a message will be printed if any of them terminate unexpectedly. Subprocesses exit with SIGTERM will be treated as graceful, thus NOT reported.
```

3. Install the dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python3 backend/main.py
```

## How to test

1. Run the test

```bash
python3 -m pytest tests
```

## Links of interest

- `routes of the application`: `http://localhost:8000/-/routes`
- `dashboard`: `http://localhost:8265`
- `documentation`: `https://docs.ray.io/en/master/serve/index.html`

## Environment variables

|                  Name                  |                          Default Value                          | Overwrite required | Description                                     |                           Reference                            |
| :------------------------------------: | :-------------------------------------------------------------: | :----------------: | ----------------------------------------------- | :------------------------------------------------------------: |
| `SETTINGS_MODULE_ENVIRONMENT_VARIABLE` |                        `config.settings`                        |        Yes         | The path to the settings module of your project | [Backend Base](https://github.com/Carlososuna11/backend-base/) |
|                `DEBUG`                 |                             `True`                              |         No         | If the application is running in debug mode     | [Backend Base](https://github.com/Carlososuna11/backend-base/) |
|             `PROJECT_NAME`             |                  `DEMO MULTIPLE MODEL SERVING`                  |         No         | The name of the project                         |                                                                |
|         `PROJECT_DESCRIPTION`          | `This is a demo of how to serve multiple models with Ray Serve` |         No         | The description of the project                  |                                                                |
|           `PROJECT_VERSION`            |                             `0.0.1`                             |         No         | The version of the project                      |                                                                |
|             `RAY_ADDRESS`              |                             `auto`                              |         No         | The address of the ray cluster                  |  [Ray Serve](https://docs.ray.io/en/master/serve/index.html)   |
