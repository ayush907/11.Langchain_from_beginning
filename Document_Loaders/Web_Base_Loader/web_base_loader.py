from langchain_community.document_loaders import WebBaseLoader

url1 = "https://www.flipkart.com/redmi-a3x-midnight-black-128-gb/p/itmae02f9f3f765a?pid=MOBH22XZZBQHFVS2&lid=LSTMOBH22XZZBQHFVS2ZJBVLP&marketplace=FLIPKART&q=mobile&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=organic&iid=d32e1310-1fac-4b39-9b4d-3a734f3d504a.MOBH22XZZBQHFVS2.SEARCH&ppt=hp&ppn=homepage&ssid=tq9c5k7idc0000001744526792703&qH=532c28d5412dd75b"

url2 = "https://www.flipkart.com/samsung-183-l-direct-cool-single-door-4-star-refrigerator-base-drawer-digital-inverter/p/itmff9626696387c?pid=RFRGHJPXZBG6Z7XY&lid=LSTRFRGHJPXZBG6Z7XYLWPRXX&marketplace=FLIPKART&q=refrigerator&store=j9e%2Fabm%2Fhzg&spotlightTagId=default_FkPickId_j9e%2Fabm%2Fhzg&srno=s_1_5&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&fm=search-autosuggest&iid=9fff95af-5b13-446f-ad19-cf867b729c10.RFRGHJPXZBG6Z7XY.SEARCH&ppt=sp&ppn=sp&ssid=lw9czfzcg00000001744527247462&qH=945c050322f005b6"

url3 = "https://www.flipkart.com/red-tape-casual-sneaker-shoes-men-combining-style-comfort-lace-up-design-sneakers/p/itm84d12e2b58f92?pid=SHOGSZYVPZBHVATG&lid=LSTSHOGSZYVPZBHVATGXSEXIA&marketplace=FLIPKART&q=redtape+shoes+black+white&store=osp%2Fcil&srno=s_1_13&otracker=search&otracker1=search&fm=search-autosuggest&iid=2022d3ef-fe9d-4a2e-8a92-216df11b8051.SHOGSZYVPZBHVATG.SEARCH&ppt=sp&ppn=sp&ssid=aimfqgcf2o0000001744527318024&qH=87de78778cb04780"

# loader = WebBaseLoader(url1)

loader = WebBaseLoader([url1, url2, url3])

docs = loader.load()

print(len(docs))

print(docs[0].page_content)