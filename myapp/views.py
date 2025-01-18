from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import analyze_pr_task
from celery.result import AsyncResult

@api_view(['POST'])
def start_task(request):
    data = request.data
    repo_url = data.get('repo_url')
    pr_number = data.get('pr_number')
    git_token = data.get('git_token')

    # Start the task
    task = analyze_pr_task.delay(repo_url, pr_number, git_token)

    return Response({
        "task_id": task.id,  # Use the actual task id
        "status": "Task Started"
    })


@api_view(['GET'])
def task_status(request, task_id):
    # Retrieve the result using the task id
    result = AsyncResult(task_id)
    
    response = {
        "task_id": result.id,  # Use the actual task id
        "status": result.state  # Status of the task
    }

    return Response(response)
