import json, urllib.request, xml.etree.ElementTree as ET
host="vegita786-rgb.github.io"
key="1edfb5cae1864a1b83ed3f0395c97b43"
keyloc=f"https://{host}/trippick/{key}.txt"
root=ET.parse("sitemap.xml").getroot()
ns={"s":"http://www.sitemaps.org/schemas/sitemap/0.9"}
urls=[n.text.strip() for n in root.findall("s:url/s:loc",ns) if n.text]
payload=json.dumps({"host":host,"key":key,"keyLocation":keyloc,"urlList":urls}).encode()
req=urllib.request.Request("https://api.indexnow.org/indexnow",data=payload,headers={"Content-Type":"application/json; charset=utf-8"},method="POST")
with urllib.request.urlopen(req,timeout=30) as r:
    print("IndexNow",r.status,"URLs",len(urls))
