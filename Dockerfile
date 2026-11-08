FROM python:3.14-slim

LABEL org.opencontainers.image.title="Ficha técnica APP-06 Recetas Rápidas"
LABEL org.opencontainers.image.authors="jantoniocollado03, luciano12gg, fregona33"
LABEL org.opencontainers.image.source="https://github.com/luciano12gg/Trabajo-Python"
LABEL org.opencontainers.image.version="1.0.0"

WORKDIR /app

COPY ficha_app.py .

CMD ["python", "ficha_app.py"]
