from django.http import HttpResponse
from django.shortcuts import render

from web.models import Entry

projects = [
    [
        {
            "name": "Royal Security",
            "url": "https://github.com/L1ghtDream/RoyalSecurity",
            "image": "../static/images/projects/royal_security.png"
        },
        {
            "name": "GW Levels",
            "url": "https://github.com/L1ghtDream/GWLevels",
            "image": "../static/images/projects/gwlevels.png"
        },
        {
            "name": "Practice PvP",
            "url": "https://lunaworldmc.com/",
            "image": "../static/images/projects/practice_pvp.png"
        },
    ],
    [
        {
            "name": "Hunger Games",
            "url": "https://lightdream.tk/projects",
            "image": "../static/images/projects/hunger_games.png"
        },
        {
            "name": "Grappling Hook",
            "url": "https://lightdream.tk/projects",
            "image": "../static/images/projects/grappling_hook.png"
        },
        {
            "name": "Level Pickaxe",
            "url": "https://lightdream.tk/projects",
            "image": "../static/images/projects/level_pickaxe.png"
        },
    ],
]
servers = [
    [
        {
            "name": "Banana Prison",
            "url": "https://bananaprison.net",
            "image": "../static/images/projects/banana_prison.png"
        },
        {
            "name": "SurrealCraft",
            "url": "https://surrealcraft.net",
            "image": "../static/images/projects/surreal_craft.png"
        },
        {
            "name": "Gaming World",
            "url": "https://gamingworld.ro",
            "image": "../static/images/projects/gaming_world.png"
        }
    ],
    [
        {
            "name": "Original",
            "url": "https://forum.original.gg",
            "image": "../static/images/projects/original.png"
        },
        {
            "name": "Royal Savage",
            "url": "https://www.royalsavageteam.com",
            "image": "../static/images/projects/royal_savage.png"
        },
        {
            "name": "Gamster",
            "url": "https://www.gamster.org",
            "image": "../static/images/projects/gamster.png"
        }
    ],
]
games = [
    [
        {
            "name": "ShootMe!",
            "url": "https://github.com/L1ghtDream/RoyalSecurity",
            "image": "../static/images/games/shootme.png"
        },
    ],
]
degrees = [
    [
        {
            "name": "CS50 EDX",
            "url": "https://courses.edx.org/certificates/34208bd0bf6148fd917003380e3b8f7c",
            "image": "../static/images/degrees/cs50_edx.png"
        },
        {
            "name": "CS50 Harvard",
            "url": "https://certificates.cs50.io/04acc3d1-53ea-4395-b8f2-6f1f67a9f720.pdf",
            "image": "../static/images/degrees/cs50_harvard.png"
        },
        {
            "name": "OSEPI 2021 - Special Distinction District Stage",
            "url": "../static/images/degrees/osepi_special_judet.png",
            "image": "../static/images/degrees/osepi_special_judet.png"
        }
    ],
    [
        {
            "name": "EmpowerSoft 2021 - National Mention",
            "url": "https://empowersoft.ro/concurs/diplome/sectiunea5/Diploma_PM_P-E160.pdf",
            "image": "../static/images/degrees/empowersoft_mention_national.png"
        },
        {
            "name": "Phi 2020 - National Mention",
            "url": "../static/images/degrees/phi_mentiune_nationala.png",
            "image": "../static/images/degrees/phi_mentiune_nationala.png"
        },
        {
            "name": "Computer Science Olympics 2020 - District Mention",
            "url": "../static/images/degrees/olimpiada_info_mentiune_judet.png",
            "image": "../static/images/degrees/olimpiada_info_mentiune_judet.png"
        }
    ],
    [
        {
            "name": "NYU - Introduction to Programming in C++",
            "url": "https://courses.edx.org/certificates/74ca9df1ce4540db93a8359369a43d21",
            "image": "../static/images/degrees/CPP.PRG.1 NYU.png"
        },
    ],
]
contact = [
    [
        {
            "name": "Email",
            "url": "mailto:radu.voinea.mihai@gmail.com",
            "image": "../static/images/contact/mail.png"
        },
        {
            "name": "LightDream#4379",
            "url": "https://discord.gg",
            "image": "../static/images/contact/discord.png"
        },
        {
            "name": "GitHub",
            "url": "https://github.com/L1ghtDream",
            "image": "../static/images/contact/github.png"
        }
    ],
]


def index(request):
    return render(request, "index.html")


def portfolio(request, type):
    if type == "projects":
        return projects(request)
    elif type == "degrees":
        return degrees(request)
    elif type == "contact":
        return contact(request)


def projectsView(request):
    return render(request, "display.html", {
        "display": {
            "Projects": projects,
            "Servers": servers,
            "Games": games
        },
    })


def degreesView(request):
    return render(request, "display.html", {
        "display": {
            "Degrees": degrees
        }
    })


def contactView(request):
    return render(request, "display.html", {
        "display": {
            "Contact": contact
        }
    })


def projectsViewDev(request):
    entries = list(Entry.objects.all())
    projects = []
    servers = []
    for entry in entries:
        if entry.type == "project":
            projects.append(entry)
        elif entry.type == "server":
            servers.append(entry)

    return render(request, "display-dev.html", {
        "display": {
            "Servers": servers,
            "Projects": projects,
        },
    })


licences = {
    "skywars": "43a3cd99-2945-4219-85c0-e88156133ebd"
}


def licence(request, plugin):
    return HttpResponse(licences.get(plugin), content_type="text/plain")
