import request

ZEROBOUNCE_API_KEY = ""


def verify_email(email):
    url = f"https://api.zerobounce.net/v2/validate?api_key={ZEROBOUNCE_API_KEY}&email={email}"

    try:
        response = requests.get(url)

       
        if response.headers.get('content-type') == 'application/json':
            data = response.json()
            if data["status"] == "valid":
                print(f"The email {email} is valid.")
            elif data["status"] == "invalid":
                print(f"The email {email} is invalid.")
            else:
                print(f"Unable to verify the email {email}.")
        else:
            print("Received a non-JSON response. Status code:", response.status_code)
            print("Response content:", response.content)
    except requests.exceptions.RequestException as e:
        print("Error:", e)



email_to_verify = str(input("Enter the mail"))
verify_email(email_to_verify)
