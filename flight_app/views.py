from django.shortcuts import render, redirect
from .models import Airport, Route
from .forms import RouteForm, SearchForm

# Add Route
def add_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_routes')
    else:
        form = RouteForm()
    return render(request, 'add_route.html', {'form': form})


# View All Routes
def view_routes(request):
    routes = Route.objects.all()
    return render(request, 'view_routes.html', {'routes': routes})


# Nth Left or Right Node
def nth_node(request):
    result = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            start_code = form.cleaned_data['start_airport']
            direction = form.cleaned_data['direction']
            n = form.cleaned_data['n']

            current_airport = Airport.objects.filter(code=start_code).first()
            if not current_airport:
                result = "Invalid Airport Code"
            else:
                for i in range(n):
                    route = Route.objects.filter(source=current_airport, position=direction).first()
                    if not route:
                        result = f"No {direction} node found after {i} steps."
                        break
                    current_airport = route.destination
                else:
                    result = f"{n}th {direction} node is {current_airport.code}"
    else:
        form = SearchForm()
    return render(request, 'nth_node.html', {'form': form, 'result': result})


# Longest Route
def longest_route(request):
    route = Route.objects.order_by('-duration').first()
    return render(request, 'longest_route.html', {'route': route})


# Shortest Route Between Two Airports
def shortest_route(request):
    routes = Route.objects.order_by('duration')
    shortest = routes.first() if routes else None
    return render(request, 'shortest_route.html', {'route': shortest})
def home(request):
    return render(request, 'flight_app/home.html')

