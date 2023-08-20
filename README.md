# CIKM_2022

## Requirements
* Python version : Python 3.9.5
* Package information : requirements.txt

## Train & test victim models
1. Train victim models 
train_victim_model.py 
test_model.py 

## Simulate a membership inference on victim model
1. Simulate a membership inference on victim model

```
   example : 'python main.py --gpu_num 0 --attack wb --data alphabank --target ctgan --query_size 2000 --initialize_type random --lambda3 0.001 --batch_size 2 --maxfunc 1 --lbfgs_lr 0.0001 --K --dp --dp_type'
```
Input:
gpu_num: GPU number to use

attack: type of attack ['fbb', 'wb']
data: dataset name
target: targeted victim model ['ctgan', 'identity', 'tvae', 'tablegan', 'octgan']
query_size: number of query for attack

initialize_type: initialization type of a white-box attack [
lambda3: lambda for L2-norm regularization for a white-box attack
batch_size: batch size for querying for a white-box attack
maxfunc: maximum number of function optimization for a white-box attack
lbfgs_lr: learning rate of LBFGS algorithm for a white-box attack

K: number of generated samples collected for a black-box attack

dp: boolean for training victim model with differential privacy
dp_type: type of differential privacy algorithm ['sgd', 'gan']

Output:
```
---- White-box attack result on ctgan for alphabank ----
- Args:: lambda3: 0.001; query_size: 2000; batch_size: 2; initialize_type: random; maxfunc: 1; lbfgs_lr: 0.0001
- WB AUC: 0.60
- WB AP: 0.67
------------------------------------------
```
   
