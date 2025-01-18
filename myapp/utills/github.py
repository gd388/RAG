import requests
import base64
from urllib.parse import urlparse
import uuid
import logging
from .ai_agent import analyze_code

# Setup logging for debugging
logging.basicConfig(level=logging.DEBUG)

def get_owner_repo(url):
    """
    Extracts the owner and repository name from a GitHub URL.
    """
    passed_url = urlparse(url)
    path_parts = passed_url.path.strip("/").split("/")
    if len(path_parts) >= 2:
        owner, repo = path_parts[0], path_parts[1]
        return owner, repo
    return None, None

def fetch_pr_files(repo_url, pr_number, git_token=None):
    owner, repo = get_owner_repo(repo_url)
    if not owner or not repo:
        logging.error(f"Invalid repository URL: {repo_url}")
        return []
    
    if not git_token:
        logging.error("GitHub token is missing. Authentication is required.")
        return []
    
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    headers = {"Authorization": f"token {git_token}"}
    
    logging.debug(f"Fetching PR files from URL: {url}")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Will raise an HTTPError for bad status codes
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch PR files. Error: {e}")
        return []
    
    files = response.json()
    logging.debug(f"Fetched PR files: {files}")
    
    if not files:
        logging.warning(f"No files found in PR {pr_number} for repository {repo_url}")
    
    return files


def fetch_content(repo_url, file_path, git_token=None):
    """
    Fetches the content of a file from the repository.
    """
    owner, repo = get_owner_repo(repo_url)
    if not owner or not repo:
        logging.error(f"Invalid repository URL: {repo_url}")
        return None
    
    logging.debug(f"Fetching content from: {file_path}")
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {"Authorization": f"token {git_token}"} if git_token else {}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logging.error(f"Error fetching content from {file_path}: {str(e)}")
        return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed for {file_path}: {str(e)}")
        return None
    
    content = response.json()
    if 'content' in content:
        return base64.b64decode(content['content'].encode())
    else:
        logging.warning(f"No content found for file: {file_path}")
        return None

def analyze_pr(repo_url, pr_number, git_token=None):
    """
    Analyzes the PR by fetching files and their contents.
    """
    task_id = str(uuid.uuid4())
    result = []  # Initialize result to an empty list
    
    try:
        # Fetch the PR files
        pr_files = fetch_pr_files(repo_url, pr_number, git_token)
        
        if not pr_files:
            logging.warning(f"No files found in PR {pr_number} for repository {repo_url}")
        
        analysis_results = []
        
        # Analyze each file in the PR
        for file in pr_files:
            if 'filename' not in file:  # Correct field name
                logging.warning(f"Skipping file: {file} due to missing 'filename' field.")
                continue
            
            file_name = file['filename']
            raw_content = fetch_content(repo_url, file_name, git_token)
            
            if raw_content:
                file_result = analyze_code(raw_content, file_name)
                analysis_results.append({"result": file_result, "file_name": file_name})
            else:
                logging.warning(f"Skipping file: {file_name} due to empty content.")
        
        result = analysis_results
    except Exception as e:
        logging.error(f"Error analyzing PR: {e}")
    
    # Return task ID and the analysis result, ensuring result is a list (even if empty)
    logging.debug(f"Task {task_id} analysis result: {result}")
    return {"task_id": task_id, "result": result or []}
