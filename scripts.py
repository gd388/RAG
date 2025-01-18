import base64


code = "IiIiCkRqYW5nbyBzZXR0aW5ncyBmb3IgY29yZSBwcm9qZWN0LgoKR2VuZXJh\ndGVkIGJ5ICdkamFuZ28tYWRtaW4gc3RhcnRwcm9qZWN0JyB1c2luZyBEamFu\nZ28gNS4xLjUuCgpGb3IgbW9yZSBpbmZvcm1hdGlvbiBvbiB0aGlzIGZpbGUs\nIHNlZQpodHRwczovL2RvY3MuZGphbmdvcHJvamVjdC5jb20vZW4vNS4xL3Rv\ncGljcy9zZXR0aW5ncy8KCkZvciB0aGUgZnVsbCBsaXN0IG9mIHNldHRpbmdz\nIGFuZCB0aGVpciB2YWx1ZXMsIHNlZQpodHRwczovL2RvY3MuZGphbmdvcHJv\namVjdC5jb20vZW4vNS4xL3JlZi9zZXR0aW5ncy8KIiIiCgpmcm9tIHBhdGhs\naWIgaW1wb3J0IFBhdGgKCiMgQnVpbGQgcGF0aHMgaW5zaWRlIHRoZSBwcm9q\nZWN0IGxpa2UgdGhpczogQkFTRV9ESVIgLyAnc3ViZGlyJy4KQkFTRV9ESVIg\nPSBQYXRoKF9fZmlsZV9fKS5yZXNvbHZlKCkucGFyZW50LnBhcmVudAoKCiMg\nUXVpY2stc3RhcnQgZGV2ZWxvcG1lbnQgc2V0dGluZ3MgLSB1bnN1aXRhYmxl\nIGZvciBwcm9kdWN0aW9uCiMgU2VlIGh0dHBzOi8vZG9jcy5kamFuZ29wcm9q\nZWN0LmNvbS9lbi81LjEvaG93dG8vZGVwbG95bWVudC9jaGVja2xpc3QvCgoj\nIFNFQ1VSSVRZIFdBUk5JTkc6IGtlZXAgdGhlIHNlY3JldCBrZXkgdXNlZCBp\nbiBwcm9kdWN0aW9uIHNlY3JldCEKU0VDUkVUX0tFWSA9ICdkamFuZ28taW5z\nZWN1cmUtamgoeC0zYnZ4KzI4bDJxJkB6cXJua3YmLTB1bioyemYodnB4M2E1\nZWxeNGRmayVyOConCgojIFNFQ1VSSVRZIFdBUk5JTkc6IGRvbid0IHJ1biB3\naXRoIGRlYnVnIHR1cm5lZCBvbiBpbiBwcm9kdWN0aW9uIQpERUJVRyA9IFRy\ndWUKCkFMTE9XRURfSE9TVFMgPSBbXQoKCiMgQXBwbGljYXRpb24gZGVmaW5p\ndGlvbgoKSU5TVEFMTEVEX0FQUFMgPSBbCiAgICAnZGphbmdvLmNvbnRyaWIu\nYWRtaW4nLAogICAgJ2RqYW5nby5jb250cmliLmF1dGgnLAogICAgJ2RqYW5n\nby5jb250cmliLmNvbnRlbnR0eXBlcycsCiAgICAnZGphbmdvLmNvbnRyaWIu\nc2Vzc2lvbnMnLAogICAgJ2RqYW5nby5jb250cmliLm1lc3NhZ2VzJywKICAg\nICdkamFuZ28uY29udHJpYi5zdGF0aWNmaWxlcycsCiAgICAncmVzdF9mcmFt\nZXdvcmsnLAogICAgJ215YXBwJywKXQoKTUlERExFV0FSRSA9IFsKICAgICdk\namFuZ28ubWlkZGxld2FyZS5zZWN1cml0eS5TZWN1cml0eU1pZGRsZXdhcmUn\nLAogICAgJ2RqYW5nby5jb250cmliLnNlc3Npb25zLm1pZGRsZXdhcmUuU2Vz\nc2lvbk1pZGRsZXdhcmUnLAogICAgJ2RqYW5nby5taWRkbGV3YXJlLmNvbW1v\nbi5Db21tb25NaWRkbGV3YXJlJywKICAgICdkamFuZ28ubWlkZGxld2FyZS5j\nc3JmLkNzcmZWaWV3TWlkZGxld2FyZScsCiAgICAnZGphbmdvLmNvbnRyaWIu\nYXV0aC5taWRkbGV3YXJlLkF1dGhlbnRpY2F0aW9uTWlkZGxld2FyZScsCiAg\nICAnZGphbmdvLmNvbnRyaWIubWVzc2FnZXMubWlkZGxld2FyZS5NZXNzYWdl\nTWlkZGxld2FyZScsCiAgICAnZGphbmdvLm1pZGRsZXdhcmUuY2xpY2tqYWNr\naW5nLlhGcmFtZU9wdGlvbnNNaWRkbGV3YXJlJywKXQoKUk9PVF9VUkxDT05G\nID0gJ2NvcmUudXJscycKClRFTVBMQVRFUyA9IFsKICAgIHsKICAgICAgICAn\nQkFDS0VORCc6ICdkamFuZ28udGVtcGxhdGUuYmFja2VuZHMuZGphbmdvLkRq\nYW5nb1RlbXBsYXRlcycsCiAgICAgICAgJ0RJUlMnOiBbXSwKICAgICAgICAn\nQVBQX0RJUlMnOiBUcnVlLAogICAgICAgICdPUFRJT05TJzogewogICAgICAg\nICAgICAnY29udGV4dF9wcm9jZXNzb3JzJzogWwogICAgICAgICAgICAgICAg\nJ2RqYW5nby50ZW1wbGF0ZS5jb250ZXh0X3Byb2Nlc3NvcnMuZGVidWcnLAog\nICAgICAgICAgICAgICAgJ2RqYW5nby50ZW1wbGF0ZS5jb250ZXh0X3Byb2Nl\nc3NvcnMucmVxdWVzdCcsCiAgICAgICAgICAgICAgICAnZGphbmdvLmNvbnRy\naWIuYXV0aC5jb250ZXh0X3Byb2Nlc3NvcnMuYXV0aCcsCiAgICAgICAgICAg\nICAgICAnZGphbmdvLmNvbnRyaWIubWVzc2FnZXMuY29udGV4dF9wcm9jZXNz\nb3JzLm1lc3NhZ2VzJywKICAgICAgICAgICAgXSwKICAgICAgICB9LAogICAg\nfSwKXQoKV1NHSV9BUFBMSUNBVElPTiA9ICdjb3JlLndzZ2kuYXBwbGljYXRp\nb24nCgoKIyBEYXRhYmFzZQojIGh0dHBzOi8vZG9jcy5kamFuZ29wcm9qZWN0\nLmNvbS9lbi81LjEvcmVmL3NldHRpbmdzLyNkYXRhYmFzZXMKCkRBVEFCQVNF\nUyA9IHsKICAgICdkZWZhdWx0JzogewogICAgICAgICdFTkdJTkUnOiAnZGph\nbmdvLmRiLmJhY2tlbmRzLnNxbGl0ZTMnLAogICAgICAgICdOQU1FJzogQkFT\nRV9ESVIgLyAnZGIuc3FsaXRlMycsCiAgICB9Cn0KCgojIFBhc3N3b3JkIHZh\nbGlkYXRpb24KIyBodHRwczovL2RvY3MuZGphbmdvcHJvamVjdC5jb20vZW4v\nNS4xL3JlZi9zZXR0aW5ncy8jYXV0aC1wYXNzd29yZC12YWxpZGF0b3JzCgpB\nVVRIX1BBU1NXT1JEX1ZBTElEQVRPUlMgPSBbCiAgICB7CiAgICAgICAgJ05B\nTUUnOiAnZGphbmdvLmNvbnRyaWIuYXV0aC5wYXNzd29yZF92YWxpZGF0aW9u\nLlVzZXJBdHRyaWJ1dGVTaW1pbGFyaXR5VmFsaWRhdG9yJywKICAgIH0sCiAg\nICB7CiAgICAgICAgJ05BTUUnOiAnZGphbmdvLmNvbnRyaWIuYXV0aC5wYXNz\nd29yZF92YWxpZGF0aW9uLk1pbmltdW1MZW5ndGhWYWxpZGF0b3InLAogICAg\nfSwKICAgIHsKICAgICAgICAnTkFNRSc6ICdkamFuZ28uY29udHJpYi5hdXRo\nLnBhc3N3b3JkX3ZhbGlkYXRpb24uQ29tbW9uUGFzc3dvcmRWYWxpZGF0b3In\nLAogICAgfSwKICAgIHsKICAgICAgICAnTkFNRSc6ICdkamFuZ28uY29udHJp\nYi5hdXRoLnBhc3N3b3JkX3ZhbGlkYXRpb24uTnVtZXJpY1Bhc3N3b3JkVmFs\naWRhdG9yJywKICAgIH0sCl0KCgojIEludGVybmF0aW9uYWxpemF0aW9uCiMg\naHR0cHM6Ly9kb2NzLmRqYW5nb3Byb2plY3QuY29tL2VuLzUuMS90b3BpY3Mv\naTE4bi8KCkxBTkdVQUdFX0NPREUgPSAnZW4tdXMnCgpUSU1FX1pPTkUgPSAn\nVVRDJwoKVVNFX0kxOE4gPSBUcnVlCgpVU0VfVFogPSBUcnVlCgoKIyBTdGF0\naWMgZmlsZXMgKENTUywgSmF2YVNjcmlwdCwgSW1hZ2VzKQojIGh0dHBzOi8v\nZG9jcy5kamFuZ29wcm9qZWN0LmNvbS9lbi81LjEvaG93dG8vc3RhdGljLWZp\nbGVzLwoKU1RBVElDX1VSTCA9ICdzdGF0aWMvJwoKIyBEZWZhdWx0IHByaW1h\ncnkga2V5IGZpZWxkIHR5cGUKIyBodHRwczovL2RvY3MuZGphbmdvcHJvamVj\ndC5jb20vZW4vNS4xL3JlZi9zZXR0aW5ncy8jZGVmYXVsdC1hdXRvLWZpZWxk\nCgpERUZBVUxUX0FVVE9fRklFTEQgPSAnZGphbmdvLmRiLm1vZGVscy5CaWdB\ndXRvRmllbGQnCgo=\n"
# print(base64.b64decode(code).decode())


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


analyze_code(base64.b64decode(code).decode(),"models.py" )