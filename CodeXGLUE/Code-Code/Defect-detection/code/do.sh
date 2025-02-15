python run.py \
    --output_dir=./saved_models \
    --model_type=roberta \
    --tokenizer_name=neulab/codebert-java \
    --model_name_or_path=neulab/codebert-java \
    --do_train \
    --train_data_file=../dataset/train.jsonl \
    --eval_data_file=../dataset/valid.jsonl \
    --test_data_file=../dataset/test.jsonl \
    --epoch 10 \
    --block_size 400 \
    --train_batch_size 30 \
    --eval_batch_size 30 \
    --learning_rate 2e-5 \
    --max_grad_norm 1.0 \
    --evaluate_during_training \
    --seed 123456  2>&1 | tee train.log
