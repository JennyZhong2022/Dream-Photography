# DreamPhotography

## Introduction
DreamPhotography is a web-based application designed for wedding photography booking and management. It allows clients to find and book photographers for their wedding, while providing a platform for photographers to showcase their work and manage bookings. It is deployed to Heroku: [DreamPhotographer](https://dreamphotography-f9294ed19bab.herokuapp.com/)


## Features
- Photographer and client account registration and management
- Photographer portfolio galleries
- Client-photographer messaging system
- Photo upload and management
- Booking and scheduling functionalities

## Installation

### Prerequisites
- Python 3.x
- Django 3.x
- Other dependencies in `requirements.txt`

### Setup
1. Clone the repository:

git clone https://github.com/your-username/dreamphotography.git

2. Navigate to the project directory:

`cd dreamphotography`

3. Install dependencies:

`pip install -r requirements.txt`

4. Set up the environment variables:
- Copy `.env.sample` to `.env`
- Update the `.env` file with your settings (e.g., database configurations, secret keys)

5. Run migrations:

`python3 manage.py migrate`


6. Start the development server:

`python3 manage.py runserver`


7. Open the application in a web browser:

http://localhost:8000


## Usage

### As a Photographer
- Register as a photographer
- Set up your portfolio gallery
- Respond to client messages and booking requests

### As a Client
- Register as a client
- Browse photographer portfolios
- Send messages and book photographers for your wedding


## Screenshots

![Screenshot Description](src/screenshots/slot-machine.jpg)
![Screenshot Description](src/screenshots/play-table.jpg)

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any queries or suggestions, please contact us at email:(zhongxiao2017@gmail.com).

---

© 2023 DreamPhotography. All rights reserved.
