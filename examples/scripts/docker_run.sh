set -x

PROJECT_PATH=$(cd $(dirname $0)/../../; pwd)
IMAGE_NAME="nvcr.io/nvidia/pytorch:24.07-py3"

docker run --network=host --gpus all -it --rm --shm-size="10g" --cap-add=SYS_ADMIN \
	-v $PROJECT_PATH:/openrlhf -v  $HOME/.cache:/root/.cache -v  $HOME/.bash_history2:/root/.bash_history \
	$IMAGE_NAME bash

python -m pip install --upgrade pip
cd ../openrlhf
python pip install -r requirment.txt