#!/bin/bash

export DATABASE_URL="sqlite:///./smart_home.db"
export SECRET_KEY="your_secret_key"

uvicorn app.main:app --reload