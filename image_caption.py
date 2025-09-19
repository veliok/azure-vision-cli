def image_caption():
    import os
    from azure.ai.vision.imageanalysis import ImageAnalysisClient
    from azure.ai.vision.imageanalysis.models import VisualFeatures
    from azure.core.credentials import AzureKeyCredential

    endpoint = input("Enter Azure Vision Endpoint: ").strip()
    key = input("Enter Azure Vision Key: ").strip()
    image_url = input("Enter Image URL to analyze: ").strip()

    client = ImageAnalysisClient(
        endpoint,
        AzureKeyCredential(key)
    )

    result = client.analyze_from_url(
        image_url,
        visual_features=[
            VisualFeatures.CAPTION,
            VisualFeatures.TAGS,
        ]
    )

    print(f" Model version: {result.model_version}")
    print("Image analysis results:")

    if result.caption is not None:
        print(" Caption:")
        print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")
    
    if result.tags is not None:
        print(" Tags:")
        for tag in result.tags.list:
            print(f"   '{tag.name}', Confidence {tag.confidence:.4f}")


if __name__ == "__main__":
    image_caption()