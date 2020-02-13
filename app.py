#!/usr/bin/env python3
import os
from aws_cdk import core

from aws_sac_meetup.aws_sac_meetup_stack import AwsSacMeetupStack


app = core.App()
AwsSacMeetupStack(app, "aws-sac-meetup", env=core.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], 
    region=os.environ["CDK_DEFAULT_REGION"]))

app.synth()
