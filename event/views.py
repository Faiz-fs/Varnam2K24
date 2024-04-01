import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EventRegist


# Create your views here.
part = {
    "PRC": 130,
    "CS": 150,
    "TOV": 150,
    "HH": 110,
    "DD": 110,
    "AU": 150,
    "POV": 110,
    "G2G": 140,
    "ZS": 110,
    "EH": 120,
    "CM": 190,
    "FF": 130,
    "BP": 130,
    "IA": 150,
    "TH": 500,
}
slot = {
    1: [
        "Tamil oodu vilaiyadu",
        "Among us in real life",
        "Grasp to Gather",
        "Bay Of Pixels",
        "Feet on Fire"
    ],
    2: ["Treasure Hunt", "IPL Auction"],
    3: [
        "Deal Dazzle",
        "Handmade Hues",
        "Point of View",
        "Product Review Contest",
    ],
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
    "FF": "Feet on Fire",
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
    ev = EventRegist.objects.filter(eventname=eventlst[val]).count()
    # print(ev)
    if ev >= part[val]:
        messages.error(request, "Registeration is closed")
        return redirect("index")
    else:
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
