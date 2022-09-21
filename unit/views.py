import unit_templates.hero_class_templates as class_templates
from descent_web_core.authentication import authenticate
import unit_templates.hero_templates as hero_templates
from unit.models.unit_model import Unit
from django.http import HttpResponse
from django.views import View
import json


class UnitCreateView(View):

    heroes = {
                 'SINDRAEL': hero_templates.SINDRAEL,
                 'GRISBAN': hero_templates.GRISBAN,
                 'ASHRIAN': hero_templates.ASHRIAN,
                 'LEORIC': hero_templates.LEORIC,
    }

    hero_classes = {
                    'KNIGHT': class_templates.KNIGHT,
                    'BERSERKER': class_templates.BERSERKER,
                    'DISCIPLE': class_templates.DISCIPLE,
                    'SPIRITSPEAKER': class_templates.SPIRITSPEAKER,
                    'NECROMANCER': class_templates.NECROMANCER,
                    'RUNEMASTER': class_templates.RUNEMASTER,
    }

    allowed_classes = {
                    'SINDRAEL': [class_templates.KNIGHT, class_templates.BERSERKER],
                    'GRISBAN': [class_templates.KNIGHT, class_templates.BERSERKER],
                    'ASHRIAN': [class_templates.DISCIPLE, class_templates.SPIRITSPEAKER],
                    'LEORIC': [class_templates.NECROMANCER, class_templates.RUNEMASTER],
    }

    def post(self, request):
        if authenticate(request):
            data = json.loads(request.body)
            user = authenticate(request)[0]

            if data['hero_name'] in self.heroes.keys() and data['hero_class'] in self.hero_classes.keys():
                hero = self.heroes[data['hero_name']]
                hero_class = self.hero_classes[data['hero_class']]
                if hero_class in self.allowed_classes[data['hero_name']]:

                    for key in hero_class.keys():
                        hero[key] += hero_class.get(key)
                    unit = Unit.objects.create(user=user, **hero)
                    print(vars(unit))
                    return HttpResponse(vars(unit), status=204, content_type='application/json')
                else:
                    context = {
                        'status': '400', 'message': 'Wrong data: Hero got No such class'
                    }
                    response = HttpResponse(json.dumps(context), content_type='application/json')
                    response.status_code = 400
                    return response
            else:
                context = {
                    'status': '400', 'message': 'Wrong data: No such Hero or No such class'
                }
                response = HttpResponse(json.dumps(context), content_type='application/json')
                response.status_code = 400
                return response

    def get(self, request, **kwargs):
        pass


class UnitListCreateView(View):

    def get(self, request, hero):
        pass

    def put(self, request, hero):
        pass

    def patch(self, request, hero):
        pass

    def delete(self, request, hero):
        pass
