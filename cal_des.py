'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-04-22 22:50:56
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-04-22 22:50:56
FilePath: /PyNEP/examples/cal_des.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from pynep.io import load_nep
from pynep.calculate import NEP
import os

# export PYTHONPATH=/data/home/wuxingxing/codespace/GPUMD_python/PyNEP:$PYTHONPATH

nep_path = "/data/home/wuxingxing/datas/pwmat_mlff_workdir/hfo2/nep_gpumd_1image/nep.txt"
# train_path = "/data/home/wuxingxing/datas/pwmat_mlff_workdir/hfo2/nep_gpumd_1image/train.xyz"
train_path = "/data/home/wuxingxing/datas/PWMLFF_library_data/HfO2/hfo2_dpgen/HfO2_liutheory/mvms/train.xyz"
# train_in_path = os.path.join(os.path.dirname(train_path), "train.in")
#covert xyz to in file

train_data = load_nep(train_path, ftype="exyz")
# dump_nep(train_in_path, train_data, ftype="nep")

# train_data = load_nep(train_in_path)
calc = NEP(nep_path)

# def split_dataset(dataset, ratio=0.1):
#     indices = np.arange(len(dataset))
#     np.random.shuffle(indices)
#     num = int(len(dataset) * ratio)
#     return dataset[:num], dataset[num:]
# d1, d2 = split_dataset(test_data)
i = 0
for atoms in train_data:
    # nep_forces = calc.get_forces(atoms)
    des = calc.get_property('descriptor', atoms)
    des = calc.get_property('neigh', atoms)
    if i == 0:
        raise Exception("out!")
    # lat = calc.get_property('latent', atoms)
    print("=============image {}=============".format(i))
    # print(type(des))
    # print(des.shape)
    # print(des)
    print("=================")
    # print(type(lat))
    # print(lat.shape)
    # print("=================")