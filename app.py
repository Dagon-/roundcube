#!/usr/bin/env python3

from aws_cdk import core

from roundcube.roundcube_stack import RoundcubeStack

env_eu = core.Environment(account="585823398980", region="eu-west-1")
app = core.App()
RoundcubeStack(app, "roundcube", env=env_eu)

core.Tag.add(app, "resource-group", "roundcube",
  exclude_resource_types = ["AWS::ResourceGroups::Group"] # Tagging the resource group fails
)

app.synth()