<p align="center">
    <img width="150" src="https://github.com/jeraldconstantino/pili-balita/blob/main/larawan/pili-balita-icon.png" alt="Pili-Balita logo">
</p>
<h1 align="center">Pili-Balita</h1>
<h4 align="center"> Machine learning-based Android application that can classifies Philippine fake news spread throughout the social media. </h4>

## Features
- Detects Philippine fake news or articles spread in social media.
- Display the accuracy output of the three different algorithms used in the App.

## How to install and use the App
1. Make sure that you have an adequate Internet connection since the App requires to send API request to accessed the machine learning model (deployed in [Heroku](https://www.heroku.com/) cloud platform).
2. Download and install the available [APK](https://github.com/jeraldconstantino/pili-balita/blob/main/Pili-Balita.apk). 
3. Search for any Tagalog articles found in the social media and copy its content. 
4. Open the App and paste the content.
5. Click the "TUKLASIN!" button.
6. Wait for a second until the result is displayed. 

> **NOTE:** Limitation exists such as data availability. The AI model may predict an accurate result if you have provided an article that is published on 2021 and below. As of now (January, 2023), the dataset is not yet cleaned and updated with the latest news report. Thus, training and validating the AI model is highly needed and should be fix sooner.

If the result is not displaying even if you have a good Internet connection, the possible problem may exists in the Heroku side as I only used a free accessed account with that cloud platform. By following the instructions below, you can replicate the App and deploy the AI model in Heroku (or any cloud platform service) to make it working.

## Usage
To use this project, make sure that you have [Git](https://git-scm.com/) and [Python](https://www.python.org/downloads/) (which includes PIP) installed in your machine. 

> **NOTE:** As of now, Python 3.10 (and below) is the only compatible version with the required dependencies. The latest Python version can't run this application due to incompatibility with the Kivy package. 

Kindly follow the instructions below:    
* Use `cd` command to go to your desired directory where you want to save the repository.
1. Clone this repository
```
$ git clone https://github.com/jeraldconstantino/pili-balita
```
2. Create a [virtual environment](https://docs.python.org/3/library/venv.html).
```
$ python -m venv [your desired name]
$ path\to\venv\Scripts\Activate.ps1      # This will activate your environment.
```
3. Install dependencies within your environment.
```
$ pip install -r requirements.txt
```
4. Set up your [Heroku](https://www.heroku.com/) account, deploy the AI model there, and copy the generated URL. You may refer from [pili-balita-fast-API](https://github.com/jeraldconstantino/pili-balita-fast-API) repository to have an elaborated usage of Heroku platform. 
5. Paste the URL link within the [url.py](https://github.com/jeraldconstantino/pili-balita/blob/main/url.py) file.
6. Run the App.

> **NOTE:** variables and other parameters are written in Filipino language because the App is designed as part of our research during the Filipino course. Sooner, if I have a free time, I will translate it in English.

## Open for Contribution
1. Clone repository and create a new branch: 
```
$ git clone https://github.com/jeraldconstantino/pili-balita
$ git checkout https://github.com/jeraldconstantino/pili-balita -b name_for_new_branch
```
2. Make changes and test.
3. Submit [Pull Request](https://github.com/jeraldconstantino/pili-balita/pulls) with comprehensive description of changes.

### Bug Reports & Feature Requests
Kindly use the [issue tracker](https://github.com/jeraldconstantino/pili-balita/issues) to report any bugs or file feature requests.
