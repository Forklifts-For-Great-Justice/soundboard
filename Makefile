.PHONY: test build run stop rm clean push

# Define the name of the Docker image
IMAGE_NAME := "forklift-soundbot"

# Define the Dockerfile
DOCKERFILE := Dockerfile

# Build the Docker image 🐳
build:
	@docker build --no-cache -t $(IMAGE_NAME) .
	@echo "✅ Docker image built successfully!"

# Run the Docker container 🏃‍♂️
run:
	@docker run -it $(IMAGE_NAME)
	@echo "🚀 Container started!"

# Stop the running container 🛑
stop:
	@docker stop $(CONTAINER_ID)
	@echo "🛑 Container stopped!"

# Remove the stopped container 🗑️
rm:
	@docker rm $(CONTAINER_ID)
	@echo "🗑️ Container removed!"

# Clean up all dangling images and containers 🧹
clean:
	@docker system prune -f
	@echo "🧹 System pruned!"

# Push the image to a Docker registry 🚢
push:
	@docker push $(IMAGE_NAME)
	@echo "🚢 Image pushed successfully!"

test:
	@echo "running pytest"
	@pipenv run python3 -m pytest
