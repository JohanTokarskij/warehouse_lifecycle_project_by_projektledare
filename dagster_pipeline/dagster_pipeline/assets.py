from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets
from .project import dbt_projektledare_project
from dlt import pipeline

from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from .source import job_ads
from .destination import aw_snowflake


@dlt_assets(
        dlt_source = job_ads(),
        dlt_pipeline = pipeline(
            pipeline_name='dlt_project_leader',
            destination=aw_snowflake,
            dataset_name='staging'
        )
)
def compute(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)

@dbt_assets(manifest=dbt_projektledare_project.manifest_path)
def dbt_projektledare_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    