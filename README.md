# digitalocean-langchain

Boilerplate for deploying LangChain on Digitalocean App Platform

## Installation and running locally

1. Create and activate a virtual environment

   ```sh
   virtualenv MY_ENV
   source MY_ENV/bin/activate
   ```

1. Install packages with pip

   ```sh
   cd ad-gpt
   pip install -r requirements.txt
   ```

1. Set up your .env file

   - Duplicate `.env.example` to `.env`

1. Run the project

   ```sh
   flask --app run app
   ```

## Deploying to Google Cloud Run (Requires CloudSDK)

1. Use Google builds command to create the docker image in the container registry

   ```sh
   gcloud builds submit --tag gcr.io/PROJECT_ID/langchain
   ```

1. Create a Cloud Run service

   ```sh
   gcloud run deploy --image gcr.io/PROJECT_ID/langchain --timeout=300 --platform managed
   ```

1. Verify the deployed cloud run service in the Google Cloud Console
