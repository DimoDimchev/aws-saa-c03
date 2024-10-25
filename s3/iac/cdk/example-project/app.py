#!/usr/bin/env python3

import aws_cdk as cdk

from example_project.example_project_stack import ExampleProjectStack


app = cdk.App()
ExampleProjectStack(app, "ExampleProjectStack")

app.synth()
