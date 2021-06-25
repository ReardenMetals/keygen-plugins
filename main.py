from plugins.bnb_crypto_coin_service import BnbCoinService


def main():
    print("Hello world")
    service = BnbCoinService()
    coin = service.generate()
    print(coin)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# Needed dependenices: XMR, WAVES, USDT, EOS, BSV, ADA