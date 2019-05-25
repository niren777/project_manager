from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from .models import Projects, Tasks
from .serializers import ProjectSerializer, TaskSerializer, ProjectDetailSerializer

class Project(APIView):
    def get(self, request, id=None):
        if id is None:
            projects = Projects.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            return render(request, 'templates/projects.html', {'projects': serializer.data})
        else:
            project = Projects.objects.get(id=id)
            serializer = ProjectDetailSerializer(project)
            print(serializer.data)
            return render(request, 'templates/project_details.html', {'project': serializer.data})
            
        # return Response({"projects": serializer.data})

class Task(APIView):
    def get(self, request, project_id=None, id=None):
        tasks = Tasks.objects.get(id=id)
        serializer = TaskSerializer(tasks)
        print(serializer.data)
        # return Response({"tasks": serializer.data})
        return render(request, 'templates/task_details.html', {'task': serializer.data})
