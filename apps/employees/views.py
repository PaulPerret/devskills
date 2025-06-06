from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from employees.models import Employee
from skills.models import Skill, SkillCategory

@login_required
def index(request):
    
    # Fetch all the skills associated with the logged-in user
    my_skills = request.user.employee.skills.all().order_by('category')
    
    context = {'skills': my_skills}
    return render(request, 'employee.html', context)

@login_required
def find_an_expert(request):
    
    employees_list = Employee.objects.all()
    categories_list = SkillCategory.objects.all()
    skills_list = Skill.objects.select_related('category').all()
    context = {
        'employees': employees_list,
        'categories': categories_list,
        'skills': skills_list
        }
    return render(request, 'search.html', context)