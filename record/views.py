from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Member

# Create your views here.

def Home(request):
    return render(request,'home.html')


def add_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        date_of_joining = request.POST.get('date_of_joining')
        date_of_fee_submission = request.POST.get('date_of_fee_submission')

        member = Member(name=name, mobile_number=mobile_number, date_of_joining=date_of_joining, date_of_fee_submission=date_of_fee_submission)
        member.save()
        
        return HttpResponseRedirect('/members/') # Redirect to a members list page after adding a new member

    return render(request, 'add_member.html') # Render the add member page if it's a GET request



def members(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})


#from django.shortcuts import render, redirect, get_object_or_404

#from .forms import MemberForm

#def edit_member(request, member_id):
 #   member = get_object_or_404(Member, id=member_id)
  #  if request.method == 'POST':
   #     form = MemberForm(request.POST, instance=member)
    #    if form.is_valid():
     #       form.save()
      #      return redirect('members')
    #else:
     #   form = MemberForm(instance=member)
    #return render(request, 'edit_member.html', {'form': form, 'member': member})

