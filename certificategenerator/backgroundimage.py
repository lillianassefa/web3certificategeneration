from openai import OpenAI
import requests
import os
import cv2
from dotenv import load_dotenv
from datetime import datetime as dt


load_dotenv()

def generate_background(api_key, prompt):

    client = OpenAI(api_key=api_key)

    
    response = client.images.generate(prompt=prompt)

    print("Background image generated")
    image_url = response.data[0].url

   
    local_path = os.path.join(os.getcwd(), 'certificate_background.jpg')
    with open(local_path, 'wb') as file:
        file.write(requests.get(image_url).content)
    
    return local_path

def edit_image(background_path, full_name, date, company_logo_path):
   
    certificate_background = cv2.imread(background_path)

    
    height, width, _ = certificate_background.shape
    center_x, center_y = width // 2, height // 2

    
    font_scale = 1
    font_thickness = 2
    font_color = (0, 0, 0)  

    (text_width, text_height), baseline = cv2.getTextSize(full_name, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)
    
   
    text_x = center_x - (text_width // 2)
    text_y = center_y + (text_height // 2)

   
    cv2.putText(certificate_background, full_name, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, font_thickness, cv2.LINE_AA)
    print("Name is added")

   
    (text_width, text_height), baseline = cv2.getTextSize(date, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)

  
    text_x = center_x - (text_width // 2)
    text_y = center_y + text_height + (text_height // 2)

    cv2.putText(certificate_background, date, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, font_thickness, cv2.LINE_AA)
    print("Date is added")

    
    logo_img = cv2.imread(company_logo_path)
    certificate_background[10:10 + logo_img.shape[0], 400:400 + logo_img.shape[1]] = logo_img
    print("Logo is added")

    
    cv2.imshow('Personalized Certificate', certificate_background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

 
    output_path = os.path.join(os.getcwd(), 'personalized_certificate.jpg')
    cv2.imwrite(output_path, certificate_background)

    print(f"Personalized certificate saved at: {output_path}")

if __name__ == "__main__":
   
    full_name = input("Enter your full name: ")
    date = dt.now().strftime('%m/%d/%y')
    company_logo_path ="tenacademylogo.png"
  
    open_ai_key = os.getenv("OPENAI_API_KEY")

  
    background_prompt = "Generate an image with a white background. Color the lower half of the image with very light red. Make it rectangular."

 
    background_path = generate_background(api_key=open_ai_key, prompt=background_prompt)
    edit_image(background_path, full_name, date, company_logo_path)
