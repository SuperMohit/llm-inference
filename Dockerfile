FROM vllm/vllm-openai:latest

ENV HF_HUB_ENABLE_HF_TRANSFER=1

EXPOSE 8080

ENTRYPOINT ["python3", "-m", "vllm.entrypoints.openai.api_server", \
           "--model", "deepseek-ai/DeepSeek-R1-Distill-Llama-70B", \
           "--dtype", "bfloat16", \
           "--tensor-parallel-size","4", \
           "--max-model-len", "4096", \
           "--port", "8080", \
           "--api-key", "${VLLM_API_KEY}"]
