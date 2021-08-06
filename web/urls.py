from django.urls import path

from web import views

urlpatterns = [
    path("", views.index),
    path("projects", views.projectsView, name="projects"),
    path("projects-dev", views.projectsViewDev, name="projects-dev"),
    path("degrees", views.degreesView, name="degrees"),
    path("contact", views.contactView, name="contact"),
    # path("<str:type>", views.portfolio),
    # path("<str:type>/", views.portfolio)
]
