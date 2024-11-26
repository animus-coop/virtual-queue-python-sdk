from importlib import resources

try:
    import tomllib  # type:ignore
except ModuleNotFoundError:
    import tomli as tomllib  # type:ignore

_cfg = tomllib.loads(resources.read_text("virtualqueue_sdk", "config.toml"))

API_BASE_PATH = _cfg["api"]["base_path"]
