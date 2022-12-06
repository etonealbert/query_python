#!/bin/bash 

#read name

curl -XPUT 'http://localhost:9200/app?pretty '
-d  '{
"name":"Ivan",
"age" :"18",
"degree" : "90",
}'

