from django.shortcuts import redirect, render
from django.views import View

from car_app.forms import CarForm, CarFormSet
from car_app.models import Brand, Car, Color


class ManagementPanelView(View):
    def get(self, request):
        cars = Car.objects.all()
        return render(request, "management_panel.html", {"cars": cars})


class AddCarView(View):
    def get(self, request):
        form = CarForm()
        brands = Brand.objects.all()
        colors = Color.objects.all()

        return render(
            request,
            "add_car.html",
            {"form": form, "brands": brands, "colors": colors},
        )

    def post(self, request):
        form = CarForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("management_panel")
        return render(request, "add_car.html", {"form": form})


class UpdateCarsView(View):
    def get(self, request):
        cars = Car.objects.all()

        initial_data = [
            {
                "id": car.id,
                "model": car.model,
                "brand": car.brand,
                "main_color": car.main_color,
                "value": car.value,
                "production_costs": car.production_costs,
                "transportation_costs": car.transportation_costs,
                "total": car.total,
            }
            for car in cars
        ]

        formset = CarFormSet(initial=initial_data)

        return render(
            request,
            "car_update.html",
            {
                "formset": formset,
            },
        )

    def post(self, request):
        formset = CarFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                car_id = form.cleaned_data.get("id")
                model = form.cleaned_data.get("model")
                brand = form.cleaned_data.get("brand")
                main_color = form.cleaned_data.get("main_color")
                value = form.cleaned_data.get("value")
                production_costs = form.cleaned_data.get("production_costs")
                transportation_costs = form.cleaned_data.get(
                    "transportation_costs"
                )

                car = Car.objects.get(id=car_id)
                car.model = model
                car.brand = brand
                car.main_color = main_color
                car.value = value
                car.production_costs = production_costs
                car.transportation_costs = transportation_costs
                car.save()

            return redirect("management_panel")

        cars = Car.objects.all()

        initial_data = [
            {
                "id": car.id,
                "model": car.model,
                "brand": car.brand,
                "main_color": car.main_color,
                "value": car.value,
                "production_costs": car.production_costs,
                "transportation_costs": car.transportation_costs,
                "total": car.total,
            }
            for car in cars
        ]

        formset = CarFormSet(initial=initial_data)

        return render(request, "car_update.html", {"formset": formset})
