from pactus import PactusConnect


def main() -> None:
    connection = PactusConnect(
        "testnet1.pactus.org:50052",
    ).connect(secure=True)


if __name__ == "__main__":
    main()
