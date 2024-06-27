Contributors

    Mateusz Laskowski s23835
    Pilarski Karol s22682
    Kawa Bartłomiej s18581
    Bławdzin Sebastian s21251

Rules and guidelines
In order to get the best out of the template:

    Don't remove any lines from the .gitignore file we provide
    Make sure your results can be reproduced by following a data engineering convention
    Don't commit data to your repository
    Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in conf/local/

 Environment set up

    Download and install Miniconda
    Download file environment.yml from catalog env
    In terminal use command conda env create -f environment.yml
    Activate created environment using command conda activate tortilla-prices

 Kedro

    pip install -r requirements.txt
    kedro new --name=spaceflights
    kedro run --from-inputs aug_train
    kedro viz
    
Tortilla Price Prediction Model
The model described here will be able to predict the price of tortillas (expressed in Mexican pesos per kilogram)
based on several parameters. The model will take the following input features:

    State -> String; Values=['State1','State2',..., 'State32']
    City -> String; Values=['City1','City2',..., 'City56']
    Year -> int
    Month -> int
    Day -> int
    Store Type -> String; Values=['Type1','Type2',...,'TypeN']

Dataset and Inspiration

    https://www.kaggle.com/datasets/richave/tortilla-prices-in-mexico

Docker Setup

    1. Download Docker Desktop from the official website and install it on your system with the default settings.
    2. Launch Docker Desktop.
    3. Clone our repository with git clone https://github.com/KarolPilarski/PJA-ASI-14c-GR3.git .
    4. To run the application in a container, use the command in directory of git project 'docker-compose up'

Jupyter

    To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

    pip install jupyter

    After installing Jupyter, you can start a local notebook server:

    kedro jupyter notebook

JupyterLab

    To use JupyterLab, you need to install it:

    pip install jupyterlab

    You can also start JupyterLab:

    kedro jupyter lab



