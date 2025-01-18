import os
import shutil
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .tasks import analyze_pr_task
from celery.result import AsyncResult
import re
def delete_unnecessary_files(directory):
    """
    This function will delete .pyc files and __pycache__ directories at runtime
    from the specified directory and its subdirectories.
    """
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            # Delete .pyc files
            if name.endswith(".pyc"):
                file_path = os.path.join(root, name)
                print(f"Deleting file: {file_path}")
                os.remove(file_path)
        
        # Delete __pycache__ directories
        for name in dirs:
            if name == "__pycache__":
                dir_path = os.path.join(root, name)
                print(f"Deleting directory: {dir_path}")
                shutil.rmtree(dir_path)

@api_view(['POST'])
def start_task(request):
    data = request.data
    
    # Ensure required fields are provided
    repo_url = data.get('repo_url')
    pr_number = data.get('pr_number')
    git_token = data.get('git_token')

    if not repo_url or not pr_number or not git_token:
        return Response({"error": "Both 'repo_url', 'pr_number', and 'git_token' are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Assuming you have the path to the repository (repo_url) or directory (locally cloned)
    # Delete unnecessary files in the repository (if it's a local path)
    # If repo_url is a GitHub URL, you may need to clone it first.
    local_repo_path = "/path/to/your/local/repo"  # Change this to the local path of your repo

    # Delete unnecessary files (e.g., __pycache__ and .pyc files) at runtime
    delete_unnecessary_files(local_repo_path)
    
    # Start the task (pass the necessary files here)
    task = analyze_pr_task.delay(repo_url, pr_number, git_token)

    return Response({
        "task_id": task.id,  # Return the actual task id
        "status": "Task Started"
    }, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def task_status(request, task_id):
    # Retrieve the result using the task id
    result = AsyncResult(task_id)

    response = {
        "task_id": result.id,  
        "status": result.state,  
        "result": result.result if result.state == "SUCCESS" else "Task is still in progress"
    }

    if result.state == 'FAILURE':
        response["error"] = str(result.result)  

    return Response(response, status=status.HTTP_200_OK)
