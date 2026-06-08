# My VS Code Self-Learning AI Project

This is a starter Visual Studio Code project with a self-learning AI model exposed via FastAPI.

## Setup

pip install -r requirements.txt

## Run API

uvicorn src.main:app --reload


Invoke-RestMethod -Uri "http://localhost:8000/predict" `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"features":[0.1,0.2,0.3,0.4]}'


Invoke-RestMethod -Uri "http://localhost:8000/teach" `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"features":[0.1,0.2,0.3,0.4],"label":1}'


Invoke-WebRequest -Uri "http://localhost:8000/teach" `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"features":[0.1,0.2,0.3,0.4],"label":1}'


http://localhost:8000/dashboard
