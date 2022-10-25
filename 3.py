from dataclasses import dataclass, field
import requests

@dataclass
class extension:
    extension: list[str] = field(default_factory=list)
    url: list[str] = field(default_factory=list)

    def set_extensions(self, extension: str):
        self.extension = extension

    def set_url(self, url: str):
        self.url = url
@dataclass
class extensions:
    ext_list : list[extension] = field(default_factory=list)


list_ext = extensions()

def get_name_ext():

    url="https://www.mediawiki.org/w/api.php"
    params = {
    'action': 'query',
    'format':'json',
    'meta':'siteinfo',
    'formatversion':2,
    'siprop':'extensions'
    }
    resp = requests.get(url,params).json() 
    resp = resp['query']['extensions']
    for ext in resp:
        new_ext = extension()
        if 'url' in ext:
            exte = ext['name']
            url=ext['url']
            new_ext.set_extensions(exte),new_ext.set_url(url)
            list_ext.ext_list.append(new_ext)
    
get_name_ext()

print(type(list_ext.ext_list))
urls = []
for i,v in enumerate(list_ext.ext_list):
    extensoes=list_ext.ext_list[i]
    urls.append(f"https://www.mediawiki.org/w/api.php?action=query&list=extdistbranches&edbexts={extensoes.extension}&format=json")
                  
for url in urls:
    resp = requests.get(url).json() 
    print(resp)