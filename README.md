# DfE6_Final_Project

## DfE Cloud Specialism - Final Project
### Introduction

This project serves as the culmination of all of the topics I have covered as part of my training. It will involve the following concepts/technologies:

•	Project Management

•	Python Fundamentals

•	Python Testing

•	Git

•	Linux

•	Python Web Development

•	Databases

•	Continuous Integration and Deployment (CI/CD)

•	Cloud Fundamentals

•	Containerisation

This project is an individual project designed to demonstrate my knowledge.

## Overview

My objective with this project is to achieve the following:

•	To create a web application that integrates with a database and demonstrates CRUD functionality.

•	To utilise containers to host and deploy your application.

•	To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application.

## Planning and Introduction

For the project, I planned on creating  a website that creates properties and allows to add,  update and delete properties with their information. Additionally it allows to search any property in the database.

## Project Management and Version Control

To manage the project, I used the Jira.

![Jira Screenshot](https://user-images.githubusercontent.com/43039925/147856876-ee9bb753-0263-4c3d-b3cb-6e278531ed4f.png)

The Jira project board helped me to plan and  complete the project. The categories represent the MoSCoW method and the user stories help me to understand the features needed for the application.

## Application

The application is a microservice Flask application that serves both the frontend and backend of the application.

The frontend aspect of the app uses HTML templates to serve the web pages that allows the user to perform CRUD functionality with information from the database.

The backend aspect of the application uses SQLAlchemy to model and integrate with the database.

## CI/CD Pipeline

The CI/CD pipeline is important part of the process of the integration and release of the website. 

![CI_CD](https://user-images.githubusercontent.com/43039925/147859099-34e70702-eb7a-41f1-a947-45b8034e4c1c.png)



## Testing

By the use of pytest and Jenkins, I created the test logs, test coverages and reports. The Jenkins pipelines reads these test to translate these data into easily read information.

![Test](https://user-images.githubusercontent.com/43039925/147859257-22ce5dfb-49b3-472c-b782-b607f150532b.png)

All the tests passed 100%.

## Video 

In the video you can see the brief of the application.

https://drive.google.com/file/d/1hN8tax4lXNzal95UIfqmTxf8eRp2vteU/view?usp=sharing

