from pactus import PactusConnect
from pactus.apis import Network


def main() -> None:
    connection = PactusConnect(
        "testnet4.pactus.org:50052",
    ).connect()

    response = Network.get_node_info(connection)

    print(response)


if __name__ == "__main__":
    main()
