from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Member, BRANCH_CHOICES, INDIAN_STATE_CHOICES, COUNTRY_CHOICES
from member_pics.models import MemberPic as mp
import csv
from django.http import HttpResponse
from members.forms import EditMemberForm
from member_pics.forms import EditMemberPicForm, DeleteMemberPicForm

def members(request):
    sort_members_val = 'names-ascending'
    filter_branch_val = 'all-branches'
    if request.method=='GET':
        sort_query = request.GET.get('sort-members', None)
        filter_query = request.GET.get('filter-branch', None)
        search_query = request.GET.get('search-members', None)
        
        search_query = request.GET.get('search-members', None)
        if sort_query is not None or filter_query is not None:
            print(f"sort_query={sort_query} and filter_query={filter_query}")
            sort_param = 'display_name'
            filter_param = filter_query
            if sort_query == "names-descending":
                sort_param = '-display_name'

            if filter_param == 'all-branches':
                members = Member.objects.all().order_by(sort_param)
            else:
                members = Member.objects.filter(branch=filter_param).order_by(sort_param)
            sort_members_val = sort_query
            filter_branch_val = filter_query
        elif search_query is None:
            members = Member.objects.all().order_by('display_name')
        else:
            members = Member.objects.filter(display_name__icontains=search_query).order_by('display_name')
    context = {
        'members' : members,
        'branches' : BRANCH_CHOICES,
        'sort_members' : sort_members_val,
        'filter_branch' : filter_branch_val
    }
    if search_query is not None:
        context['search_query'] = search_query
    return render(request,'members/members.html', context)

def individual_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    images = mp.objects.filter(member=member)
    print(type(images))
    print(type(member))
    #images = member.mp_set.all()
    context = {
        'member' : member,
        'images' : images,
        'branches' : BRANCH_CHOICES,
        'states' : INDIAN_STATE_CHOICES,
        'countries' : COUNTRY_CHOICES
    }
    return render(request, 'individual-member/individual-member.html', context)

def view_profile(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    images = mp.objects.filter(member=member)
    #images = member.mp_set.all()
    context = {
        'member' : member,
        'images' : images,
        'branches' : BRANCH_CHOICES,
        'states' : INDIAN_STATE_CHOICES,
        'countries' : COUNTRY_CHOICES
    }
    return render(request, 'individual-member/profile.html', context)

def edit_profile(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = EditMemberForm(request.POST, request.FILES, instance=member)
        print(type(form))
        if form.is_valid():
            form.save()
            return redirect('view_profile', member_id)
    else:
        form = EditMemberForm(instance=member)
    return render(request,
                  'individual-member/edit_profile.html',
                  {
                      'form': form,
                      'member': member
                  })

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=export.csv'
    writer = csv.writer(response)
    opts = Member._meta
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    members = Member.objects.all()
    for obj in members:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response

def edit_pic(request, member_pic_id):
    member_pic = get_object_or_404(mp, pk=member_pic_id)
    if request.method == 'POST':
        form = EditMemberPicForm(request.POST, request.FILES, instance=member_pic)
        if form.is_valid():
            form.save()
            return redirect('view_profile', member_pic.member.id)
    else:
        form = EditMemberPicForm(instance=member_pic)
    return render(request,
                  'individual-member/edit_pic.html',
                  {
                      'form': form,
                      'memberPic': member_pic
                  })

def delete_pic(request, member_pic_id):
    member_pic = get_object_or_404(mp, pk=member_pic_id)
    if request.method == 'POST':
        form = DeleteMemberPicForm(request.POST, request.FILES, instance=member_pic)
        if form.is_valid():
            member_pic.delete()
            return redirect('view_profile', member_pic.member.id)
    else:
        form = DeleteMemberPicForm(instance=member_pic)
    return render(request,
                  'individual-member/delete_pic.html',
                  {
                      'form': form,
                      'memberPic': member_pic
                  })


def add_pic(request, member_id):
    context = {
        'member_id' : member_id
    }
    if request.method == 'POST':
        # Get form values
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        print(type(request.FILES['photo']))
        photo = request.FILES['photo']
        print(type(request.POST['caption']))
        caption = request.POST['caption']
        member = Member.objects.get(pk=member_id)
        pic_obj = mp(member=member, photo=photo, caption=caption)
        pic_obj.save()
        messages.success(request, 'Pic Added')
        return redirect('view_profile', member_id)
    else:
        return render(request, 'individual-member/add_pic.html', context)