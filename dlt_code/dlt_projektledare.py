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

@dlt.resource(write_disposition='replace')
def jobsearch_resource(params):
    url = 'https://jobsearch.api.jobtechdev.se'
    url_for_search = f'{url}/search'
    
    while True:
        ads_data = _get_ads(url_for_search, params)
        hits = ads_data.get('hits', [])

        for ad in hits:
            yield ad
        
        if len(hits) < params['limit']:
            break

        params['offset'] += params['limit']
    
def run_pipeline(query, table_name):
    pipeline = dlt.pipeline(
        pipeline_name='dlt_project_leader',
        destination='snowflake',
        dataset_name='staging',
    )    
    params = {'q': query, 'limit': 100, 'offset': 0}
    load_info = pipeline.run(jobsearch_resource(params=params), table_name=table_name)
    print(load_info)
    
if __name__ == '__main__':
    working_directory = Path(__file__).parent
    os.chdir(working_directory)
    
    query = 'projektledare'
    table_name = 'stg_project_leader_job_ads'
    
    run_pipeline(query, table_name)
