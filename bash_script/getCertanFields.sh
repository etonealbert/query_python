#!/bin/bash 

curl -XGET '10.3.21.123:9200/merged/_search?pretty ' -H 'Content-Type: application/json'  -d '{ 
"_source" : [ "GoodID" ,"Price", "DiscountPrice", "DiscountPercent", 
                "Title", "Count", "Source"],
"query": {
    "bool" : {
            "must" : [
                {
                    "match" : {
                        "ICategoryID" : "528"
                    }
                }
            ]
        }
    }
}'

