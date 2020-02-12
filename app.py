#!/usr/bin/env python3

from aws_cdk import core

from aws_sac_meetup.aws_sac_meetup_stack import AwsSacMeetupStack


app = core.App()
AwsSacMeetupStack(app, "aws-sac-meetup")

app.synth()
