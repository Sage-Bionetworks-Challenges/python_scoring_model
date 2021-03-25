"""Sample validation script."""

import argparse
import json


def get_args():
    """Suggested command-line arguments.

    You may add additional ones if they are needed.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--entity_type", required=True,
                        help="Downloaded Synapse entity type")
    parser.add_argument("-s", "--submission_file",
                        help="Submission file")
    parser.add_argument("-r", "--results", required=True,
                        help="Validations output file")

    return parser.parse_args()


def main():
    """Main function."""
    args = get_args()

    invalid_reasons = []
    if args.submission_file is None:
        invalid_reasons.append(
            f"Expected FileEntity type but found {args.entity_type}"
        )

    else:
        with open(args.submission_file, "r") as sub_file:

            ## Sample validation test ##
            message = sub_file.read()
            if not message.startswith("test"):
                invalid_reasons.append("Submission must have test column")

    prediction_file_status = "INVALID" if invalid_reasons else "VALIDATED"

    result = {'submission_errors': "\n".join(invalid_reasons),
              'submission_status': prediction_file_status}
    with open(args.results, "w") as o:
        o.write(json.dumps(result))


if __name__ == "__main__":
    main()
