import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EventRegist


# Create your views here.

slot = {
    1: ["Product Review Contest", "Tamil oodu vilaiyadu", "Among us in real life", "Grasp to Gather"],
    2: ["Treasure Hunt", "IPL Auction"],
    3: ["Deal Dazzle", "Handmade Hues", "Point of View", "Bay Of Pixels"],
    4: ["Cine Saga", "Zizzle stark", "Environmental Hunters", "Code Maria"],
}
eventlst = {
    "PRC": "Product Review Contest",
    "CS": "Cine Saga",
    "TOV": "Tamil oodu vilaiyadu",
    "HH": "Handmade Hues",
    "DD": "Deal Dazzle",
    "AU": "Among us in real life",
    "POV": "Point of View",
    "G2G": "Grasp to Gather",
    "ZS": "Zizzle stark",
    "EH": "Environmental Hunters",
    "CM": "Code Maria",
    "DC": "Dance Competition",
    "BP": "Bay Of Pixels",
    "IA": "IPL Auction",
    "TH": "Treasure Hunt",
}


def index(request):
    return render(request, "index.html")


def eventpage(request):
    return render(request, "eventpage.html")


def sgsevent(request):
    return render(request, "sgsevent.html")


def register(request, val):
    # print(eventlst[val])
    return render(request, "register.html", {"data": val})


def send(request, val):
    pattern = r"\d+\w+\d+@\w+\.\w+"
    phonep = r"\d"
    if request.method == "POST":
        email = request.POST["email"]
        name = request.POST["name"]
        phoneno = request.POST["phoneno"]
        if (
            re.match(pattern, email)
            and "7276" in email
            and "@mcet.in" in email
            and re.match(phonep, phoneno)
            and len(phoneno) == 10
        ):
            users = EventRegist.objects.filter(email=email)
            if users.exists():
                for user in users:
                    for i in slot.keys():
                        if user.eventname in slot[i] and eventlst[val] in slot[i]:
                            messages.warning(
                                request, "Event Clash Please select other event"
                            )
                            return redirect("index")
                else:
                    EventRegist.objects.create(
                        email=email, name=name, phoneno=phoneno, eventname=eventlst[val]
                    )
                    messages.success(request, "Registered Successfull")
                    return redirect("index")
            else:
                EventRegist.objects.create(
                    email=email, name=name, phoneno=phoneno, eventname=eventlst[val]
                )
                messages.success(request, "Registered Successfull")
                return redirect("index")

        else:
            messages.error(
                request, "Invalid Detail Please check your email and phone number"
            )
            return render(request, "register.html", {"data": val})
