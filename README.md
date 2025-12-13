# CSO_Event_Tracker
A Django-based web application for reporting, storing, and visualizing 
Combined Sewer Overflow (CSO) events.

This project includes:

    A form for submitting CSO events

    Database storage with Django

    A dashboard with an interactive Leaflet map

    Severity-colored markers (high=red, medium=orange, low=green)

    A Chart.js bar chart showing overflow volumes

    Ability to manually input latitude / longitude for exact mapping
    A Mitigation Action feature for recording follow-up actions associated with CSO events

    An Excel (XLSX) export function for downloading all CSO event records

    A Django admin interface for managing events and mitigation actions

    Dockerized deployment for portability

    A GitHub Actions workflow that builds the Docker image automatically

    A basic pytest + pytest-django test suite


Application Pages

Submit CSO Event:
/report/

Dashboard (map, chart, table):
/dashboard/

Add Mitigation Action:
/action/add/

Excel Export:
/export/events.xlsx

Admin Interface:
/admin/

Logs:

11/29/2025 Update:
    Django project created
    Base app created
    Models and admin configured
    Database migrations complete
    Created superuser account

12/12/2025 Update:
    Built framework for the project around Django.
    Added dashboard, leaflet map and chartjs chart.
    Configured URLs, added color coded marker for event location on map.
    Added mitigation action functionality
    Implemented Excel export feature
    Dockerized the application
    Added GitHub Actions workflow for Docker builds
    Added pytest-based testing configuration

How to run:
1: Install dependencies:
    pip install -r requirements.txt

2: Migrate:
    python manage.py migrate

3: Start Server
    python manage.py runserver