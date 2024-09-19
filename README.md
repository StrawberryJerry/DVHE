

Official resources of "DVHE: Dual-View Hyper-Relational Knowledge Graph Embedding for Link Prediction and Entity Typing".
Overview

An example of DV-KG structure:

Overall DVHE model:
Requirements

This project should work fine with the following environments:

    Python 3.7.11 for training & evaluation with:
        Pytorch 1.8.1+cu101
        numpy 1.20.3
    GPU with CUDA 10.1

All the experiments are conducted on a single 11G GeForce GTX 1080Ti GPU.
How to Run
Unzip datasets

bash

unzip -o -d dataset/ dataset/JW44K-6K.zip

unzip -o -d dataset/ dataset/HTDM.zip

Training & Evaluation

To train and evaluate the DVHE model for tasks of link prediction and entity typing on JW44K-6K dataset, please run:

bash

python run.py

To train and evaluate the DVHE model for tasks of medicine prediction and medicine class prediction on HTDM dataset, please run:

bash

python run_med.py

