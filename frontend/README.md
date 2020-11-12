# _project_name_ Frontend

## Getting Setup

> _tip_: this frontend is designed to work with a [Flask-based backend](../backend). It is recommended you stand up the backend first, test using Postman and the test script, and then the frontend should integrate smoothly.

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run `npm install`.

### Configure Environment Variables (Optional)

Secrets (such as private API keys) shouldn't be stored directly in your React app. For this reason, we use environment variables to setup app secrets such as your application's Auth0 ClientID. [More information here](https://create-react-app.dev/docs/adding-custom-environment-variables/).

Create a `.env` file in the frontend directory's root and include the needed variables.

### Running The Frontend

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`. After starting the server successfully, open `http://localhost:3000` to view it in the browser. The page will reload automatically if you make edits.
