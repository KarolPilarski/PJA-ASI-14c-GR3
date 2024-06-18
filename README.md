# PJA-ASI-14c-GR3


Contributors

    Mateusz Laskowski s23835
    Pilarski Karol s22682
    Kawa Bartłomiej s18581
    Bławdzin Sebastian s21251

 Environment set up

    Download and install Miniconda
    Download file environment.yml from catalog env
    In terminal use command conda env create -f environment.yml
    Activate created environment using command conda activate tortilla-prices
    
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


