from pathlib import Path

from dagster_dbt import DbtProject

dbt_projektledare_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "dbt_code").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
dbt_projektledare_project.prepare_if_dev()