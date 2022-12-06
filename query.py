from elasticsearch import Elasticsearch

es = Elasticsearch( HOST = "http://localhost", PORT = 9200 )
es = Elasticsearch()

class elastic_query:    

    def elastic_match_query(self, query, index):
        body = {
    	    "from":0,
    	    "size":10,
    	    "query": {
        	    "match": {
       	    	    	"sentence":query
        		    }
    		    }
	    }

	    res = es.search(index = index, body=body)
	    return res


    def comb_query(query, index):
	body = {
    "from":0,
    "size":2,
    "query": {
        "bool": {
            "must_not": {
                "match": {
                    "sentence":"COVID-19"
                }
            },
            "should": {
                "match": {
                    "sentence": "Hack"
                }
            }
        }
    }
}

	res = es.search(index="getgoods", body=body)
	return(res)

def update_query(index, goodid ): 
	doc = {
 "GoodID" : "16370011",
          "Title" : "1812 год",
          "Slug" : "1812_god-g16370011",
          "BrandID" : "-21151",
          "Published" : "True",
          "DoUnpublish" : "",
          "Price" : "639",
          "DiscountPrice" : "320",
          "DiscountPercent" : "50",
          "RecommendedPrice" : "",
          "StorageCount" : "",
          "SEOTitle" : "1812 год, Клаузевиц К. - купить книгу по низким ценам с доставкой | Интернет-магазин «Белый кролик»",
          "SEODescription" : "Купить книгу 1812 год. Клаузевиц К. в интернет-магазине «Белый кролик» по лучшей цене. Акции, скидки, распродажи! Быстрая доставка по Москве и другим городам России.",
          "Keywords" : "1812 год клаузевиц к юрайт гуманитарная литература книги по гуманитарным наукам"
        }
	resp = client.update(index = index, id = goodid, document=doc)
	print(resp['result'])

def post_query(index, new_id):
	doc =  {
	 "GoodID" : "16370011",
          "Title" : "1812 год",
          "Slug" : "1812_god-g16370011",
          "BrandID" : "-21151",
          "Published" : "True",
          "DoUnpublish" : "",
          "Price" : "639",
          "DiscountPrice" : "320",
          "DiscountPercent" : "50",
          "RecommendedPrice" : "",
          "StorageCount" : "",
          "SEOTitle" : "1812 год, Клаузевиц К. - купить книгу по низким ценам с доставкой | Интернет-магазин «Белый кролик»",
          "SEODescription" : "Купить книгу 1812 год. Клаузевиц К. в интернет-магазине «Белый кролик» по лучшей цене. Акции, скидки, распродажи! Быстрая доставка по Москве и другим городам России.",
          "Keywords" : "1812 год клаузевиц к юрайт гуманитарная литература книги по гуманитарным наукам"
        }

	resp = es.index(index = index, id= new_id, document=doc)
	print(resp['result'])
