FROM lmsysorg/sglang:latest

# Expose the port that the server will use
EXPOSE 30000

# Set the default command for running the server.
CMD ["python3", "-m", "sglang.launch_server", "--model-path", "Qwen/Qwen2.5-VL-7B-Instruct", "--host", "0.0.0.0", "--port", "30000"]
