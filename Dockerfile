# Use the official Python image
   FROM python:3.10

   # Set the working directory in the container
   WORKDIR /src

   # Copy the local code to the container
   COPY . .
   # Install FastAPI and Uvicorn
   RUN pip install fastapi uvicorn

   RUN pip install -r src/requirements.txt

# Expose the port the app runs on
   EXPOSE 8000

   # Command to run the application
   CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
