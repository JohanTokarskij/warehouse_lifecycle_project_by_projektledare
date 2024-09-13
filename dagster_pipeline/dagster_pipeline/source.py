import dlt
import requests
import json

import dlt



""" #Fetches ads from the API
def _get_ads(url_for_search, params):
    headers = {'accept': 'application/json'}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status()
    return json.loads(response.content.decode('utf8'))

#Specifies the base url and the ad search
@dlt.resource(write_disposition='replace')
def jobsearch_resource(params):
    url = 'https://jobsearch.api.jobtechdev.se'
    url_for_search = f'{url}/search'


#Yields ads until there are no more available
    while True:
        ads_data = _get_ads(url_for_search, params)
        hits = ads_data.get('hits', [])

        #Yield each ad
        for ad in hits:
            yield ad
        
        #If the amount of ads is less than the offset
        if len(hits) < params['limit']:
            break

        #Update offset for the next API fetch
        params['offset'] += params['limit']
    
    
#Extracts and loads data into Snowflake    
def run_pipeline(query, table_name):
    pipeline = dlt.pipeline(
        pipeline_name='dlt_project_leader',
        destination='snowflake',
        dataset_name='staging',
    )    
    #Job search parameters
    params = {'q': query, 'limit': 100, 'offset': 0}
    
    #Run pipeline and print the load information
    load_info = pipeline.run(jobsearch_resource(params=params), table_name=table_name)
    print(load_info)


#Set the directory to where the script is located    
if __name__ == '__main__':
    working_directory = Path(__file__).parent
    os.chdir(working_directory)
    
    #Define the search query and Snowflake table name
    query = 'projektledare'
    table_name = 'stg_project_leader_job_ads'
    
    #Executes the pipeline
    run_pipeline(query, table_name) """

ENDPOINT_URL = 'https://jobsearch.api.jobtechdev.se/search'


@dlt.source
def project_leader():
    def get_all_pages(endpoint_url):
        headers = {'accept': 'application/json'}
        params = {'q': 'projektledare', 'limit': 100, 'offset': 0}
        all_ads = []
        
        while True:
            response = requests.get(endpoint_url, headers=headers, params=params)
            response.raise_for_status()
            ads_data = json.loads(response.content.decode('utf8'))
            hits = ads_data.get('hits', [])
            
            all_ads.extend(hits)
            
            if len(hits) < params['limit']:
                break
            
            params['offset'] += params['limit']
        
        return all_ads

    def stg_job_ads(endpoint_url):
        all_ads = get_all_pages(endpoint_url)

        for ad in all_ads:
            yield ad

    yield dlt.resource(
        stg_job_ads(ENDPOINT_URL),
        write_disposition='replace'
    )




    

