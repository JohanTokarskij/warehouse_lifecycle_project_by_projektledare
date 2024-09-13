import dlt
import requests
import json
import dlt

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




    

