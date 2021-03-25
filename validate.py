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
    parser.add_argument("-s", "--submission",
                        help="Submission file")
    parser.add_argument("-r", "--results", required=True,
                        help="Validations output file")
    parser.add_argument("-q", "--question", required=True,
                        type=int, help="Question number")
    return parser.parse_args()


def validate_sc1(pred):
    """Validation function for sub-challenge 1.

    TODO:
        Edit this function for your validation purposes.
    """
    errors = []
    if not pred.startswith("test"):
        errors.append("Submission must have a `test` column")
    if not pred.endswith("value"):
        errors.append("Submission must have a `value` column")
    return errors


def validate_sc2(pred):
    """Validation function for sub-challenge 2.

    TODO:
        Edit this function for your validation purposes.
    """
    errors = []
    if not pred.startswith("test"):
        errors.append("Submission must have a `test` column")
    if not pred.endswith("value"):
        errors.append("Submission must have a `value` column")
    return errors


def main():
    """Main function."""
    args = get_args()

    invalid_reasons = []
    if args.submission_file is None:
        invalid_reasons.append(
            f"Expected FileEntity type but found {args.entity_type}"
        )

    else:
        # This will map the sub-challenge to its respective validation
        # tests. Feel free to remove this mapping if all sub-challenges
        # are using the same predictions file.
        validation_func_mapping = {1: validate_sc1,
                                   2: validate_sc2}

        with open(args.submission, "r") as sub_file:
            pred = sub_file.read()
            errors_found = validation_func_mapping[args.questions](pred)
            invalid_reasons.extend(errors_found)

    prediction_file_status = "INVALID" if invalid_reasons else "VALIDATED"

    result = {'submission_errors': "\n".join(invalid_reasons),
              'submission_status': prediction_file_status}
    with open(args.results, "w") as o:
        o.write(json.dumps(result))


if __name__ == "__main__":
    main()
