import argparse
from src.pipeline import Pipeline


def main():
    parser = argparse.ArgumentParser(
        description="Traffic multi-object tracking pipeline"
    )
    parser.add_argument(
        "--config",
        default="configs/default.yaml",
        help="Path to config file"
    )
    args = parser.parse_args()

    pipeline = Pipeline(config_path=args.config)
    pipeline.run()


if __name__ == "__main__":
    main()