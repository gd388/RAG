from groq import Groq

key = "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"

def analyze_code(file_content,file_name):
    prompt = f"""
            Analyze the code on these checks:
            -Code style and formatting issue
            -Potential bugs or error 
            -Performance improvements
            -Best Practices

    File : {file_name})
    Content : {file_content}

    provide a detailed Json output with the structure : 
        {{"issues" :
        [
            {{
                "type" : "<style|bugs|performance|best_practice>",
                "line" : <line_number>,
                "description" : "<description>",
                "suggestion" : "<suggestion>"
            }}
        ]
        }}
    """
    '''json
    '''
    client = Groq(
        api_key=key
    )
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages= [
            {
                "role" : "user",
                "content" : prompt
            }
        ],
        temperature=1,
        top_p=1

    )
    
    print(completion.choices[0].message.content)
