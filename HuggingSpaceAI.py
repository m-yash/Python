from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import gradio as gr

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

def text_generation(input_text, seed):
  input_ids = tokenizer(input_text, return_tensors="pt").input_ids
  torch.manual_seed(seed) 
  outputs = model.generate(input_ids, do_sample=True, max_length=60, top_k=50, temperature=0.7, top_p=0.9)
  generated_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)
  return generated_text

title = "Kirua"

gr.Interface(
    text_generation,
    [gr.Textbox(lines=2, label="input"), gr.Number(label="seed")],
    [gr.Textbox(label="output")],
    title=title,
).launch()
