import pytest
from django.urls import reverse
from car_app.models import Brand, Car, Color
from django.test import Client


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def brand():
    return Brand.objects.create(brand="Brand 1")


@pytest.fixture
def color():
    return Color.objects.create(color="Color 1")


@pytest.fixture
def car(brand, color):
    return Car.objects.create(
        model="Car 1",
        brand=brand,
        main_color=color,
        value=10000,
        production_costs=5000,
        transportation_costs=2000,
    )


@pytest.mark.django_db
def test_management_panel_view(client):
    url = reverse("management_panel")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_car_view_get(client):
    url = reverse("add_car")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_car_view_post(client, brand, color, car):
    url = reverse("add_car")
    data = {
        "model": "Car 2",
        "brand": brand.id,
        "main_color": color.id,
        "value": 15000,
        "production_costs": 6000,
        "transportation_costs": 2500,
    }

    response = client.post(url, data)

    car.refresh_from_db()

    assert response.status_code == 200
    assert Car.objects.count() == 1


@pytest.mark.django_db
def test_update_cars_view_get(client):
    url = reverse("update_cars")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_cars_view_post(client, car):
    url = reverse("update_cars")
    data = {
        "form-TOTAL_FORMS": "1",
        "form-INITIAL_FORMS": "1",
        "form-0-id": car.id,
        "form-0-model": "Updated Car 1",
        "form-0-brand": car.brand.id,
        "form-0-main_color": car.main_color.id,
        "form-0-value": 20000,
        "form-0-production_costs": 8000,
        "form-0-transportation_costs": 3000,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    car.refresh_from_db()
    assert car.model == "Updated Car 1"
    assert car.value == 20000
    assert car.total == 11000
