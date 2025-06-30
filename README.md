# synology-notification

[![Github](https://img.shields.io/badge/Github-100000.svg?logo=github&logoColor=white)](https://github.com/ChowRex/synology-notification) ![Python](https://img.shields.io/badge/Python-14354C.svg?logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000.svg?logo=flask&logoColor=white) [![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://hub.docker.com/r/chowrex/synology-notification) [![codecov](https://codecov.io/gh/ChowRex/synology-notification/graph/badge.svg?token=DK06DH99KO)](https://codecov.io/gh/ChowRex/synology-notification)

Synology DSM notification webhook, work with Synology Web Station.

## How to use

### Set up service

#### 🐳 With `Docker`

<details><summary>Click here for details</summary>

##### Install and enable [Container Manager](https://www.synology.com/en-us/dsm/packages/ContainerManager) on your Synology DSM

1. Login your DSM then open `Package Center` application ➡️ Search bar input `container manager` ➡️ Get in `Container Manager` application.

    ![InstallContainerManager](synology_notification/static/image/InstallContainerManager.png)

2. If you've installed this package, make it stay in `Running`status, if not, install it then keep it run.

    ![MakeContainerManagerRunning](synology_notification/static/image/MakeContainerManagerRunning.png)

##### Pull image

1. Open `Container Manager` application, navigate to `Registry` section, search keyword `chowrex` ➡️ `chowrex/synology-notification` ➡️ `Download`

    ![FindOutDockerImage](synology_notification/static/image/FindOutDockerImage.png)

2. Use `latest` tag, click `Download`

    ![UseLatestDockerImageTag](synology_notification/static/image/UseLatestDockerImageTag.png)

##### Run container

1. Goto `Image`, select the image just downloaded, click `Run`

    ![RunDockerImage](synology_notification/static/image/RunDockerImage.png)

2. Check `Enable auto-restart` checkbox, then click `Next` button.

    ![EnableAutoRestart](synology_notification/static/image/EnableAutoRestart.png)

3. Set the local port to `6789` *(Or any number  between 1024 - 65535, if the port you specify has been taken, change another one)*,  then click `Next` button.

    ![SetContainerLocalPort](synology_notification/static/image/SetContainerLocalPort.png)

4. Overview all settings and click `Done` button.

    ![OverviewAllContainerSettings](synology_notification/static/image/OverviewAllContainerSettings.png)

5. After wait for a while, click the container name *(Here is `chowrex-synology-notification-1` )* to enter the detail of container.

    ![EnterContainerDetail](synology_notification/static/image/EnterContainerDetail.png)

6. Click the `Log` tab to see all logs, if everything is OK, some info logs will appear.

    ![ContainerInfoLogs](synology_notification/static/image/ContainerInfoLogs.png)

</details>

#### 🌐 With `Web Station`

<details><summary>Click here for details</summary>

##### Install and enable [Web Station](https://www.synology.com/en-us/dsm/packages/WebStation) on your Synology DSM

1. Login your DSM then open `Package Center` application ➡️ Search bar input `web station` ➡️ Get in `Web Station` application.

    ![FindOutWebStation](synology_notification/static/image/FindOutWebStation.png)

2. If you've installed this package, make it stay in `Running`status, if not, install it then keep it run.

    ![MakeSureWebStationIsRunning](synology_notification/static/image/MakeSureWebStationIsRunning.png)

##### Install and enable [Python 3.9 ](https://www.synology.com/en-us/dsm/packages/Python3.9)on your Synology DSM

Follow the same path, install `Python 3.9` and make it stay in `Running` status.

![InstallPython39](synology_notification/static/image/InstallPython39.png)

![MakePython39Running](synology_notification/static/image/MakePython39Running.png)

##### Copy this repository code into your web directory

1. Open `File Station` application, navigate to `web` directory, click `Create` ➡️ `Create folder`

    ![CreateANewFolder](synology_notification/static/image/CreateANewFolder.png)

2. Enter name then click `OK`

    ![InputFolderName](synology_notification/static/image/InputFolderName.png)

3. Navigate into the new folder, click `Action` ➡️ `Upload - Skip`, upload all the files.

    ![UploadAllCode](synology_notification/static/image/UploadAllCode.png)

##### Create a Python profile

1. Open `Web Station` application, Click `Script Language Settings` ➡️ `Python` ➡️ `Create`.

    ![CreateAPythonService](synology_notification/static/image/CreateAPythonService.png)

2. Input `Profile Name` & `Description`, then click `Next`.

    - Profile Name: *Webhook*
    - Description: *Use for system notification*

    ![InputProfileNameAndDescription](synology_notification/static/image/InputProfileNameAndDescription.png)

3. Set `Process` to `1`, `Max.request count` to `1024`, then click `Next`.

    ![SetProcessAndMaxRequestCount](synology_notification/static/image/SetProcessAndMaxRequestCount.png)

4. Click `Browse` button to select the `requirements.txt` file, then click `Next` button.

    ![ClickBrowseButton](synology_notification/static/image/ClickBrowseButton.png)

    ![SelectRequirementsFile](synology_notification/static/image/SelectRequirementsFile.png)

    ![ClickNextButton](synology_notification/static/image/ClickNextButton.png)

5. Overview all settings and click `Create` button.

    ![ClickCreateButtonForPython](synology_notification/static/image/ClickCreateButtonForPython.png)

##### Create a Web service

1. Open `Web Station` application, Click `Web Service` ➡️ `Create`.

    ![CreateAWebService](synology_notification/static/image/CreateAWebService.png)

2. Select `Native script language website` ➡️ `Python 3.9` ➡️ `Webhook`, then click `Next`.

    ![SelectPythonService](synology_notification/static/image/SelectPythonService.png)

3. Input `Name`/`Description`, then select the correct `Document root` and `WSGI file`, click `Next`.

    - Name: *webhook-service*
    - Description: *Use for system webhook notification*

    ![ConfirmGeneralSettings](synology_notification/static/image/ConfirmGeneralSettings.png)

4. Overview all settings and click `Create` button.

    ![ClickCreateButtonForService](synology_notification/static/image/ClickCreateButtonForService.png)

##### Create a Web portal

1. Open `Web Station` application, Click `Web Portal` ➡️ `Create`.

    ![CreateAWebPortal](synology_notification/static/image/CreateAWebPortal.png)

2. Select `Web service portal` type as new portal.

    ![SelectWebServicePortal](synology_notification/static/image/SelectWebServicePortal.png)

3. Set up web service portal detail, if you have private DNS server, you can choose `Name-based` type; For most common scenarios, choose the `Port-based`

    ![SelectPortalDetails](synology_notification/static/image/SelectPortalDetails.png)

</details>

### Verify service

Use your browser to visit the service page, for common scenarios, try: http://YOUR-DMS-IP:6789

If everything is OK, the website will show this document.

### Configure System notification settings

<details><summary>Click here to show</summary>

1. Open `Contorl Panel` application ➡️ `Notification` ➡️ `Webhooks` ➡️ `Add`

    ![CreateAWebhook](synology_notification/static/image/CreateAWebhook.png)

2. Chose the `Custom` type provider and `All` rule, then click `Next`button.

    ![ChoseProviderAndRule](synology_notification/static/image/ChoseProviderAndRule.png)

3. Input `Provider name`&`Webhook URL`(For common scenarios, use: http://YOUR-DMS-IP:6789), then click `Next` button.

    - Provider Name: *Synology Webhook*
    - Webhook URL: *http://YOUR-DMS-IP:6789?api=wecom_group_bot&text=@@TEXT@@*

    ![InputNameAndWebhook](synology_notification/static/image/InputNameAndWebhook.png)

4. Set `HTTP Method` to `POST`, then click the `Add Header` button, fill the API provider's required header keys and values, at the `HTTP Body` section,  add a key-value pair: `"api": "PROVIDER_NAME"`, then click `Apply` button.

    - Bot-Key: *YOUR_WECOM_GROUP_BOT_KEY_NOT_THE_WEBHOOK_URL*
    - Body: *{"api": "wecom_group_bot", "text": "@@TEXT@@"}*

    ![ModifyWebhookSettings](synology_notification/static/image/ModifyWebhookSettings.png)

</details>

### Verify webhook

<details><summary>Click here to show</summary>

Once you've done above, you can test this webhook by open `Contorl Panel` application ➡️ `Notification` ➡️ `Webhooks` ➡️ ***Select this web hook*** ➡️ `Send Test Message` ➡️ 🎉 Done

![TestWebhook](synology_notification/static/image/TestWebhook.png)

</details>

## Support providers

- [x] WeChat Work Group Bot 

    *By another of my open source project: [ChowRex/pywgb: Wecom(A.K.A Wechat Work) Group Bot python API.](https://github.com/ChowRex/pywgb)*

- [ ] WeChat Work Application

- [ ] DingDing Group Bot

- [ ] Lark(飞书) Group Bot

- [ ] Bark

## Create your own provider (*Technological*)

Fork this repository, then goto [docs](https://github.com/ChowRex/synology-notification/tree/main/synology_notification)
