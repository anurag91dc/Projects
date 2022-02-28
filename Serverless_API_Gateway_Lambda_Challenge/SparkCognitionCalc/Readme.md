## Steps to deploy the Serverless Lambda API on AWS API Gateway - 
    1) Install Node, and then serverless through npm package manager.
    2) Pull this git repository on your local machine
    3) Run the command serverless deploy on the the same folder
    4) You should receive a random URL and API key.  

## Steps to call this API from Postman - 
    1) Select GET method and use the Random URL generated -  "https://6iqyibt6lc.execute-api.us-east-1.amazonaws.com/Prod" for example.
    2) Add API Path to the URL string - "/Calc"
    3) Add query Parameters - ?Num1=< First Number >&Operator=< + or - or * or / >&Num2=< Second Number >
    4) Add x-api-key and the API key that is generated on deployment.
    5) Now send the request from Postman - You should receive something like this - 

            {
                "statusCode": 200, 
                "body": {
                    "Num1": "23", 
                    "Num2": "33", 
                    "Operator": "+", 
                    "Result": "56"
                    }
            }

###  NOTE IMP - For only "+" Operand select the character + in the URL and right click and choose 
                "encode uri parameter" option before executing the API call. This needs to be done 
                as + has a special meaning to URLs and gets converted to a space if it is not encoded. 
                This issue can be solved by using the POST method but for the scope of this question 
                only GET method is required. For other operations the symbols - * and / can be used 
                without any issues.
 