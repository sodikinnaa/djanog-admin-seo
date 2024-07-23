from django.shortcuts import render, redirect
from django.http import HttpResponse
from .helpers.global_function import *
from io import TextIOWrapper

# Create your views here.
def home(request):
    enpoint = "/api/v2.0/client"
    data = getdata(enpoint)
    return render(request, 'daftar_master.html', {'content':data})

# codingan master 
def editMaster(request, id_master):
    enp = f"/api/v2.0/client/{id_master}"
    data = getdata(enp)
    data = data[0]
    if request.method == "POST":
        nm_website = request.POST.get('nama_master')
        url_website = request.POST.get('url_master')
        enp = f"/api/v2.0/client/{id_master}"
        
        data = {
            
            "nm_client": nm_website,
            "url_client": url_website
        }
        save = putdata(enp, data)
        dd(save)
        if(save):
            return redirect('/')
        else:
            return HttpResponse(f'update website {data} gagal di update')
    return render(request, 'edit_master.html', {'content':data})

def addMaster(request):
    if request.method == "POST":
        nm_website = request.POST.get('nama_master')
        url_website = request.POST.get('url_master')
        data = {
            'nm_client': nm_website,
            'url_client': url_website
        }
        enpoint = "/api/v2.0/client"
        save = postdata(enpoint, data)
        dd(data)
        print(enpoint)
        if (save):
            return redirect('/')
        else:
            return HttpResponse('data gagal di simpan')
    return render(request, 'add_master.html')

# code daftar website
def deleteMaster(request, id_website):
    enpoint = f"/api/v2.0/client/{id_website}"
    delete = deletedata(enpoint)
    
    dd(id_master)
    return redirect('/')

def daftarWebsite(request, id_master):
    endpoint = f"/api/v2.0/website/client/{id_master}"
    data = getdata(endpoint)
    
    return render(request, 'daftar_website.html', {'content':data})
    return HttpResponse(f'get artikel {data}')

def deleteWebsite(request, id_website):
    enpoint = f"/api/v2.0/website/{id_website}"
    enp_detail = f"/api/v2.0/website/{id_website}"
    master = getdata(enp_detail)
    id_client = master[0]['id_client']
    redenp = f"/website/{id_client}"
    delete = deletedata(enpoint)
    # delete = []
    if(delete):
        return redirect(redenp)
    else : 
        return HttpResponse(f'Data gagal di hapus {redenp}')
def editWebsite(requests, id_website):
    return HttpResponse('edit website')

def getWebsiteArtikel(request, id_website):
    endpoint = f"/api/v2.0/artikel-show?param={id_website}"
    enpoint = f"/api/v1.0/website/{id_website}"
    last_id = getLasidArtikel()
    
    data = dataArtikel(endpoint)
    
    if (data=="Data Tidak Ditmukan"):
        data = []
    
    return render(request, 'daftar_artikel.html', {'content':data, 'id_artikel':last_id, 'id_website':id_website})
    return HttpResponse(f'artikel {data}')

def addWebsite(request):
    if request.method == 'POST':
        nm_website = request.POST.get('nama_website')
        url_website = request.POST.get('url_website')
        id_client = request.POST.get('id_master')
        data = {
            'nm_website':	nm_website,
            'url_website':	url_website,            
            'id_client':	id_client,
        }
        enpoint = "/api/v2.0/website"
        save = postdata(enpoint, data)
        if (save):
            return redirect(f'/website/{id_client}')
        else :
            return HttpResponse(f'data gagal di simpan {save}')
            
    
    data = getdataClient()
    
    return render(request, 'add_website.html', {'content':data})


    
    
   
    # return HttpResponse(f'{delete} <br> <a href="/">Kembali</a>')
   
# codingan artikel 
def addArtikel(request):
    return render(request, 'add_artikel.html')


# scrape artikel
def postdataArtikel(request, id_website):
    data = {}
    if request.method == 'POST':
        idArtikel = getLasidArtikel()
        idWebsite = id_website
        endpredirect = "/artikel/" + idWebsite
        fileTXT = request.FILES.get('fileTXT', None)
        
        endpArtikel = "/api/v2.0/artikel"

        endpWebsite = "/api/v2.0/artikel-show"
        
        if fileTXT:                    
            with TextIOWrapper(fileTXT, encoding='utf-8') as file:
                lines = file.readlines()    
                # Proses kolom data yang ada di TXT dengan BeautifulSoup untuk mengekstrak title                
                for line in lines:
                    namaDomain = line.strip()  # Mengambil data dari setiap baris
                    dataArtikel = scrapeHeadData(namaDomain, idArtikel)  
                     
                    data = {
                        'id_website': idWebsite,
                        'id_artikel': idArtikel,
                    }
                    
                    save = PostWenbsite(dataArtikel, endpArtikel)
                    if save:
                        save = PostWenbsite(data, endpWebsite)
                        dd(save)
                    idArtikel = int(idArtikel) + 1 
                    dd(dataArtikel)
                    dd(data)  
                                                     
        else:
            titleArtikel = request.POST.get('title_artikel', 'DefaultValue')
            metaArtikel = request.POST.get('meta_artikel', 'DefaultValue')
            urlArtikel = titleArtikel.lower().replace(' ', '-')
            dataArtikel = {
                'title_artikel': titleArtikel,
                'meta_description': metaArtikel,
                'link_artikel': urlArtikel
            }
            dd(dataArtikel)
            
            save = PostWenbsite(dataArtikel, endpArtikel)
            data = {
                                        'id_website': idWebsite,
                                        'id_artikel': idArtikel,
                                    }
            
            if save:
                save = PostWenbsite(data, endpWebsite)
                dd(save)
                return redirect(endpredirect)
            
            dd(save)
        # return HttpResponse('post artikel')
        
        return redirect(endpredirect)
    else:
        # return HttpResponse('post artikel via txt')
        
        return redirect(endpredirect)