#djangobluemix

Allows you to quickly start building and deploying Django Python Apps To IBM Bluemix.

##To manually push this starter Django App to Bluemix using CF

### Getting Started

1. Create a Bluemix Account

    [Sign up][sign_up] on Bluemix.net, or use an existing account. Runtimes are free to try for one month.

2. Download and install the [Cloud-foundry CLI][cloud_foundry] tool

3. Edit the `manifest.yml` file and change the `<application-name>` to something unique and modify the `<services-name>` to reflect your own Postgres SQL database service instance on Bluemix after you create it.
```none
applications:
- name: <application-name>
memory: 256M
# This is command provided by cf -c option
command: bash ./run.sh
buildpack: https://github.com/cloudfoundry/python-buildpack
path: .
declared-services:
<services-name>:
label:postgresql
plan:100
services:
- <services-name>


```

    The name you use will determinate your application url initially, e.g. `<application-name>.mybluemix.net`.

4. Connect to Bluemix in the command line tool
  ```sh
  $ cf api https://api.ng.bluemix.net
  $ cf login -u <your user ID>
  ```

5. Create the PostGress Databse Service on in Bluemix

  ```sh
  $ cf create-service postgresql "100" postgresqlmine
  ```

6. Push it live!

  ```sh
  $ cf push
  ```

## To automate the deployment of this starter template 
Simply click on the deploy to bluemix button below to deploy this Django Python Application. 

[![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](http://goo.gl/UWpUya)

<b>Directions</b>
- Accept the default values for you the app location and name. 
- The app will deploy however the initial application start will fail because you haven't created your postgress database service. 
- The error messages in the DevOps pipeline services shows you haven't created your postgresql-qc database service.
- Create the postgress service. I used "postgresql-qc" as the name in the manifest file.  
- Bind the service to your app in the blumix dashboard  bluemix.net
- Restart your app in Bluemix
- Access the deployed app using the routesURL at the top of your app  routesURL/admin
- Use admin for user id and password and start creating users.
- Enjoy

## Troubleshooting

To troubleshoot your Bluemix app the main useful source of information are the logs, to see them, run:

  ```sh
  $ cf logs <application-name> --recent
  ```

## License

  This sample code is licensed under Apache 2.0. Full license text is available in [LICENSE](LICENSE).

## Contributing

  See [CONTRIBUTING](CONTRIBUTING.md).
  
[service_url]: https://console.ng.bluemix.net/?ace_base=true#/store/cloudOEPaneId=store&orgGuid=0372034e-31d6-41b5-8843-819c07218821&spaceGuid=737c360d-c1c3-481f-923c-e7ee0b193c28&serviceOfferingGuid=7ca52cdd-ae04-4fac-b153-47f7805583e2&fromCatalog=true
[cloud_foundry]: https://github.com/cloudfoundry/cli
[getting_started]: https://console.ng.bluemix.net/solutions/web-applications
[sign_up]: https://apps.admin.ibmcloud.com/manage/trial/bluemix.html
