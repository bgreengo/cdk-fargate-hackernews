import json
import os
import pytest

from aws_cdk import core
from aws_sac_meetup.aws_sac_meetup_stack import AwsSacMeetupStack

def get_template():
    app = core.App()
    AwsSacMeetupStack(app, "aws-sac-meetup", env=core.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"], 
        region=os.environ["CDK_DEFAULT_REGION"]))
    return json.dumps(app.synth().get_stack("aws-sac-meetup").template)

def test_ecs_service():
    assert("Memory" and "512" in get_template())