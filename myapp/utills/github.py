import requests
import base64
from urllib.parse import urlparse
import uuid
from .ai_agent import analyze_code

def get_owner_repo(url):
    passed_url = urlparse(url)
    path_parts = passed_url.path.strip("/").split("/")
    if len(path_parts) >= 2:
        owner , repo = path_parts[0],path_parts[1]
        return owner , repo
    return None,None

def fetch_pr_files(repo_url,pr_number,git_token=None):
    
    owner , repo = get_owner_repo(repo_url)
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    headers = {"Authorization" : f"token {git_token}"} if git_token else {}
    response = requests.get(url,headers=headers)
    return response.json()


def fetch_content(repo_url,file_path,git_token=None):
    
    owner , repo = get_owner_repo(repo_url)
    url = f"https://api.github.com/repos/{owner}/{repo}/content/{file_path}"
    headers = {"Authorization" : f"token {git_token}"} if git_token else {}
    response = requests.get(url,headers=headers)
    content =  response.json()
    return base64.b64decode(content['content'].decode())

def analyze_pr(repo_url,pr_number,git_token=None):
    task_id = str(uuid.uuid4())
    try : 
        pr_files = fetch_pr_files(repo_url,pr_number,git_token=None)
        analysis_results = []
        for file in pr_files:
            file_name = file['file_name']
            raw_content = fetch_content(repo_url,file_name,git_token)
            result = analyze_code(raw_content,file_name)
            analysis_results.append({"result" : result,"file_name" : file_name})
        return {"task_id" : task_id , "result" : analysis_results}

    except Exception as e:
        print(e)
        return {"task_id" : task_id, result : []}


     