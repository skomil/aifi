# AIFI

AIFI is a no-code Generative AI workflow tool designed to simplify the process of building, training, and deploying AI models. With an intuitive user interface and seamless integration with various AI frameworks and platforms, AIFI enables users to focus on their AI use cases and create complex workflows for stable diffusion without worrying about complex code and configurations.

## Features

- Drag-and-drop interface for designing complex workflows for stable diffusion
- Integration with popular AI frameworks and platforms
- Support for data preprocessing and feature engineering
- Model training and evaluation with customizable configurations
- Model deployment and monitoring
- Collaboration and version control for AI projects

## Getting Started

Follow these steps to set up the AIFI project on your local machine:

### Prerequisites

- Python 3.7 or higher
- Node.js 14 or higher
- NPM 6 or higher

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/aifi.git
cd aifi
```

2. Set up the Python backend:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

3. Set up the UI:

```bash
cd ui
npm install
```

### Running the project

1. Start the backend server:

```bash
cd backend
python -m aifi.server
```

2. Start the UI development server:

```
cd ui
npm start
```

The UI should now be running at http://localhost:3000, and the backend should be listening on http://localhost:5000.

### Updating the API Schema

AIFI uses the OpenAPI 3 schema to define the API contract between the backend and the UI. To update the API schema, follow these steps:

1. Open the `api.yaml` (or `api.json`) file in your project's root directory.
2. Update the schema according to the OpenAPI Specification.
3. Regenerate the TypeScript classes for the UI:

```bash
openapi-generator-cli generate -i api.yaml -g typescript-axios -o ui/src/api
```

4. Regenerate the Python API interface:

```bash
openapi-generator-cli generate -i api.yaml -g python-flask -o backend --package-name aifi.api
```

Please note the paths /ui/src/api and backend/aifi/api are generated code and should not be edited

5. in the backend generated openapi.yaml, replace all instances of `aifi.api.controllers.default_controller` with the actual implementation, `aifi.server.controller` and modify the method signatures in that module if needed. 

6. Update your backend implementation and UI components to reflect the changes in the API schema.

###

To view the API:
```
http://localhost:8080/ui/
```

Your OpenAPI definition lives here:

```
http://localhost:8080/openapi.json
```
## Contributing

If you're interested in contributing to AIFI, please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to get started.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
