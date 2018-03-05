#!/bin/bash

# Install Nginx
helm install stable/nginx-ingress --name sacacorp-ingress --set rbac.create=true

# Get external facing IP for ingress controller
kubectl get service sacacorp-ingress-nginx-ingress-controller 

# Add a DNS entry with your domain provider (e.g GoDaddy)
# *** this is done via web browser ***

# Install Lets Encrypt
helm install --name sacacorp-lego --set config.LEGO_EMAIL=gsacavdm@sacacorp.com --set config.LEGO_URL=https://acme-v01.api.letsencrypt.org/directory stable/kube-lego --set rbac.create=true

# Create Kubernetes ingress (sets up both nginx ingress and lego ingress)
kubectl create -f ingress.yaml