# Quick Guide: Managing Environment Variables with Helm Charts

This tutorial will show you how to modify environment variables in your OpenShift demo application using Helm charts and an IDE.

## Prerequisites

- Access to an OpenShift cluster
- WSL installed and set up ([Microsoft guide](https://learn.microsoft.com/en-us/windows/wsl/install))
- `oc` CLI installed in WSL ([BC Gov guide](https://developer.gov.bc.ca/docs/default/component/platform-developer-docs/docs/openshift-projects-and-access/install-the-oc-command-line-tool/))
- `helm` installed in WSL ([Helm guide](https://helm.sh/docs/intro/install/))
- Visual Studio Code or another IDE with YAML support
- Basic understanding of YAML syntax
- Familiarity with the deployment steps from [Openshift_Tutorial.md](./Openshift_Tutorial.md)

### Setting Up Visual Studio Code

**Install Visual Studio Code** if you haven't already ([Download VS Code](https://code.visualstudio.com/download))

## Setting the Environment Variable

In the previous tutorial, you learned how to set the `DEMO_MESSAGE` environment variable using the OpenShift web interface or the `oc set env` command. Now, we'll configure this variable directly in the Helm chart files.


### 1. Open the demo_app directory in your IDE

   ```powershell
   code .
   ```

### 2. Modify the values.yaml File

1. **Open the values.yaml file**

2. **Add the environment variables section** to your values.yaml file:
   ```yaml
   # Add this section to your values.yaml file
   env:
     DEMO_MESSAGE: "Hello from Helm values!"
   ```

   This creates a simple static value that can be referenced in the deployment template.

### 3. Update the deployment.yaml Template

Now you need to modify the deployment template to use the environment variable values from the values.yaml file.

1. **Open the deployment.yaml file**

2. **Locate the container specification** in the deployment template. This will be in the `spec.template.spec.containers` section.

3. **Add or modify the env section** with a static assignment for DEMO_MESSAGE:
   ```yaml
   # Find the containers section and add this inside it (around line 40-50)
   containers:
     - name: {{ .Chart.Name }}
       # ...existing configuration like image and ports...
       env:
         - name: DEMO_MESSAGE
           value: {{ .Values.env.DEMO_MESSAGE | quote }}
       # ...rest of container configuration...
   ```

   This template code will take any environment variables defined in the `env` section of your values.yaml and add them to your container.

## Deploy the Application to See Your Changes

Now that you've updated your Helm chart files, you need to deploy or upgrade your application to see the changes.

### 1. Deploy or Upgrade Your Application

If you're **deploying for the first time**:
```sh
helm install <your initials> ./charts
```

If you've **already deployed** and need to upgrade:
```sh
helm upgrade <your initials> ./charts
```

You should see output similar to:
```
NAME: <your initials>
LAST DEPLOYED: Wed Jun 12 10:30:00 2025
NAMESPACE: d4a7e0-dev
STATUS: deployed
REVISION: 1  # or a higher number if upgrading
```

### 2. Verify the Deployment

Check that your pods are running with the updated configuration:
```sh
oc get pods -l app.kubernetes.io/instance=<your initials>
```

Wait until the status shows `Running`.

### 3. Access Your Application's URL

To find your application's URL:
```sh
oc get route <your initials>-demo-app
```

This will display the hostname for your application. Open this URL in your browser to see your application with the updated environment variable.

You should see your custom message displayed on the web page.

## Making Further Changes

To modify the environment variable:

1. Edit the values.yaml file again
2. Update the `DEMO_MESSAGE` value
3. Run `helm upgrade <your initials> ./charts`

If you want to add additional environment variables, you'll need to add each one explicitly in both the values.yaml file and the deployment.yaml template.

> **Note**\
> Changes made through Helm will trigger a new deployment, replacing pods with the updated configuration.

## Removing Your Application

When you are finished, you can remove your application:
```sh
helm uninstall <your initials>
```

## References
- [Helm Documentation](https://helm.sh/docs/)
- [Helm Templates Guide](https://helm.sh/docs/chart_template_guide/)
- [Visual Studio Code](https://code.visualstudio.com/docs)
