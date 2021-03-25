# Scoring Model in Python
This repository will serve as a template for a scoring model written in Python.  Base scripts include one script for validation and another for scoring, as well as a Dockerfile.

If additional validation and/or scoring scripts are needed, e.g. each sub-challenge requires a different scoring script, they must be `COPY`'d over in the Dockerfile (so don't forget to update!).

## Steps
1. update validate.py. A basic template and an example validation test is provided in the script as reference.

2. update score.py. A basic template and an example scoring algorithm is provided in the script as reference.

3. if necessary, update Dockerfile.

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