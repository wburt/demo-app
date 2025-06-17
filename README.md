# OpenShift Demo Application

## Overview

This project provides a simple Python application designed to help users quickly learn the basics of deploying and managing applications on OpenShift. The demo app serves as an educational tool for understanding fundamental OpenShift concepts including deployments, services, routes, and environment variables.

## Purpose

The purpose of this demo is to:

- Provide hands-on experience with OpenShift deployment workflows
- Familiarize users with both the OpenShift CLI (`oc`) and web console
- Demonstrate how to examine and modify application configurations
- Showcase the use of Helm charts for Kubernetes-based deployments

## Getting Started

1. Ensure you have access to an OpenShift cluster
2. Install and set up WSL (Windows Subsystem for Linux)
3. Install the OpenShift CLI (`oc`) and Helm in your WSL environment
4. Follow the detailed instructions in [1_Openshift_Tutorial.md](./learning_resources/tutorials/1_Openshift_Tutorial.md)

## Tutorials

### Basic OpenShift Deployment
The [1_Openshift_Tutorial.md](./learning_resources/tutorials/1_Openshift_Tutorial.md) document provides an introduction on:

- Logging into OpenShift via the command line
- Deploying the application using Helm
- Exploring the deployed application
- Viewing and modifying configuration settings
- Working with environment variables

### Managing Environment Variables with Helm
The [2_Helm_Variables_Tutorial.md](./learning_resources/tutorials/2_Helm_Variables_Tutorial.md) shows how to:

- Configure environment variables directly in Helm chart files
- Modify the values.yaml and deployment.yaml files
- Deploy and verify your changes
- Update variables using Helm upgrades

## Target Audience

This demo is ideal for:
- Developers new to OpenShift
- Operations teams learning container orchestration
- Anyone looking to understand deployment workflows in OpenShift

## Project Structure

- `app.py` - Simple Python web application
- `Dockerfile` - Container definition for the application
- `charts/` - Helm chart for deploying to OpenShift
- `1_Openshift_Tutorial.md` - Step-by-step tutorial for basic OpenShift deployment
- `2_Helm_Variables_Tutorial.md` - Guide for managing environment variables with Helm