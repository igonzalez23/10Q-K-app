import requests

class SecEdgar:
    def __init__(self):
        self.company_name_to_cik = {}
        self.ticker_to_cik = {}
        self.retrieve_data()
    
    def retrieve_data(self):
        edgar_url = 'https://www.sec.gov/files/company_tickers.json'
        headers = {'user-agent': 'MLT isabelgonzalez1023@gmail.com'}

        r = requests.get(edgar_url, headers=headers)
        
        if r.status_code == 200:
            data = r.json()
            for company_info in data.values():
                cik = company_info['cik_str']
                name = company_info['title']
                ticker = company_info['ticker']

                self.company_name_to_cik[name] = (cik, name, ticker)
                self.ticker_to_cik[ticker] = (cik, name, ticker)
        else:
            raise Exception(f"Failed to retreive data: {r.status_code}")
        
    def name_to_cik(self, company_name):
        return self.company_name_to_cik.get(company_name)
    
    def ticker_to_cik(self, ticker):
        return self.ticker_to_cik.get(ticker)

if __name__ == "__main__":
    edgar_data = SecEdgar()

    print("Company ticker to CIK Dic")
    for name, info, in edgar_data.ticker_to_cik.items():
        print(f"{name}: {info}")
    print("Company name to CIK Dic")
    for name, info, in edgar_data.company_name_to_cik.items():
        print(f"{name}: {info}")