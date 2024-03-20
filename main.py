import requests


user_input = input("Para birimini giriniz: ")
def get_data():
    url = "https://hasanadiguzel.com.tr/api/kurgetir"
    response = requests.get(url)
    return response.json()

data = get_data()
for i in data["TCMB_AnlikKurBilgileri"]:
    if user_input == i["Isim"]:
        print(i["ForexBuying"])
        break
else:
    print("Veri Bu Listede Bulunmuyor.")
