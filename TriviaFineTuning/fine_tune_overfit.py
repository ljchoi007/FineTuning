'''
Tutorial: https://huggingface.co/docs/transformers/en/training

'''

from transformers import AutoTokenizer, DataCollatorForLanguageModeling, AutoModelForCausalLM
from trl import SFTConfig
import matplotlib.pyplot as plt
import torch
import subprocess
import huggingface_hub

huggingface_hub.login()

model_name = "google/gemma-3-270m-it"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained("google/gemma-3-270m-it", device_map="auto")

learning_rate = 5e-5

def tokenize(batch):
  return tokenizer(
    batch["answers"],
    truncation=True,
    max_length=512,
  )

