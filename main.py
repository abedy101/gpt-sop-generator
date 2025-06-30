import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

prompt = """
Convert the following meeting notes into a formal SOP:
- ID must be submitted within 24 hours
- Accounts setup takes 2 days
- Assign buddy for 1st week
"""

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant that writes formal SOPs."},
    {"role": "user", "content": prompt}
  ]
)

print(response['choices'][0]['message']['content'])
