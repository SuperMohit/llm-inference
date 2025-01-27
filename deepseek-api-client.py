import openai

# Replace with your actual URL and token
base_url = "https://op1ctdhgjd004p-8080.proxy.runpod.net/v1/"
api_key = "vllm-mohit-api-key"

openai.base_url = base_url
openai.api_key = api_key

response = openai.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Who is expert in AI/ML."},
        {"role": "user", "content": "Explain how Flash Attention is used in Deepseek"},
        {"role": "user", "content": "Explain MoE in Deepseek"},
        {"role": "user", "content": "Explain how Deepseek was able to optimize cost?"},
    ],
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
)

print(response.choices[0].message.content)
