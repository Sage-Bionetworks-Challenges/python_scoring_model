"""Sample scoring script."""

import argparse
import json


def get_args():
    """Suggested command-line arguments.

    You may add additional ones if they are needed.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--goldstandard", required=True,
                        help="Goldstandard file")
    parser.add_argument("-s", "--submission", required=True,
                        help="Submission file")
    parser.add_argument("-r", "--results", required=True,
                        help="Scores output file")
    parser.add_argument("-q", "--question", required=True,
                        type=int, help="Question number")
    return parser.parse_args()


def score_sc1(pred, gold):
    """Scoring function for sub-challenge 1.

    TODO:
        Edit this function for your scoring purposes.
    """
    score1 = 0.8
    score2 = 0.2
    return score1, score2


def score_sc2(pred, gold):
    """Scoring function for sub-challenge 2.

    TODO:
        Edit this function for your scoring purposes.
    """
    score1 = 0.5
    score2 = 0.3
    return score1, score2


def main():
    """Main function."""
    args = get_args()

    # This will map the sub-challenge to its respective scoring algorithms.
    scoring_func_mapping = {1: score_sc1,
                            2: score_sc2}

    with open(args.submission, "r") as sub_file, \
            open(args.goldstandard, "r") as gold_file:
        pred = sub_file.read()
        gold = gold_file.read()

        score1, score2 = scoring_func_mapping[args.question](
            pred, gold
        )
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
