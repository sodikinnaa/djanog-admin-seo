import requests, json
from bs4 import BeautifulSoup

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJJc3N1ZXIgb2YgdGhlIEpXVCIsImF1ZCI6IkF1ZGllbmNlIHRoYXQgdGhlIEpXVCIsInN1YiI6IlN1YmplY3Qgb2YgdGhlIEpXVCIsImlhdCI6MTcyMDQxMjg4NCwiZXhwIjoxNzIzMDA0ODg0LCJlbWFpbCI6InNvZGlraW5AdGVrbm9rcmF0LmFjLmlkIn0.to_7OyavtLgLSYB2RVDZDq19ukGqmS8qoQ_E6Q0uyNs"

servers = "http://localhost:8080"
def getdataClient():
    headers = {
        'Authorization': f'Bearer {token}'
    }
    endpreq = servers+"/api/v2.0/client/"
    response = requests.get(endpreq, headers=headers)
    data = response.json()
    if(data['message']=="data Tidak ditemukan"):
        data = []               
        return data
    else:
        data = data['payload']['data']                
        data = {
            'client':data
        }
        return data
def getdata(endp):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    endpreq = servers+endp
    response = requests.get(endpreq, headers=headers)
    data = response.json()
    if(data['message']=="data Tidak ditemukan"):
        data = []               
        return data
    else:
        data = data['payload']['data']                
        return data
def dataArtikel(endp):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    endpreq = servers+endp
    response = requests.get(endpreq, headers=headers)
    data = response.json()
    if(data['message']=="Data Tidak Ditmukan"):
        return data['message']        
    else:
        data = data['payload']['data']                
        return data
    
# delete data
def deletedata(endpoint):
    enpreq = servers+endpoint
    headers = {
        'Authorization': f'Bearer {token}'        
    }
    print(enpreq)
    response = requests.delete(enpreq, headers=headers)
    data = response.json()
    if (data['message']=="Data Tidak Ditemukan"):
        data = data['message']
        return data    
    else:
        return "data berhasil di hapus"
# post data and scrape data artikel
def PostWenbsite(data, enp):
    enpreq = servers+enp
    headers = {
        'Authorization': f'Bearer {token}'        
    }
    response = requests.post(enpreq, json=data, headers=headers)
    dd(enpreq)
    if response.status_code == 200:
        return "data berhasil di kirimkan"
    else:
        return "data gagal di kirim"


def scrapeHeadData(url, idArtikel):
    import time
    try:
        while True:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.head.title
                title = title.get_text(strip=True) if title else 'Tidak ada judul'
                urlArtikel = title.lower().replace(' ', '-')
                deskripsi = ' '.join(p.get_text(strip=True) for p in soup.find_all('p')[:3]) if soup.find('p') else title
                meta = {meta_tag['name']: meta_tag['content'] for meta_tag in soup.find_all('meta') if 'name' in meta_tag.attrs and 'content' in meta_tag.attrs}
                break
            else:
                print("Gagal mengakses URL. Status code:", response.status_code, "Mencoba lagi dalam 10 detik.")
                print(url)
                time.sleep(10)
    except Exception as e:
        print("Error saat mengakses URL:", e)
    data = {
        
        'title': title,
        'meta': {key: value.strip() for key, value in meta.items()},
        'deskripsi':deskripsi
    }
    dataArtikel = {
        'idArtikel': idArtikel,
        'title_artikel': title,
        'meta_description': deskripsi,
        'link_artikel': urlArtikel,
    }
    
    return dataArtikel
# end artikel postt
# post data service
def postdata(enp, data):
    enpreq = servers+enp
    headers = {
        'Authorization': f'Bearer {token}'        
    }
    response = requests.post(enpreq, json=data, headers=headers)
    dd(enpreq)
    if response.status_code == 200:
        return "data berhasil di kirimkan"
    else:
        return "data gagal di kirim"
def putdata(enp, data):
    enpreq = servers+enp
    headers = {
        'Authorization': f'Bearer {token}'        
    }
    response = requests.put(enpreq, json=data, headers=headers)
    dd(enpreq)
    if response.status_code == 200:
        return "data berhasil di kirimkan"
    else:
        return "data gagal di kirim"
def dd(var):
    if isinstance(var, dict) or isinstance(var, list):
        # Gunakan json.dumps untuk mencetak dengan format yang rapi
        print(json.dumps(var, indent=4))
    else:
        # Tampilkan tipe dan nilai variabel
        print(f'Type: {type(var)}')
        print(f'Value: {repr(var)}')


# function tambahan
def getLasidArtikel():
    enp = "/api/v1.0/artikel/lastid"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    endpreq = servers+enp
    response = requests.get(endpreq, headers=headers)
    data = response.json()
    if(data['message']=="data Tidak ditemukan"):
        data = []               
        return data
    else:
        data = data['payload']['data']['id']['id_artikel']
        return data