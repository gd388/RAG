from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .tasks import analyze_pr_task
from celery.result import AsyncResult

@api_view(['POST'])
def start_task(request):
    data = request.data
    
    # Ensure required fields are provided
    repo_url = data.get('repo_url')
    pr_number = data.get('pr_number')
    git_token = data.get('git_token')

    if not repo_url or not pr_number:
        return Response({"error": "Both 'repo_url' and 'pr_number' are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Start the task
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
        "result" : result.result
    }

   

    return Response(response, status=status.HTTP_200_OK)
