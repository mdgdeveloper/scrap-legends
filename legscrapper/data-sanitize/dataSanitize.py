# Data Sanitizer
from sanitizer import *


def locationData(village):
    village = village.lower()
    print(f"Village: {village}")
    base_api = f"https://data.opendatasoft.com/api/records/1.0/search/?dataset=georef-spain-municipio%40public&q={village}&facet=year&facet=acom_code&facet=acom_name&facet=prov_code&facet=prov_name&facet=mun_code&facet=mun_name&facet=mun_area_code&facet=mun_type"
    data = get_json_from_api(base_api)
    result = ["", ""]
    if (data["records"]):
        result = [data["records"][0]["fields"]["prov_name"],
                  data["records"][0]["fields"]["acom_name"]]

    return (result)
