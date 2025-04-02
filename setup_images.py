import requests
import os
import shutil

def setup_logo():
    # Create static/images directory if it doesn't exist
    os.makedirs('app/static/images', exist_ok=True)
    destination = "app/static/images/logo.png"
    
    # Direct Unsplash image URL
    image_url = "https://images.unsplash.com/photo-1619736163418-0826329731fe?fm=jpg&w=1000&fit=crop"
    
    try:
        # Download the Shih Tzu image
        print("Downloading Shih Tzu logo from Unsplash...")
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(destination, 'wb') as f:
                f.write(response.content)
            print("Shih Tzu logo downloaded successfully!")
        else:
            print("Failed to download logo. Please check the URL or your internet connection.")
    except Exception as e:
        print(f"Error setting up logo: {str(e)}")
        print("Please manually add a Shih Tzu image named 'logo.png' in the app/static/images folder")

if __name__ == "__main__":
    setup_logo() 