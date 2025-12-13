import openpyxl
from django.http import HttpResponse
from .models import CSOEvent

def export_events_xlsx(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "CSO Events"

    # Header row
    ws.append([
        "Location", "Latitude", "Longitude", "Start Time", "End Time",
        "Overflow Volume (m3)", "Cause", "Severity", "Description"
    ])

    # Data rows
    for e in CSOEvent.objects.all():
        ws.append([
            e.location,
            e.latitude,
            e.longitude,
            e.start_time.strftime("%Y-%m-%d %H:%M"),
            e.end_time.strftime("%Y-%m-%d %H:%M"),
            e.overflow_volume_m3,
            e.cause,
            e.severity,
            e.description,
        ])

    response = HttpResponse(
        content=openpyxl.writer.excel.save_virtual_workbook(wb),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="cso_events.xlsx"'
    return response
