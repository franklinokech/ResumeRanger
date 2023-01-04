from django.shortcuts import render, redirect
from .forms import JobPostingForm
from .utilities import calculate_match_percentage


def job_posting(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST, request.FILES)
        if form.is_valid():
            cv_file = request.FILES['cv']
            job_description = request.POST['requirements']
            form.save()
            match_percentage = calculate_match_percentage(cv_file,job_description)
            return render(request, 'resumematcher/results.html', {'match_percentage': match_percentage})
    else:
        form = JobPostingForm()
    return render(request, 'resumematcher/job_posting.html', {'form': form})
