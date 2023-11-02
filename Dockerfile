FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN python -m venv .venv
ENV PATH="/app/.venv/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
