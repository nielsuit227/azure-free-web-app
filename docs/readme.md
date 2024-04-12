# Free Web App on Azure

This repository contains the infrastructure templates for an (almost) free web application on Azure. 

## Requirements

- Authentication handled by Entra
- RBAC in the backend
- Support Django & React

## Azure Guides

[Static Web App API](https://learn.microsoft.com/en-us/azure/static-web-apps/add-api?tabs=vanilla-javascript)
[App Service RBAC](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-enable-rbac)
[Django Startup](https://stackoverflow.com/questions/60807485/running-migrations-as-a-part-of-an-ms-azure-app-service-release-pipeline-for-a-d)
[Deploy Django](https://learn.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app?tabs=flask%2Cwindows&pivots=azure-portal)
[Django production settings](https://learn.microsoft.com/en-us/azure/app-service/configure-language-python#production-settings-for-django-apps)

## Components

- Database - Postgres Flexible Server
- Backend - App Service
- Frontend - Static Web App (App Service)
- CI/CD - Github Actions
