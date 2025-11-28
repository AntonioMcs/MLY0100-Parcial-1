"""
Project settings. 
No necesitas modificarlo salvo que desees cambiar valores por defecto.
Documentación:
https://docs.kedro.org/en/stable/kedro_project_setup/settings.html
"""

# ==========================
# CONFIG LOADER
# ==========================
from kedro.config import OmegaConfigLoader  # noqa: E402

CONFIG_LOADER_CLASS = OmegaConfigLoader
CONFIG_LOADER_ARGS = {
    "base_env": "base",
    "default_run_env": "local",
}

# ==========================
# PIPELINE REGISTRY
# ==========================
# En Kedro 0.19+ ya NO se usa PipelineRegistry.
# Solo declaramos el diccionario PIPELINE_REGISTRY.

from mly0100parcial_kedro.pipelines.clustering import (
    create_pipeline as clustering_pipeline,
)

PIPELINE_REGISTRY = {
    "__default__": clustering_pipeline(),
    "clustering": clustering_pipeline(),
}

# ==========================
# OPCIONAL: HOOKS / SESSION / STORE
# (Déjalo vacío si no lo usas)
# ==========================

# HOOKS = ()
# SESSION_STORE_CLASS = None
# DATA_CATALOG_CLASS = None
