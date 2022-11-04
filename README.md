# Wings Prometheus Monitoring

---

### Introduction

This is a simple application to monitor [Wings](https://pterodactyl.io/wings/1.0/installing.html) instances
using [Prometheus](https://prometheus.io/). This application is designed to run separated from the wings instance(s).
The configuration is done via environment variables.

### Installation

#### Using Docker

```bash
docker run -d \
    -e CHECK_INTERVAL_S=5\
    -e WINGS_1_URL=http://localhost:8080 \
    -e WINGS_1_TOKEN=replaceMeWithTheToken \
    -e PORT=9001 \
    -p 9001:9001 \
    --name wings-prometheus \
    --restart unless-stopped \
    kristofhetenyi228/wings-prometheus-monitoring:stable
```
_You can add as many WINGS_N_URL and WINGS_N_TOKEN as you want. 
The N is the number of the wings instance. (The numbering must be continuous)_

Additionally, you can configure the container with a dot-env file (See [example .env](example.env)):
```bash
docker run -d \
    --env-file .env \
    -p 9001:9001 \
    --name wings-prometheus \
    --restart unless-stopped \
    kristofhetenyi228/wings-prometheus-monitoring:stable
```

#### Using docker-compose
    
```yaml
version: "3.8"
services:
  wings-prometheus-monitoring:
    image: kristofhetenyi228/wings-prometheus-monitoring:stable
    container_name: wings-prometheus-monitoring
    restart: unless-stopped
    ports:
      - "9001:9001"
    environment:
      - PORT=9001
      - CHECK_INTERVAL_S=5
      - WINGS_1_URL=https://localhost:8080
      - WINGS_1_TOKEN=REPLACEMEWITHYOURTOKEN

```

Example can be found: [docker-compose.yml](docker-compose.yml)

```bash
# Separated compose plugin
docker-compose up -d

# Built in compose plugin
docker compose up -d
```

#### Using Python interpreter

Requirements:
- Python 3.8 or higher
- Pip 21.0.1 or higher

Linux:
```bash
# Clone the repository
git clone https://github.com/TheDoctor028/wings-prometheus-monitoring.git
cd wings-prometheus-monitoring/src
# Install the dependencies
pip install -r requirements.txt
# Set up your environment variables (See example .env)
vi .env
# Start the application
python main.py
```

### Configuration
The configuration is done via environment variables.

| Name             | Default Value         | Description                                                                                                                                                                      |
|------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PORT             | 9001                  | The port where the monitoring http server will listen.                                                                                                                           |
| CHECK_INTERVAL_S | 5                     | The time between, checking the wings status. In seconds.                                                                                                                         |
| WINGS_N_URL      | http://localhost:8080 | The url of an wings instance (protocol must be included). The N is the number of the wings instance. (The numbering must be continuous) You can add as many of this as you want. |
| WINGS_N_TOKEN    | REPLACEME             | The token to authenticate to wings instance. The N is the number of the wings instance. (The numbering must be continuous) You can add as many of this as you want.              |

**WARNING**

_The number of WINGS_N_URL and WINGS_N_TOKEN must be match._
_The numbers must be continuous._

### Docker

**Official docker image**:

[https://hub.docker.com/r/kristofhetenyi228/wings-prometheus-monitoring](https://hub.docker.com/r/kristofhetenyi228/wings-prometheus-monitoring)

#### Tags
- `latest` - Latest version (Most of the time the `master` branch)
- `stable` - Stable version (Latest release)
- `vX.X.X` - Specific version
