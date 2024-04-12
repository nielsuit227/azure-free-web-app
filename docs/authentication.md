# Create App Registration

1. Go to Entra > App Registrations > Create App Registration. 
2. Provide the details. Important is the redirect URI, select SPA, and add the static web URL + `/.auth/login/aad/callback`.
3. Add a client secret

# Define the app configuration

1. Add the `staticwebapp.config.json`
2. Specify the routes, with the `[authenticated]` attribute.
3. Specify the authentication provider (requires Tenant ID)

# Add Static Web App Environmental Variables

Note your Application Client ID and Application Secret, and specify these in the environmental variables (`APP_CLIENT_ID` and `APP_CLIENT_SECRET`).
