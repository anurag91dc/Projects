import json

def Calc_handler(event, context):
    # text = '400 Invalid Input !!' + str(event.values())
    # return {
    #         'statusCode': 400,
    #         'body': json.dumps(text) 
    #     }
    if not event or len(event) < 3 or event['Num1'] == "" or event['Num2'] == "" or event['Operator'] == "":
        text = '400 Invalid Input !!'
        return {
            'statusCode': 400,
            'body': json.dumps(text) 
        }
    if event['Num2']== '0' and event['Operator'] == "/":
        return {
            'statusCode': 400,
            'body': json.dumps("Division by 0 is not allowed") 
        }
        
    if event['Operator'] not in "+-*/":
        return {
            'statusCode': 400,
            'body': json.dumps("Not a supported Operation") 
        }
    
    else:
        if event['Operator'] == '+': 
            result = int(event['Num1']) + int(event['Num2'])
        elif event['Operator'] == '-': 
            result = int(event['Num1']) - int(event['Num2'])
        elif event['Operator'] == '*':
            result = int(event['Num1']) * int(event['Num2'])
        elif event['Operator'] == '/':
            result = int(event['Num1']) / int(event['Num2'])
        else:
            result = "Error"
        
        event['Result'] = str(result)
        
        return {
            'statusCode': 200,
            'body': event
        }