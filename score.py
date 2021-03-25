"""Sample scoring script."""

import argparse
import json


def get_args():
    """Suggested command-line arguments.

    You may add additional ones if they are needed.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--goldstandard", required=True,
                        help="Goldstandard for scoring")
    parser.add_argument("-s", "--submission_file", required=True,
                        help="Submission file")
    parser.add_argument("-r", "--results", required=True,
                        help="Scores output file")

    return parser.parse_args()


def main():
    """Main function."""
    args = get_args()

    with open(args.submission_file, "r") as sub_file, \
            open(args.goldstandard, "r") as gold_file:
        pred = sub_file.read()
        gold = gold_file.read()

        ## Sample scoring ##
        score1 = 0.8
        score2 = 0.2
        prediction_file_status = "SCORED"

    # secondary_metric and secondary_metric_value are optional
    result = {'primary_metric': "auc",
              'primary_metric_value': score1,
              'secondary_metric': "aupr",
              'secondary_metric_value': score2,
              'submission_status': prediction_file_status}
    with open(args.results, "w") as o:
        o.write(json.dumps(result))


if __name__ == "__main__":
    main()
