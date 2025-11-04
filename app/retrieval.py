import requests
import xml.etree.ElementTree as ET
from urllib.parse import quote_plus

def fetch_pubmed_ids(query, max_results=20):
    q = quote_plus(query)
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={q}&retmode=json&retmax={max_results}&sort=date"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    ids = r.json().get("esearchresult", {}).get("idlist", [])
    return ids

def fetch_pubmed_details(pmid_list):
    ids = ",".join(pmid_list)
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={ids}&retmode=xml"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    root = ET.fromstring(r.text)
    papers = []
    for art in root.findall(".//PubmedArticle"):
        pmid = art.findtext(".//PMID")
        title = art.findtext(".//ArticleTitle") or ""
        abstract_nodes = art.findall(".//AbstractText")
        abstract = " ".join([ (n.text or "") for n in abstract_nodes ])
        year = art.findtext(".//PubDate/Year") or ""
        papers.append(dict(pmid=pmid, title=title, abstract=abstract, year=year))
    return papers

def fetch_papers_for_query(query, max_results=20):
    ids = fetch_pubmed_ids(query, max_results=max_results)
    if not ids:
        return []
    return fetch_pubmed_details(ids)
