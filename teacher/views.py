from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# =========================
# TEACHER DASHBOARD
# =========================

@login_required
def teacher_dashboard(request):

    teacher = request.user.teacher_profile

    return render(
        request,
        "teacher/dashboard.html",
        {
            "teacher": teacher
        }
    )


# =========================
# TEACHER PROFILE
# =========================

@login_required
def teacher_profile(request):

    teacher = request.user.teacher_profile

    context = {
        "name": teacher.teacher_name,
        "staff_id": teacher.teacher_id,
        "mobile_no": teacher.mobile,
        "department": teacher.department,
        "email": teacher.email,
    }

    return render(
        request,
        "teacher_profile.html",
        context
    )
from django.shortcuts import render

def teacher_profile(request):
    # Dynamic teacher data (Aap ise Database/Model se bhi fetch kar sakte hain)
    context = {
        'name': 'Dr. Rajesh Sharma',
        'staff_id': 'TS-1042',
        'mobile_no': '+91 98765 43210',
        'department': 'Computer Science & Engineering',
        'qualification': 'Ph.D. in Computer Science',
        'specialization': 'AI & Machine Learning',
        'total_experience': '8+ Years',
        'linkedin_url': 'https://linkedin.com/in/example',
        'github_url': 'https://github.com/example',
        'profile_photo_url': '/static/images/teacher.jpg' # Ya dynamic image URL
    }
    return render(request, 'teacher_profile.html', context)
