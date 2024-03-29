from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import *
from .serializers import *
import time
#from .utils import cheackTime

class WheelView(APIView):

    def get(self, request):
        wheel = Wheel.objects.all()

        serializer = WheelSerializer(wheel, many=True)
       
        return Response(serializer.data)
    
class HealthView(APIView):
    
    def get(self, request):

        #obj = Health.objects.all().prefetch_related('many_set')
        #one_objs = One.objects.all().prefetch_related('many_set')
        obj = ToDoHealth.objects.all()

        for toDo in obj:
            if toDo.timeEnd <= time.time():
                obi = Wheel.objects.get(id=1)
                obi.health = obi.health-1
                obi.save()
                toDo.delete()

        serializer = ToDoHealthSerializerId(obj, many=True)

        

        return Response({"health": serializer.data})
    

    def post(self, request):
        health = request.data.get('health')
        print(request.data)
        # Create an article from the above data
        serializer = ToDoHealthSerializer(data=health)

        if serializer.is_valid(raise_exception=True):
            health_saved = serializer.save()
        return Response({"success": "health '{}' created successfully".format(health_saved.id)})


class HealthDone(APIView):

    def delete(self, request, pk):
    # Get object with this pk
        health = get_object_or_404(ToDoHealth.objects.all(), pk=pk)
        health.delete()
        obj = Wheel.objects.get(id=1)
        obj.health = obj.health+1
        obj.save()
        return Response({"message": "healthе with id `{}` has been deleted.".format(pk)}, status=204)
  
class HealthDelete(APIView):

    def delete(self, request, pk):
    # Get object with this pk
        health = get_object_or_404(ToDoHealth.objects.all(), pk=pk)
        health.delete()
        return Response({"message": "healthе with id `{}` has been deleted.".format(pk)}, status=204)


class RelationshipsView(APIView):
    def get(self, request):
        obj = ToDoRelationships.objects.all()

        for toDo in obj:
            if toDo.timeEnd <= time.time():
                obi = Wheel.objects.get(id=1)
                obi.relationships = obi.relationships-1
                obi.save()
                toDo.delete()


        serializer = ToDoRelationshipsSerializerId(obj, many=True)
                
        return Response({"relationships": serializer.data})

    def post(self, request):
        relationships = request.data.get('relationships')
        # Create an article from the above data
        serializer = ToDoRelationshipsSerializer(data=relationships)

        if serializer.is_valid(raise_exception=True):
            relationships_saved = serializer.save()
        return Response({"success": "relationships '{}' created successfully".format(relationships_saved.id)})

class RelationshipsDone(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        relationships = get_object_or_404(ToDoRelationships.objects.all(), pk=pk)
        relationships.delete()

        obj = Wheel.objects.get(id=1)
        obj.relationships = obj.relationships+1
        obj.save()
        return Response({"message": "relationships with id `{}` has been deleted.".format(pk)}, status=204)

class RelationshipsDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        relationships = get_object_or_404(ToDoRelationships.objects.all(), pk=pk)
        relationships.delete()

        
        return Response({"message": "relationships with id `{}` has been deleted.".format(pk)}, status=204)



class EnvironmentView(APIView):
    def get(self, request):

        obj = ToDoEnvironment.objects.all()
        for toDo in obj:
            if toDo.timeEnd <= time.time():
                obi = Wheel.objects.get(id=1)
                obi.environment = obi.environment-1
                obi.save()
                toDo.delete()


        serializer = ToDoEnvironmentSerializerId(obj, many=True)

        return Response({"environment": serializer.data})

    def post(self, request):
        environment = request.data.get('environment')
        # Create an article from the above data
        serializer = ToDoEnvironmentSerializer(data=environment)

        if serializer.is_valid(raise_exception=True):
            environment_saved = serializer.save()
        return Response({"success": "environment '{}' created successfully".format(environment_saved.id)})

class EnvironmentDone(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        environment = get_object_or_404(ToDoEnvironment.objects.all(), pk=pk)
        environment.delete()

        obj = Wheel.objects.get(id=1)
        obj.environment = obj.environment+1
        obj.save()

        return Response({"message": "environment with id `{}` has been deleted.".format(pk)}, status=204)

class EnvironmentDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        environment = get_object_or_404(ToDoEnvironment.objects.all(), pk=pk)
        environment.delete()

        return Response({"message": "environment with id `{}` has been deleted.".format(pk)}, status=204)


class VocationView(APIView):
    def get(self, request):
        obj = ToDoVocation.objects.all()

        for toDo in obj:
            if toDo.timeEnd <= time.time():
                obi = Wheel.objects.get(id=1)
                obi.vocation = obi.vocation-1
                obi.save()
                toDo.delete()


        serializer = ToDoVocationSerializerId(obj, many=True)

        return Response({"vocation": serializer.data})

    def post(self, request):
        vocation = request.data.get('vocation')
        # Create an article from the above data
        serializer = ToDoVocationSerializer(data=vocation)

        if serializer.is_valid(raise_exception=True):
            vocation_saved = serializer.save()
        return Response({"success": "vocation '{}' created successfully".format(vocation_saved.id)})


class VocationDone(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        vocation = get_object_or_404(ToDoVocation.objects.all(), pk=pk)
        vocation.delete()

        obj = Wheel.objects.get(id=1)
        obj.vocation = obj.vocation+1
        obj.save()

        return Response({"message": "vocation with id `{}` has been deleted.".format(pk)}, status=204)

class VocationDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        vocation = get_object_or_404(ToDoVocation.objects.all(), pk=pk)
        vocation.delete()


        return Response({"message": "vocation with id `{}` has been deleted.".format(pk)}, status=204)





class ProsperityView(APIView):
    def get(self, request):
        obj = ToDoProsperity.objects.all()

        for toDo in obj:
            if toDo.timeEnd <= time.time():
                obi = Wheel.objects.get(id=1)
                obi.prosperity = obi.prosperity-1
                obi.save()
                toDo.delete()

        serializer = ToDoProsperitySerializerId(obj, many=True)

        return Response({"prosperity": serializer.data})

    def post(self, request):
        prosperity = request.data.get('prosperity')
        # Create an article from the above data
        serializer = ToDoProsperitySerializer(data=prosperity)

        if serializer.is_valid(raise_exception=True):
            prosperity_saved = serializer.save()
        return Response({"success": "rosperity '{}' created successfully".format(prosperity_saved.id)})

class ProsperityDone(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        prosperity = get_object_or_404(ToDoProsperity.objects.all(), pk=pk)
        prosperity.delete()
        obj = Wheel.objects.get(id=1)
        obj.prosperity = obj.prosperity+1
        obj.save()

        return Response({"message": "prosperity with id `{}` has been deleted.".format(pk)}, status=204)

class ProsperityDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        prosperity = get_object_or_404(ToDoProsperity.objects.all(), pk=pk)
        prosperity.delete()
        return Response({"message": "prosperity with id `{}` has been deleted.".format(pk)}, status=204)



class SelfImprovementView(APIView):
    def get(self, request):
        obj = ToDoSelfImprovement.objects.all()

        for toDo in obj:
            if toDo.timeEnd <= time.time():
                obi = Wheel.objects.get(id=1)
                obi.selfImprovement = obi.selfImprovement-1
                obi.save()
                toDo.delete()

        serializer = ToDoSelfImprovementSerializerId(obj, many=True)

        return Response({"selfImprovement": serializer.data})

    def post(self, request):
        selfImprovement = request.data.get('selfImprovement')
        # Create an article from the above data
        serializer = ToDoSelfImprovementSerializer(data=selfImprovement)

        if serializer.is_valid(raise_exception=True):
            selfImprovement_saved = serializer.save()
        return Response({"success": "selfImprovement '{}' created successfully".format(selfImprovement_saved.id)})

class SelfImprovementDone(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        selfImprovement= get_object_or_404(ToDoSelfImprovement.objects.all(), pk=pk)
        selfImprovement.delete()

        obj = Wheel.objects.get(id=1)
        obj.selfImprovement = obj.selfImprovement+1
        obj.save()
        return Response({"message": "selfImprovement with id `{}` has been deleted.".format(pk)}, status=204)

class SelfImprovementDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        selfImprovement= get_object_or_404(ToDoSelfImprovement.objects.all(), pk=pk)
        selfImprovement.delete()

       
        return Response({"message": "selfImprovement with id `{}` has been deleted.".format(pk)}, status=204)




class BrightnessOfLifeView(APIView):
    def get(self, request):
        obj = ToDoBrightnessOfLife.objects.all()

        for toDo in obj:
            if toDo.timeEnd <= time.time():
                obi = Wheel.objects.get(id=1)
                obi.brightnessOfLife = obi.brightnessOfLife-1
                obi.save()
                toDo.delete()

        serializer = ToDoBrightnessOfLifeSerializerId(obj, many=True)

        return Response({"brightnessOfLife": serializer.data})

    def post(self, request):
        brightnessOfLife = request.data.get('brightnessOfLife')
        # Create an article from the above data
        serializer = ToDoBrightnessOfLifeSerializer(data=brightnessOfLife)

        if serializer.is_valid(raise_exception=True):
            brightnessOfLife_saved = serializer.save()
        return Response({"success": "brightnessOfLife '{}' created successfully".format(brightnessOfLife_saved.id)})

class BrightnessOfLifeDone(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        brightnessOfLife = get_object_or_404(ToDoBrightnessOfLife.objects.all(), pk=pk)
        brightnessOfLife.delete()
        obj = Wheel.objects.get(id=1)
        obj.brightnessOfLife= obj.brightnessOfLife+1
        obj.save()
        return Response({"message": "brightnessOfLife with id `{}` has been deleted.".format(pk)}, status=204)

class BrightnessOfLifeDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        brightnessOfLife = get_object_or_404(ToDoBrightnessOfLife.objects.all(), pk=pk)
        brightnessOfLife.delete()
        return Response({"message": "brightnessOfLife with id `{}` has been deleted.".format(pk)}, status=204)



class SpiritualityView(APIView):
    def get(self, request): 
        obj = ToDoSpirituality.objects.all()

        for toDo in obj:
            if toDo.timeEnd <= time.time():
                obi = Wheel.objects.get(id=1)
                obi.spirituality = obi.spirituality-1
                obi.save()
                toDo.delete()

        serializer = ToDoSpiritualitySerializerId(obj, many=True)

        return Response({"spirituality": serializer.data})

    def post(self, request):
        spirituality = request.data.get('spirituality')
        # Create an article from the above data
        serializer = ToDoSpiritualitySerializer(data=spirituality)

        if serializer.is_valid(raise_exception=True):
            spirituality_saved = serializer.save()
        return Response({"success": "spirituality  '{}' created successfully".format(spirituality_saved.id)})

class SpiritualityDone(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        spirituality = get_object_or_404(ToDoSpirituality.objects.all(), pk=pk)
        spirituality.delete()

        obj = Wheel.objects.get(id=1)
        obj.spirituality= obj.spirituality+1
        obj.save()
        return Response({"message": "spirituality with id `{}` has been deleted.".format(pk)}, status=204)

class SpiritualityDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        spirituality = get_object_or_404(ToDoSpirituality.objects.all(), pk=pk)
        spirituality.delete()

        return Response({"message": "spirituality with id `{}` has been deleted.".format(pk)}, status=204)
