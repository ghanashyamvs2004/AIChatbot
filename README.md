# Thejus Engineering College Student Chatbot

## Project Overview

The Thejus Engineering College Student Chatbot is a web-based chatbot developed using Python and Flask. The chatbot is designed to assist students by providing quick answers to commonly asked questions related to the college, such as admissions, courses, placements, hostel facilities, contact information, and college location.

The chatbot uses an intent-based approach where user messages are matched with predefined patterns stored in a JSON file. Based on the detected intent, the chatbot generates an appropriate response and displays it through a simple and interactive web interface.

## Objectives

* Provide instant answers to common student queries.
* Reduce the need for repetitive manual responses.
* Demonstrate the implementation of chatbot technology using Python.
* Learn web development concepts using Flask, HTML, CSS, and JSON.

## Features

* User-friendly chat interface.
* Intent-based response system.
* College information support.
* Admission-related query handling.
* Placement information assistance.
* Hostel and accommodation information.
* Contact and location details.
* Fast response generation.
* Easy to customize and expand.

## Technologies Used

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Data Storage

* JSON (intents.json)

## Working Principle

1. The user enters a message in the chatbot interface.
2. The message is sent to the Flask backend.
3. The backend loads predefined intents from the intents.json file.
4. The chatbot compares the user's message with the available patterns.
5. When a matching pattern is found, the corresponding response is returned.
6. The response is displayed in the chat window.

## Project Structure

AIchatbot/
│
├── app.py
├── intents.json
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md

## Learning Outcomes

Through this project, the following concepts were explored:

* Python programming
* Flask web framework
* JSON data handling
* Frontend and backend integration
* Chatbot development fundamentals
* HTTP requests and responses
* User interface design

## Future Enhancements

* AI-powered responses using machine learning.
* Database integration.
* Student login system.
* Attendance and result tracking.
* Voice-based interaction.
* Integration with college management systems.
* Multilingual support.
* Mobile application version.

## Conclusion

This project demonstrates the development of a simple yet functional student chatbot that can assist users with college-related information. It serves as a beginner-friendly introduction to chatbot development and full-stack web application design using Python and Flask.
