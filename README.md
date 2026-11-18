# 🚌 Cloud-Based Bus Pass Management System

## Project Overview
A web-based student bus pass management application built using Python and Streamlit. It allows students to register, apply for bus passes, and track application status. Administrators can review applications and update their status.

## Features
- Student Registration
- Online Bus Pass Application
- Monthly, Quarterly and Yearly Pass Options
- Application Status Tracking
- Admin Login and Logout
- Admin Dashboard
- Approve, Reject and Pending Status Management
- SQLite Database Integration
- Dashboard Metrics and Application Records

## Technologies Used
- Python
- Streamlit
- SQLite
- Pandas

## Project Structure
- `app.py` - Student application
- `admin_dashboard.py` - Admin dashboard
- `admin_login.py` - Demo admin login
- `database.py` - Database and table creation
- `requirements.txt` - Project dependencies

## Installation
Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Run Student Application
```bash
python -m streamlit run app.py
```

## Run Admin Dashboard
Open another terminal and run:

```bash
python -m streamlit run admin_dashboard.py --server.port 8600
```

## Database
The application uses SQLite to store student and bus pass application records locally.

## Project Scope
This is a working local prototype. Cloud hosting and a persistent cloud database are future deployment improvements.

The included admin login uses demo credentials and is not intended for production use.

## Developer
Salman Reyaz Bhat