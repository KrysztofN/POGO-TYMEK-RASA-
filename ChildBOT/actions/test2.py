# import requests
#
# def check_bot(token):
#     url = f"https://api.telegram.org/bot{token}/getMe"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         if data['ok']:
#             print("Bot jest dostępny. Oto informacje o bocie:")
#             print("ID:", data['result']['id'])
#             print("Nazwa użytkownika:", data['result']['username'])
#             print("Imię:", data['result']['first_name'])
#         else:
#             print("Wystąpił błąd podczas sprawdzania bota:", data['description'])
#     else:
#         print("Nie można połączyć się z API Telegrama. Sprawdź swój token i upewnij się, że masz połączenie internetowe.")
#
# # Wstaw swój token bota
# token = "your-token"
# check_bot(token)
