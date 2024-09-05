import dlt
import requests
import json
import os
from pathlib import Path


def _get_ads(url_for_search, params):
    headers = {'accept': 'application/json'}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status()
    return json.loads(response.content.decode('utf8'))

@dlt.resource(write_disposition="replace")
def jobsearch_resource(
    params
):
    url = 'https://jobsearch.api.jobtechdev.se'
    url_for_search = f"{url}/search"
    
    for ad in _get_ads(url_for_search, params)["hits"]:
        yield ad
    
def run_pipeline(query, table_name):
    pipeline = dlt.pipeline(
        pipeline_name='dlt_project_leader',
        destination='snowflake',
        dataset_name='dlt_project_leader_data',
    )    
    params = {"q": query, "limit": 100}
    load_info = pipeline.run(jobsearch_resource(params=params), table_name=table_name)
    print(load_info)
    
if __name__ == "__main__":
    working_directory = Path(__file__).parent
    os.chdir(working_directory)
    
    query = "projektledare"
    table_name = "project_leader_job_ads"
    
    run_pipeline(query, table_name)
