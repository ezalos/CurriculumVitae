import fire

from src.ComposeCV import ComposeCV


def main():
    ccv = ComposeCV()
    ccv.make()


if __name__ == "__main__":
    fire.Fire(main)
