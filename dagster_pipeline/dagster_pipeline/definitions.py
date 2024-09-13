from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import dbt_projektledare_dbt_assets, compute
from .project import dbt_projektledare_project
from .schedules import schedules

from dagster_embedded_elt.dlt import DagsterDltResource




defs = Definitions(
    assets=[compute, dbt_projektledare_dbt_assets],
    schedules=schedules,
    resources={
        "dlt": DagsterDltResource(),
        "dbt": DbtCliResource(project_dir=dbt_projektledare_project),
    },
)