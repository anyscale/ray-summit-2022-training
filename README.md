# Welcome to Ray Summit 2022 Training 

© 2019-2022, Anyscale. All Rights Reserved'

<img src="images/ray-summit-2022.png" width="80%" height="50%">

Welcome to the Ray Summit 2022 training tutorials on Ray, the system for scaling your 
Python and AI/ML applications from a laptop to a cluster.

## Outline for the all the tutorial Lessons 📖

| Class| Ray Components and Library | Description
|:-----|:-----------|:----------------------------------------------------------|
| 1  | [Ray Core](ray-core/README.md)   |Introduction to Ray for Distributed Applications|
| 2  | [Ray Serve](ray-serve/README.md) |Machine Learning Model Deployment and Serving with Ray Serve|
| 3  | [Ray RLlib](ray-rllib/README.md) |Introduction to Reinforcement Learning and RLlib |

**IMPORTANT NOTE**: Modules and materials in these tutorials have been tested with 
Ray release `x.y` and supported Python `3.7+`.


## 👩 Set up instructions for Anyscale 

There is nothing you need to setup, as the Anyscale hosted environment will provide everything.

However, consider cloning or downloading a release of the tutorial notebooks and 
supporting software from the [Ray Summit training repo](https://github.com/anyscale/ray-summit-2022-training), 
so you have a local copy of everything.


## 👩 Setup instructions for local laptop 💻
This is *optional* if you want to install training material on your laptop at home,
after training is over.

### Using conda
If you need to install Anaconda, follow the instructions [here](https://www.anaconda.com/products/distribution).
If you already have Anaconda installed, consider running conda `upgrade --all.`

1. `conda create -n ray-summit-training python=3.8`
2. `conda activate ray-summit-training`
3. `git clone git@github.com:anyscale/ray-summit-2022-training.git`
4. `cd to <cloned_dir>`
5. `python3 -m pip install -r requirements.txt`
6. `python3 -m ipykernel install`
7. `jupyter lab`

If you are using Apple M1 laptop 🍎 follow the following instructions:

1. `conda create -n ray-core-tutorial-testing python=3.8`
2. `conda activate ray-summit-training`
3. `conda install grpcio`
4. `python3 -m pip install -r requirements.txt`
5. `python3 -m ipykernel install`
6. `conda install jupyterlab`
7. `jupyter lab`

### Using only pip
1. git clone git@github.com:anyscale/ray-summit-2022-training.git`
2. `cd to <cloned_dir>`
3. `python3 -m pip install -r requirements.txt`
4. `python3 -m ipykernel install`
5. `jupyter lab`

Let's have 😜 fun @ Ray Summit 2022!

Thank you 🙏










