import json
import urllib.request

def lambda_handler(event, context):
    # 🚨 SECURITY: Apne asli webhook URL ki jagah yahan placeholder daalna chahiye GitHub par
    WEBHOOK_URL = "https://discord.com/api/webhooks/1497825058733822105/L1zDTjMQ5-tejY_shAiChxTUwEGpxsvJ7Y99NgwLsRO4kGCyEuQPmcsCUjA0-hC504ql"
    
    # Message jo Discord par jayegi
    message_content = "Hello from AWS! Serverless Lambda triggered successfully. 🚀"
    
    payload = {
        "content": message_content,
        "username": "AWS Cloud Architect Bot"
    }
    
    # JSON data ko encode karna Discord ke liye
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(WEBHOOK_URL, data=data, headers={
        'Content-Type': 'application/json', 
        'User-Agent': 'Mozilla/5.0'
    })
    
    try:
        # Request bhejna
        with urllib.request.urlopen(req) as response:
            return {
                'statusCode': 200,
                'body': json.dumps('Message sent to Discord!')
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
