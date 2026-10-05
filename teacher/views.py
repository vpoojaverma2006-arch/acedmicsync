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