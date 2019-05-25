from rest_framework import serializers

from .models import Projects, Tasks

class ProjectSerializer(serializers.Serializer):
    class meta:
        model = Projects
        fields = ('id')

    name = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=200)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()

    def to_representation(self, instance):
        project_object = super(ProjectSerializer, self).to_representation(instance)
        project_object["id"] = instance.id
        project_object["number_of_tasks"] = Tasks.objects.filter(project_id=instance.id).count()
        return project_object

class ProjectDetailSerializer(serializers.Serializer):
    class meta:
        model = Projects
        fields = ('id')

    name = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=200)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()

    def to_representation(self, instance):
        project_object = super(ProjectDetailSerializer, self).to_representation(instance)
        project_object["id"] = instance.id
        tasks = Tasks.objects.filter(project_id=instance.id)
        project_object["tasks"] = TaskSerializer(tasks, many=True).data
        return project_object

class TaskSerializer(serializers.Serializer):
    class meta:
        model = Tasks
        fields = ("id")

    name = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=200)

    def to_representation(self, instance):
        task_object = super(TaskSerializer, self).to_representation(instance)
        task_object["id"] = instance.id
        task_object["owner"] = {}
        task_object["owner"]["id"] = instance.assignee.id
        task_object["owner"]["name"] = instance.assignee.username
        task_object["project"] = {}
        task_object["project"]["id"] = instance.project.id
        task_object["project"]["name"] = instance.project.name
        return task_object
