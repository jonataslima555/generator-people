import requests
import json

api_key = "14926|KDP5OCOlIOCEnbr0a3f3POkCmH8E82lx"

def generate_person(location, fields):
  url = "https://api.invertexto.com/v1/faker"
  headers = {"Authorization": f"Bearer {api_key}"}
  params = {"localizacao": location, "campos": fields}
  response = requests.get(url, headers=headers, params=params)
  data = json.loads(response.text)
  
  # Extract only requested fields and format the output
  formatted_data = {
      "Name:": data["name"],
      "CPF:": data["cpf"],
      "Email:": data["email"],
      "Phone Number:": data["phone_number"],
  }
  return formatted_data

# Get data for a person in Brazil with desired fields
data_person = generate_person("pt_BR", "name,cpf,email,phone_number")

# Print the formatted data
for key, value in data_person.items():
  print(f"{key} {value}")
