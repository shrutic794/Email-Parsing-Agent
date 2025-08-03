from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import openai

# Your credentials (replace with env vars or secrets securely)


# Setup credentials for Gmail API
creds = Credentials(
    token=None,
    refresh_token=REFRESH_TOKEN,
    token_uri="https://oauth2.googleapis.com/token",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scopes=["https://www.googleapis.com/auth/gmail.readonly"]
)

# Build Gmail API service
service = build('gmail', 'v1', credentials=creds)

# Setup OpenAI key
openai.api_key = OPENAI_API_KEY

def list_gmail_labels():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    print("Gmail Labels:")
    for label in labels:
        print(f"- {label['name']}")

def openai_test():
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Say hello in a friendly way."}
        ]
    )
    print("OpenAI response:", response.choices[0].message.content.strip())

if __name__ == "__main__":
    list_gmail_labels()
    openai_test()
