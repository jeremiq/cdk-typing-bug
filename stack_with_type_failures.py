from aws_cdk import aws_iam as iam
from aws_cdk import core

PRINCIPAL_ARNS=["fake_arn1", "fakearn_2"]

class MyStack(core.Stack):

    iam.PolicyStatement(
        effect=iam.Effect.ALLOW,
        actions=["some_action"],
        principals=[iam.ServicePrincipal("sns.amazonaws.com")],
        resources=["my_resource"]
        )
    
    iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["some_action"],
            principals=[iam.ArnPrincipal(arn) for arn in PRINCIPAL_ARNS],
            resources=["my_resource"],
        )


    
