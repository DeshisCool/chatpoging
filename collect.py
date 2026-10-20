import urllib.request,json,re,concurrent.futures,os,copy
from lxml import html,etree
from urllib.parse import urlparse,urljoin
root='/workspace/sites/limburgse-norm-desh/dist';base='https://limburgsenorm.nl'
slugs=['','handreiking','1-bewustwording-en-organisatie','2-integriteit-veilige-werkomgeving','3-veilige-publieke-taak','4-informatiepositie-informatiebeveiliging','5-beleid-en-handhaving','6-communicatie','checklist','productenoverzicht','bewustwording-organisatie','integriteit-veilige-werkomgeving','veilige-publieke-taak','informatiepositie-informatiebeveiliging','beleid-handhaving','communicatie','contact','cc-by-nc-nd-4-0-akte','proclaimer','privacy-policy','klachten']
assets={};issues=[]
def download(url):
 if url in assets:return assets[url]
 name=re.sub('[^a-zA-Z0-9._-]','_',urlparse(url).path.split('/')[-1]);path='/assets/'+name
 try:
  data=urllib.request.urlopen(url,timeout=25).read();open(root+path,'wb').write(data);assets[url]=path;return path
 except Exception as e:issues.append({'url':url,'error':str(e)});return url

def get(slug):
 url=base+'/'+slug+('/' if slug else '')
 raw=urllib.request.urlopen(url,timeout=35).read();doc=html.fromstring(raw)
 main=doc.xpath('//main')[0];title=' '.join(main.xpath('.//h1')[0].itertext()).strip();body=main.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," page-content ")]')[0]
 # unwrap layout while retaining semantic content, anchors and images
 for el in list(body.iter()):
  if el.tag in ['script','style','svg','i','iframe']:el.drop_tree();continue
  if el.tag=='img':
   src=el.get('src');el.attrib.clear()
   if src:el.set('src',download(urljoin(url,src)));el.set('alt','Piramide naar fitte gemeente' if slug=='handreiking' else title);el.set('loading','lazy')
   continue
  keep={k:v for k,v in el.attrib.items() if k in ['id','href','colspan','rowspan','title']};el.attrib.clear();el.attrib.update(keep)
 for el in list(body.iterdescendants())[::-1]:
  if el.tag in ['div','span','section']:el.drop_tag()
 for a in body.xpath('.//a[@href]'):
  href=a.get('href');parsed=urlparse(urljoin(url,href))
  if parsed.netloc=='limburgsenorm.nl':
   if '/wp-content/' in parsed.path:a.set('href',download(urljoin(url,href)))
   else:a.set('href',parsed.path.rstrip('/')+'/' if not parsed.fragment else parsed.path.rstrip('/')+'/'+ '#'+parsed.fragment)
  elif href.startswith(('http:','https:')):a.set('target','_blank');a.set('rel','noopener noreferrer')
 for el in body.xpath('.//p|.//h2|.//h3|.//a'):
  if not ''.join(el.itertext()).strip() and not el.get('id') and not len(el):el.drop_tree()
 content=(body.text or '')+''.join(etree.tostring(el,encoding='unicode',method='html') for el in body)
 text=' '.join(body.itertext());return {'slug':slug,'title':title,'html':content,'text':re.sub(r'\s+',' ',text).strip(),'source':url}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:pages=list(ex.map(get,slugs))
open(root+'/content.json','w').write(json.dumps(pages,ensure_ascii=False))
open('/workspace/sites/limburgse-norm-desh/source-report.json','w').write(json.dumps({'pages':[{ 'slug':p['slug'],'chars':len(p['text'])} for p in pages],'assets':assets,'issues':issues},indent=2))
print('Pages:',len(pages),'Assets:',len(assets),'Issues:',issues)
# official RIEC Limburg logo from original footer
source=html.parse('/tmp/source.html')
for im in source.xpath('//img'):
 src=im.get('src','')
 if 'RIEC_Limburg_Wit' in src:
  local=download(src);open(root+'/logo-path.json','w').write(json.dumps(local));print('Logo:',local);break
