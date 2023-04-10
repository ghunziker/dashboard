from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from repex.pythonscript.importdata import import_master, import_passenger
from django.core.exceptions import ValidationError
import logging
from .models import ArticleMaster ,PassengerNumbers
import datetime
from plotly.offline import plot
import plotly.express as px
import pandas as pd
from .tables import Products_Table
from django_tables2 import RequestConfig

# Views
@login_required
def dashboard(request):
    data = PassengerNumbers.objects.all().order_by('date')
    plot_data = [
        {
        'Passengers': x.passengers,
        'Date': x.date
        } for x in data
    ]
    df = pd.DataFrame(plot_data)
    print(df)
    fig = px.line(df, x='Date', y='Passengers')
    fig.update_layout(yaxis_range=[0, 10000])
    line_plot = plot(fig, output_type='div')
    context = {'plot_div': line_plot}

    return render(request, 'repex/dashboard.html', context)



@login_required
def products(request):
    table = Products_Table(ArticleMaster.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'repex/products.html', {'table': table})


@login_required
def data_upload(request):
    if request.method == 'POST':
        if 'btn_ArticleMasterData' in request.POST:
            if request.FILES.get('ArticleMasterData', False):
                csv_file  = request.FILES['ArticleMasterData']
                try:
                    if not (csv_file.name.endswith('.csv') or csv_file.name.endswith('.txt')):
                        raise ValidationError('Article Master Data: Invalid file format.')
                    import_master(csv_file)
                    messages.add_message(request, messages.SUCCESS, 'Article Master successfully uploaded!')
                except ValidationError:
                    messages.add_message(request, messages.WARNING, 'Article Master Data: Invalid file format. Please upload a .csv or .txt file.')
                except Exception as e:
                    messages.add_message(request, messages.ERROR, 'An error occurred while processing the Article Master Data file.')
                    logging.getLogger('error_logger').error('An error occurred while processing the Article Master Data file.', exc_info=True)
            else:
                messages.add_message(request, messages.WARNING, 'Please select the Article Master Data file before upload.')
    
        if 'btn_PassengerNumbers' in request.POST:
            if request.FILES.get('PassengerData', False):
                csv_file  = request.FILES['PassengerData']
                try:
                    if not (csv_file.name.endswith('.csv') or csv_file.name.endswith('.txt')):
                        raise ValidationError('Passenger Numbers: Invalid file format.')
                    import_passenger(csv_file)
                    messages.add_message(request, messages.SUCCESS, 'Passenger Numbers successfully uploaded!')
                except ValidationError:
                    messages.add_message(request, messages.WARNING, 'Passenger Numbers: Invalid file format. Please upload a .csv or .txt file.')
                except Exception as e:
                    messages.add_message(request, messages.ERROR, 'An error occurred while processing the Passenger Numbers file.')
                    logging.getLogger('error_logger').error('An error occurred while processing the Passenger Numbers file.', exc_info=True)
            else:
                messages.add_message(request, messages.WARNING, 'Please select the Passenger Numbers file before upload.')
        
        if 'btn_delete' in request.POST:
            count = 0
            if ('deleteMaster') in request.POST:
                if request.POST['deleteMaster'] == 'on':
                    ArticleMaster.objects.all().delete()
                    messages.add_message(request, messages.SUCCESS, 'Deleted: Article Master')
                    count+=1
            if 'deletePassengers' in request.POST:
                if request.POST['deletePassengers'] == 'on':
                    PassengerNumbers.objects.all().delete()
                    messages.add_message(request, messages.SUCCESS, 'Deleted: Passenger Numbers')
                    count+=1
            if 'deleteTransactions' in request.POST:
                if request.POST['deleteTransactions'] == 'on':
                    count+=1
            if count == 0:
                messages.add_message(request, messages.WARNING, 'Nothing is deleted. Please select a table.')
    return render(request, 'repex/data-upload.html', {})

