# Data Sanitizer
from sanitizer import *

# Test
base_api = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=georef-spain-municipio%40public&q=picassent&facet=year&facet=acom_code&facet=acom_name&facet=prov_code&facet=prov_name&facet=mun_code&facet=mun_name&facet=mun_area_code&facet=mun_type"

test = get_json_from_api(base_api)

print(test)
