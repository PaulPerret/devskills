from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    
    # Fetch all the skills associated with the logged-in user
    my_skills = request.user.employee.skills.all().order_by('category')
    
    context = {'skills': my_skills}
    return render(request, 'employee.html', context)
