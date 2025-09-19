# azure-vision-cli

Small sample on how to get image caption and tags using Azure AI Vision SDK.

## Requirements
```
$ pip install azure-ai-vision-imageanalysis
```
## Example

```
$ py image_caption.py 
$ Enter Azure Vision Endpoint: "Your Endpoint"
$ Enter Azure Vision Key: "Your Key"
$ Enter Image URL to analyze: "URL"

Model version: 2023-10-01
Image analysis result:
Caption:
   'a cat'
Tags:
   'cat', Confidence 0.9310
```
