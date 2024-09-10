from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import dbt_projektledare_dbt_assets
from .project import dbt_projektledare_project
from .schedules import schedules

defs = Definitions(
    assets=[dbt_projektledare_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=dbt_projektledare_project),
    },
)