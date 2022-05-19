from django import forms 
from django.forms import Form
from student_management_app.models import Courses, SessionYearModel,Fourations


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []

    #For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)

    except:
        session_year_list = []
    
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
    course_id = forms.ChoiceField(label="Salle", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))



class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []

    #For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)

    except:
        session_year_list = []

    
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
    course_id = forms.ChoiceField(label="Salle", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))


class AddFourationForm(forms.Form):
    tir_list = (
        ('nonel', 'nonel'),
        ('electrique', 'electrique'),
        ('classique', 'classique'),

    )
    mode_tir = forms.ChoiceField(label="mode_tir", choices=tir_list,
                               widget=forms.Select(attrs={"class": "form-control"}))
    type_list = (
        ('42ms,25ms,17ms', '42ms,25ms,17ms'),
        ('42ms,17ms', '42ms,17ms'),


    )
    type_tir = forms.ChoiceField(label="type_tir", choices=type_list,
                                 widget=forms.Select(attrs={"class": "form-control"}))
    charge_list = (
        ('unique', 'unique'),
        ('etagé', 'étagé'),

    )
    mode_charge = forms.ChoiceField(label="mode_charge", choices=charge_list,
                               widget=forms.Select(attrs={"class": "form-control"}))
    tranche = forms.CharField(label="tranche", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    niveau_list = (
        ('RT/SB', 'RT/SB'),
        ('RT/SA2', 'RT/SA2'),
        ('INT1/2', 'INT1/2'),
        ('INT2/4', 'INT2/4'),
        ('INT3/4', 'INT3/4'),
        ('INT3/5', 'INT3/5'),
        ('INT5/6', 'INT5/6'),
        ('INT4/5', 'INT4/5'),
        ('INT2/3', 'INT2/3'),
        ('INTSA2/C0', 'INTSA2/C0'),
        ('RT/C0', 'RT/C0'),
        ('RT/C2', 'RT/C2'),
        ('RT/C3', 'RT/C3'),
        ('RT/C4', 'RT/C4'),
        ('RT/C5', 'RT/C5'),

    )
    niveau = forms.ChoiceField(label="Niveau", choices=niveau_list,
                               widget=forms.Select(attrs={"class": "form-control"}))

    panneau_list = (
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('P3', 'P3'),
        ('P4', 'P4'),
        ('P5', 'P5'),
        ('P6', 'P6'),
        ('P7', 'P7'),
        ('P8', 'P8')
    )
    panneau = forms.ChoiceField(label="Panneau", choices=panneau_list,
                                widget=forms.Select(attrs={"class": "form-control"}))

    longueur = forms.CharField(label="longueur", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    largeur = forms.CharField(label="largeur", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    nbr_trou_range = forms.CharField(label="nbr_trou_range", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    profondeur = forms.CharField(label="profondeur", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    dosage = forms.CharField(label="dosage", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    nbr_trou = forms.CharField(label="nbr_trou", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    maille = forms.CharField(label="maille", max_length=50,
                              widget=forms.TextInput(attrs={"class": "form-control"}))
    nbr_range = forms.CharField(label="nbr_range", max_length=50,
                             widget=forms.TextInput(attrs={"class": "form-control"}))



class EditFourationForm(forms.Form):
    tir_list = (
        ('nonel', 'nonel'),
        ('electrique', 'electrique'),
        ('classique', 'classique'),

    )
    mode_tir = forms.ChoiceField(label="mode_tir", choices=tir_list,
                                 widget=forms.Select(attrs={"class": "form-control"}))
    type_list = (
        ('42ms,25ms,17ms', '42ms,25ms,17ms'),
        ('42ms,17ms', '42ms,17ms'),

    )
    type_tir = forms.ChoiceField(label="type_tir", choices=type_list,
                                 widget=forms.Select(attrs={"class": "form-control"}))
    charge_list = (
        ('unique', 'unique'),
        ('Y', 'Y'),
        ('Z', 'Z'),

    )
    mode_charge = forms.ChoiceField(label="mode_charge", choices=charge_list,
                                    widget=forms.Select(attrs={"class": "form-control"}))
    tranche = forms.CharField(label="tranche", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

    niveau_list = (
        ('INT12', 'INT12'),
        ('INT24', 'INT24'),
        ('INT34', 'INT34'),
        ('INT56', 'INT56'),
        ('INT45', 'INT45'),
        ('INT23', 'INT23'),
        ('INTSA2C0', 'INTSA2C0'),
        ('RTC0', 'RTC0'),
        ('RTC2', 'RTC2'),

    )
    niveau = forms.ChoiceField(label="Niveau", choices=niveau_list,
                               widget=forms.Select(attrs={"class": "form-control"}))

    panneau_list = (
        ('P2', 'P2'),
        ('P3', 'P3'),
        ('P4', 'P4'),
        ('P5', 'P5'),
        ('P6', 'P6'),
        ('P7', 'P7'),
        ('P8', 'P8')
    )
    panneau = forms.ChoiceField(label="Panneau", choices=panneau_list,
                                widget=forms.Select(attrs={"class": "form-control"}))
    longueur = forms.CharField(label="longueur", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    largeur = forms.CharField(label="largeur", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    nbr_trou_range = forms.CharField(label="nbr de trou_range", max_length=50,
                                     widget=forms.TextInput(attrs={"class": "form-control"}))
    profondeur = forms.CharField(label="profondeur", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    dosage = forms.CharField(label="dosage", max_length=50,
                             widget=forms.TextInput(attrs={"class": "form-control"}))
    nbr_trou = forms.CharField(label="nbr_trou", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    maille = forms.CharField(label="maille", max_length=50,
                             widget=forms.TextInput(attrs={"class": "form-control"}))
    nbr_range = forms.CharField(label="nbr range", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
