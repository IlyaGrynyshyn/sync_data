from app.services.api_client import ApiClient

api_client = ApiClient()



def get_ova_data(year, quarter):
    return api_client.get(
        url=f"https://guide.diia.gov.ua/api/v1/static_reports/list/{year}/{quarter}/?format=json"
    )




# https://guide.diia.gov.ua/api/v1/static_reports/list/<year>/<quarter>/?format=json
# https://guide.diia.gov.ua/api/v1/static_reports/entries/<report_id>?format=json
# https://guide.diia.gov.ua/api/v1/static_reports/detail/<report_entries_id>

