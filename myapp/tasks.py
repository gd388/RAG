from celery import Celery,shared_task
from .utills.github import analyze_pr



app = Celery('django_app')
app.config_from_object('django.config:settings', namespace="CELERY")


@shared_task
def analyze_pr_task(repo_url,pr_number,git_token=None):
    result = analyze_pr(repo_url,pr_number,git_token)
    return result