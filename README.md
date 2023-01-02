# python-deployment
project for keeping necessary set of files for deployment via CI-CD tools

## OpenShift
```sh
oc new-app https://github.com/cherkavi/python-deployment.git#main --name=$OC_APP_NAME
oc create route edge $OC_APP_NAME --service=$OC_APP_NAME
```
