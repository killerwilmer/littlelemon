# LittleLemon

LittleLemon is a project to manage user authentication and table bookings. Below are the API endpoints and corresponding CURL commands to interact with the service.

```sh
# User Management

# Create User
# Endpoint: http://127.0.0.1:8000/auth/users/
curl --request POST \
  --url http://localhost:8000/auth/users/ \
  --header 'Content-Type: multipart/form-data' \
  --header 'User-Agent: insomnia/2023.5.8' \
  --form email=test2@little.com \
  --form username=test2 \
  --form password=Abc123

# List Users
# Endpoint: http://127.0.0.1:8000/auth/users/
curl --request GET \
  --url http://localhost:8000/auth/users/ \
  --header 'Authorization: Token 123' \
  --header 'User-Agent: insomnia/2023.5.8'

# Booking Management

# Create Booking
# Endpoint: http://127.0.0.1:8000/tables/
curl --request POST \
  --url http://127.0.0.1:8000/tables/ \
  --header 'Authorization: Token 123' \
  --header 'Content-Type: multipart/form-data' \
  --header 'User-Agent: insomnia/2023.5.8' \
  --form name=Edwin \
  --form no_of_guests=10 \
  --form booking_date=2024-05-26T10:53:00Z

# List All Bookings
# Endpoint: http://127.0.0.1:8000/tables/
curl --request GET \
  --url http://127.0.0.1:8000/tables/ \
  --header 'Authorization: Token 123' \
  --header 'User-Agent: insomnia/2023.5.8'
