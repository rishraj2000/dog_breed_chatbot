![Alt text for the image](video/image.png "streamlite ui")

## Demo Video
[Watch the video](https://github.com/rishraj2000/dog_breed_chatbot/raw/main/video/dog_breed_1_0.mp4)

## Approach
I have used 'create_csv_agent' from langchain and an LLM from using groq. Kindly refer to the above video to check the performance.
I also tried other Agentic AI methods using crewai and can discuss about its results later.





## Instruction to run
- build your Docker image:
```bash
docker build -t dog-breed-assistant .
```

- Run the container:
 ```bash
docker run -p 8000:8000 dog-breed-assistant
```
