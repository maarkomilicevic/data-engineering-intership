Komande AWS CLI:

1. Za kreiranje DYnamo tabele: 
aws dynamodb create-table 
--table-name dynamo 
--attribute-definitions AttributeName=Int,AttributeType=N AttributeName=Broj,AttributeType=S 
--key-schema AttributeName=Int,KeyType=HASH AttributeName=Broj,KeyType=RANGE 
--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 
--region eu-west-1

2. Za podesavanje point-in-time-recovery:
aws dynamodb update-continuous-backups --table-name dynamo --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true

3. Za podesavanje TTL:
aws dynamodb update-time-to-live --table-name dynamo --time-to-live-specification "Enabled=true, AttributeName=ExpirationTime

4. Za insertovanje u dynamo tabelu:
aws dynamodb put-item --table-name dynamo 
--item '{
    "Int": {"N": "1"},
    "Broj": {"S": "A1"},
    "Name": {"S": "Alice"},
    "Age": {"N": "30"}
}'


5. Za pretrazivanje u dynamo tabeli:
aws dynamodb query --table-name dynamo --key-condition-expression "#Int = :partitionKeyVal" --expression-attribute-names "{\"#Int\": \"Int\"}" --expression-attribute-values "{\":partitionKeyVal\": {\"N\": \"1\"}}" --scan-index-forward --region eu-west-1


6. Za pretrazivanje uz filtriranje:

aws dynamodb query --table-name dynamo --key-condition-expression "#Int=:partitionKeyVal" --expression-attribute-names "{\"#Int\":\"Int\"}" --expression-attribute-values "{\"partitionKeyVal\":{\"N\":\"1\"},\":age\":{\"N\":\"5\"}}" --filter-expression "Age>:age" --region eu-west-1


