from transformers import AutoModelForCausalLM, AutoTokenizer
import transformers
import torch
import sys

if __name__ == "__main__":
    model_name = "microsoft/Phi-3.5-mini-instruct"
    try:
        device = torch.device(
            "cuda:0" if torch.cuda.is_available()
            else ("mps" if torch.backends.mps.is_available() else "cpu")
        )
        cache_dir = "./models"
        model = AutoModelForCausalLM.from_pretrained(model_name, device_map=device, cache_dir=cache_dir)
        tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
        print(f"Model {model_name} loaded successfully on {device}")
    except Exception as e:
        print(f"Error loading model {model_name}: {e}")
        sys.exit()