# FD Crawling PoC Project
 

# Requirement
- python >= 3.7.0
- CPU >= 4Core
- Memory >= 8GB

# Installation
```bash
$ git clone https://github.com/scarleaf/Project_BRCA.git
$ cd ./~~~
$ conda create -n project_brca python=3.8
$ pip install -r requirements.txt
```

# Training Code

```bash
python train.py -h
usage: train.py [-h] [--folder FOLDER] [--data_path DATA_PATH] [--save_path SAVE_PATH] [--batch_size BATCH_SIZE] [--num_workers NUM_WORKERS] [--epochs EPOCHS] [--gpu_num GPU_NUM]
                [--model_num MODEL_NUM]

optional arguments:
  -h, --help            show this help message and exit
  --folder FOLDER       (default=0)
  --data_path DATA_PATH
                        (default=./data)
  --save_path SAVE_PATH
                        (default=./result)
  --batch_size BATCH_SIZE
                        (default=16)
  --num_workers NUM_WORKERS
                        (default=8)
  --epochs EPOCHS       (default=150)
  --gpu_num GPU_NUM     (default="0,1")
  --model_num MODEL_NUM
                        0: efficinetnet-b0, 1: efficinetnet-b1, 2: efficinetnet-b2, 3: efficinetnet-b3, 4: efficinetnet-b4, 5: efficinetnet-b5, 6: vit, 7: cait, 8: deepvit, 9: resnet50,
                        10: resnet101, 11: resnet152, 12: densenet121, 13: densenet161, 14: densenet169, 15: densenet201, 16: inception_v3 (default=0, efficinetnet-b0)

```
# Test Code
```bash
python test.py -h
usage: test.py [-h] [--folder FOLDER] [--data_path DATA_PATH] [--save_path SAVE_PATH] [--batch_size BATCH_SIZE] [--num_workers NUM_WORKERS] [--gpu_num GPU_NUM] [--model_num MODEL_NUM]
               [--model_name MODEL_NAME]

optional arguments:
  -h, --help            show this help message and exit
  --folder FOLDER       (default=0)
  --data_path DATA_PATH
                        (default=./data)
  --save_path SAVE_PATH
                        (default=./result)
  --batch_size BATCH_SIZE
                        (default=1)
  --num_workers NUM_WORKERS
                        (default=8)
  --gpu_num GPU_NUM     (default=0)
  --model_num MODEL_NUM
                        0: efficinetnet-b0, 1: efficinetnet-b1, 2: efficinetnet-b2, 3: efficinetnet-b3, 4: efficinetnet-b4, 5: efficinetnet-b5, 6: vit, 7: cait, 8: deepvit, 9: resnet50,
                        10: resnet101, 11: resnet152, 12: densenet121, 13: densenet161, 14: densenet169, 15: densenet201, (default=0, efficinetnet-b0)
  --model_name MODEL_NAME
                        (default=None)
```


# Example
## Step 1. Patch Generation
```bash
python patch_generator.multi.py --folder 0 \
                                --base_path /home/Dataset/BRCA \
                                --save_path ./data \
                                --subject_case ovary 
```

## Step 2. Training & Validation
```bash
python train.py --folder 0 \
                --data_path /path/to/patch_data/dir \
                --save_path /path/to/output/model/dir \
                --batch_size 16 \
                --epochs 100 \
                --gpu_num 0 \
                --model_num 0
```

## Step 3. Test
```bash
python test.py --folder 0 \
               --data_path ./data \
               --save_path ./result_m0_eff-b0 \
               --gpu_num 0 \
               --model_num 0
```
