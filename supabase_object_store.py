from supabase import create_client, Client

SUPABASE_URL = "https://hnoiefvdhkdykhlvmigp.supabase.co" # Replace with your Supabase URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhub2llZnZkaGtkeWtobHZtaWdwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2OTA3MTcwMywiZXhwIjoyMDg0NjQ3NzAzfQ.qNtkB3f6l4oIZOE45lvP2goKIv2OJwWj0mylXRvafAs" # Replace with your Supabase API key

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

bucket_name = "image1" # Name of the bucket to be created
image_path = "PES1UG23CS689.png"  # Replace with the local image path
image_name = "PES1UG23CS689.png"  # Desired name for the uploaded file

# Step 1: Create a storage bucket
# try:
#     response = supabase.storage().create_bucket(bucket_name, public=True)
#     print(f"Bucket '{bucket_name}' created successfully.")
# except Exception as e:
#     print(f"Bucket creation error: {e}")

#     print(f"Bucket '{bucket_name}' created successfully.")
# except Exception as e:
#     print(f"Bucket creation error: {e}")

# Step 2: Upload an image to the bucket
# try:
#     with open(image_path, "rb") as f:
#         response = supabase.storage.from_(bucket_name).upload(
#             image_name,
#             f
#         )
#         print("Image uploaded successfully.")
# except Exception as e:
#     print(f"Image upload error: {e}")


# # Step 3: Get the public URL of the image
try:
    public_url =  supabase.storage.from_(bucket_name).get_public_url(
  image_path
)
    print(f"Public URL of the image: {public_url}")
except Exception as e:
    print(f"Error getting public URL: {e}")
