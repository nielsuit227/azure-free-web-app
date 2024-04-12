# Free Web App on Azure

This repository contains the infrastructure templates for an (almost) free web application on Azure. 

## Requirements

- Authentication handled by Entra
- RBAC in the backend
- Support Django & React

## Azure Guides

### Backend

[Deploy Django](https://learn.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app?tabs=flask%2Cwindows&pivots=azure-portal)
[Django Startup](https://stackoverflow.com/questions/60807485/running-migrations-as-a-part-of-an-ms-azure-app-service-release-pipeline-for-a-d)
[Django production settings](https://learn.microsoft.com/en-us/azure/app-service/configure-language-python#production-settings-for-django-apps)

### Frontend

[SWA Configuration](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration)
[Entra Auth for Web App](https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-aad?tabs=workforce-tenant)
[App Service RBAC](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-enable-rbac)
[API for SWA](https://learn.microsoft.com/en-us/azure/static-web-apps/apis-app-service)


## Components

- Database - Postgres Flexible Server
- Backend - App Service
- Frontend - Static Web App (App Service)
- CI/CD - Github Actions
