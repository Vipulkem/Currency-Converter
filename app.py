import streamlit as st
import requests

st.title("Live Currency Exchange Rate Checker")
st.subheader("Check the latest exchange rates between two currencies.")

# Currency → ISO country code (2-letters, lowercase)
country_codes = {
    "INR": "in",
    "EUR": "eu",
    "GBP": "gb",
    "JPY": "jp",
    "AUD": "au",
    "CAD": "ca",
    "CHF": "ch",
    "CNY": "cn",
    "NZD": "nz",
    "SEK": "se",
    "MXN": "mx",
    "SGD": "sg",
    "HKD": "hk",
    "NOK": "no",
    "KRW": "kr",
    "TRY": "tr",
    "RUB": "ru",
    "BRL": "br",
    "ZAR": "za"
}

amount = st.number_input("Enter amount in USD :", min_value=1.00)



# Convert dropdown to show flags + currency code
def format_currency(cur):
    flag_url = f"https://flagcdn.com/24x18/{country_codes[cur]}.png"
    return f"{cur}"


convert_currency = col2.selectbox(
    "Convert Currency to:",
    list(country_codes.keys()),
    format_func=format_currency
)

# Display flag next to dropdown
flag_display_url = f"https://flagcdn.com/48x36/{country_codes[convert_currency]}.png"
st.image(flag_display_url, width=48)

if st.button("Get Exchange Rate"):
    url = "https://v6.exchangerate-api.com/v6/a48ca9092f5bb8045c444968/latest/USD"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['result'] == 'success':
            exchange_rate = data['conversion_rates'][convert_currency]
            converted_amount = amount * exchange_rate

            st.image(flag_display_url, width=48)
            st.success(
                f"{amount} USD = {converted_amount:.2f} {convert_currency} "
                f"at an exchange rate of {exchange_rate:.4f}."
            )
        else:
            st.error("Failed to retrieve exchange rates. Please try again later.")
