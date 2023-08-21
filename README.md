# CIKM_2022

## Requirements
* Python version : Python 3.9.5
* Package information : requirements.txt

## Train victim models
```
   example: 'python train_victim_model.py --save_loc --baseline --synthesizer --dataset_name --gpu_num --dp --dp_type --noise_multiplier --max_grad_norm'
```
Input: \\

save_loc: directory to save trained model \\
baseline: boolean to identify baseline model \\
synthesizer: name of victim model ['ctgan', 'tvae', 'identity', 'tablegan', 'octgan'] \\
datasest_name: dataset name \\
gpu_num: GPU number to use \\
dp: boolean for training victim model with differential privacy \\
dp_type: type of differential privacy algorithm ['sgd', 'gan'] \\
noise_multiplier: noise multiplier for differential privacy \\
max_grad_norm: maximum gradient norm for dirrential privacy \\

Output: \\
Model parameters (pth format) saved on save_loc \\

## Test victim models' generation performance
```
   example: 'python train_victim_model.py --data --synthesizer --k --test_iter --baseline --dp --dp_type
```
Input: \\
data: dataset name \\
synthesizer: name of victim model ['ctgan', 'tvae', 'identity', 'tablegan', 'octgan'] \\
k: number of samples to synthesize \\
test_iter: number of test iterations \\
baseline: boolean to identify baseline model \\
dp: boolean for training victim model with differential privacy \\
dp_type: type of differential privacy algorithm ['sgd', 'gan'] \\

Output (example):\\
```
-----------------------------------------
Test scores for ctgan on alphabank
35.5
-----------------------------------------
```


## Simulate a membership inference on victim model

```
   example : 'python main.py --gpu_num 0 --attack wb --data alphabank --target ctgan --query_size 2000 --initialize_type random --lambda3 0.001 --batch_size 2 --maxfunc 1 --lbfgs_lr 0.0001 --K --dp --dp_type'
```
Input: \\
gpu_num: GPU number to use \\

attack: type of attack ['fbb', 'wb'] \\
data: dataset name\\
target: targeted victim model ['ctgan', 'identity', 'tvae', 'tablegan', 'octgan'] \\
query_size: number of query for attack\\

initialize_type: initialization type of a white-box attack \\ 
lambda3: lambda for L2-norm regularization for a white-box attack \\
batch_size: batch size for querying for a white-box attack \\
maxfunc: maximum number of function optimization for a white-box attack \\
lbfgs_lr: learning rate of LBFGS algorithm for a white-box attack \\

K: number of generated samples collected for a black-box attack \\

dp: boolean for training victim model with differential privacy \\
dp_type: type of differential privacy algorithm ['sgd', 'gan'] \\

Output (example): \\
```
---- White-box attack result on ctgan for alphabank ----
- Args:: lambda3: 0.001; query_size: 2000; batch_size: 2; initialize_type: random; maxfunc: 1; lbfgs_lr: 0.0001
- WB AUC: 0.60
- WB AP: 0.67
------------------------------------------
```
   
