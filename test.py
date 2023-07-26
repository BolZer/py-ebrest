from easybill_rest import Client

client = Client("u9NWgHLUwQWXNsJRq1l8dl5jdNGSOYCj6mI66yOgx2ETxYOeViCEEtaQPwulEhjP")
result = client.documents().get_document("2509811976")
print(result)
