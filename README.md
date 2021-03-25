# Scoring Model in Python
This repository will serve as a template for a scoring model written in Python.  Base scripts include one script for validation and another for scoring, as well as a Dockerfile.

If additional input files are needed, they must be `COPY`'d over so that they're available during the container run (so don't forget to update the Dockerfile!).

## Steps
1. update the validation functions within [validate.py] (e.g. `validate_sc1()`). The script is already written so that these functions are wrapped to the corresponding sub-challenge question.  Create and edit additional validation functions as needed.

2. update the scoring functions within [score.py] (e.g. `score_sc1()`). Similar to validate.py, the script is already written so that these functions are wrapped to the corresponding sub-challenge question.  Create and edit additional scoring functions as needed.

3. if necessary, update [Dockerfile].

4. build a Docker image with the following command:

```bash
docker build -t docker.synapse.org/PROJECT_ID/MODEL_NAME:VERSION .
```

where:
* `PROJECT_ID` is the Synapse ID of a Project (most likely the Challenge staging site)
* `MODEL_NAME` is some arbitrary name you want to give the image
* `VERSION` is the version tag for the image
* `.` is the filepath to the Dockerfile, in this case, the current working directory (`.`)

For example:

```bash
docker build -t docker.synapse.org/syn123/scoring:v1 .
```

will create an image named `scoring` (whose current version is `v1`).  The image will be pushed to the Synapse Project with the Synapse ID, `syn123`.

5. push the Docker image up to Synapse with the following command:

```bash
docker push docker.synapse.org/PROJECT_ID/MODEL_NAME:VERSION
```

#### Note:
Pushing to the Synapse DockerHub will require a login. If the above command does not work, try logging in first with:

```bash
docker login docker.synapse.org
```

then follow the prompts.

If you still encounter errors, you may need to become a Synapse Certified User first.  See [here](https://www.synapse.org/#!Quiz:Certification) for more details.