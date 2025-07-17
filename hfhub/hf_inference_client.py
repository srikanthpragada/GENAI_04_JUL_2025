from huggingface_hub import InferenceClient
import keys 
model_id = "mistralai/Mistral-7B-Instruct-v0.2"
client = InferenceClient(model=model_id, provider="featherless-ai",
                         token=keys.HUGGINGFACE_KEY)

response = client.text_generation("What is the capital of France?")
print(response)
