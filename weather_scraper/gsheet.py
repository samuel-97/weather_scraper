import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
from func_get_weather import get_weather

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1D8YBbIKllRbcZLWmwx3qftlQinzJ7_8CZ8IzjIVqZyU"
SAMPLE_RANGE_NAME = "Sheet1!A2"


def main():
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("ignore/token.json"):
    creds = Credentials.from_authorized_user_file("ignore/token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "ignore/credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("ignore/token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    get_weather()
    weather=pd.read_csv("New_Weather.csv")
    valueData = weather.values.tolist()
    sheet = service.spreadsheets()
    result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME,
      valueInputOption="USER_ENTERED",body={"values":valueData}).execute()
    
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()