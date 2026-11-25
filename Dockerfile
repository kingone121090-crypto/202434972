# OPTIONAL Trivy Dockerfile misconfiguration fixture; NEVER deploy this image.
# Deliberately not pinned by digest, and no non-root USER.
FROM python:3.9-slim
WORKDIR /opt/library
COPY . .
EXPOSE 8765
CMD ["python", "src/library_api.py"]
