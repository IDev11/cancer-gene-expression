# Gene Expression Analysis for Early Cancer Detection

## Overview
This project analyzes RNA-Seq data from TCGA-BRCA to detect genetic profiles for breast cancer using Apache Spark and MongoDB. It includes data preprocessing, machine learning, and visualization.

## Setup
1. Install Docker and Docker Compose.
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/gene-expression-cancer-detection.git
   ```
3. Follow instructions in `data/README.md` to download TCGA data.

## Structure
- `data/`: Instructions for TCGA data.
- `src/`: Scripts for processing, modeling, and visualization.
- `tests/`: Unit tests.
- `docs/`: Publication materials.
- `docker-compose.yml`: Docker configuration.

## Next Steps
- Download TCGA-BRCA RNA-Seq data.
- Run the Docker containers for Spark and MongoDB.

## Troubleshooting
- If the Spark container fails to start, check logs with `docker logs spark`.
- Ensure ports 8080 and 7077 are free, or modify `docker-compose.yml` to use different ports.
- Allocate at least 4GB memory to Docker (Docker Desktop > Preferences > Resources).