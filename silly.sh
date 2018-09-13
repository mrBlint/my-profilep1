#!/bin/bash

sudo yum -y update
sudo yum -y install httpd apache
sudo systemctl restart httpd.service

