# SacaNotes
Why read a book when you can get a comprehensive abstract from SacaNotes?

## About the application
This application is built using top notch web and Python development practices. It's not succeptible to any kind of attacks... AT ALL. This app doesn't sanitize query string parameters and [uses them to access the file system](container/src/main.py#L38-L41), because who wouldn't.

The app is meant to be [containerized](container/Dockerfile) and [deployed via Kubernetes](kubernetes/books-deployment.yaml) to Azure. If you want to go full pro with Kubernetes in Azure, you can use the apimodel.json file along with [acs-engine](https://github.com/Azure/acs-engine).  