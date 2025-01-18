from groq import Groq
import json

key = "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"

def analyze_code(file_content, file_name):
    prompt = f"""
            Analyze the code on these checks:
            - Code style and formatting issue
            - Potential bugs or errors
            - Performance improvements
            - Best Practices

    File: {file_name}
    Content: {file_content}

    Provide a detailed JSON output with the structure:
    {{
        "issues": [
            {{
                "type": "<style|bugs|performance|best_practice>",
                "line": <line_number>,
                "description": "<description>",
                "suggestion": "<suggestion>"
            }}
        ]
    }}
    """
    
    try:
        client = Groq(api_key=key)
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            top_p=1
        )

        response_content = completion.choices[0].message.content
        print(response_content)  # For debugging purposes

        # Attempt to parse the response as JSON
        try:
            response_json = json.loads(response_content)
            return response_json
        except json.JSONDecodeError:
            print("Failed to parse the response as JSON")
            return {"error": "Invalid JSON response"}
        
    except Exception as e:
        print(f"Error while analyzing code: {e}")
        return {"error": str(e)}
