#!/bin/bash

sudo docker-compose --env-file ./data/env down
sudo docker-compose --env-file ./data/env up --build -d

