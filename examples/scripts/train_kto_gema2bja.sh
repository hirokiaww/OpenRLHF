set -x

read -r -d '' training_commands <<EOF
openrlhf.cli.train_kto \
   --save_path ./checkpoint/llama3-8b-kto \
   --save_steps -1 \
   --logging_steps 1 \
   --eval_steps -1 \
   --train_batch_size 2 \
   --micro_train_batch_size 1 \
   --pretrain google/gemma-2-2b-jpn-it \
   --bf16 \
   --max_epochs 1 \
   --max_len 8192 \
   --zero_stage 3 \
   --learning_rate 5e-7 \
   --dataset  data/dataset/dialogue/output.json\
   --input_key interviewer \
   --output_key imma \
   --label_key label \

   --beta 0.1 \
   --max_samples 1024 \
   --gradient_checkpointing\
   --use_wandb c9bfebc2655cdc940e99595484b75be4382469b0
EOF
#    --flash_attn \

if [[ ${1} != "slurm" ]]; then
    deepspeed --module $training_commands
fi
