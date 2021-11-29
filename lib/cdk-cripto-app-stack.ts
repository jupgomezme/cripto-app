import * as cdk from '@aws-cdk/core';
import * as lambda from "@aws-cdk/aws-lambda";
import { PythonFunction } from "@aws-cdk/aws-lambda-python";
import * as apigw from '@aws-cdk/aws-apigateway';
import * as path from 'path';

export class CdkCriptoAppStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const lambdaFunction = new PythonFunction(this, 'MyFunction', {
      functionName: "MainFunction",
      entry: path.join(__dirname, "./../src"), // required
      index: "index.py",
      handler: 'handler', // optional, defaults to 'handler'
      runtime: lambda.Runtime.PYTHON_3_8, // optional, defaults to lambda.Runtime.PYTHON_3_7
    });

    const api = new apigw.LambdaRestApi(this, 'Gateway', {
      handler: lambdaFunction,
      proxy: false,
      deployOptions: {
        stageName: 'prod',
      },
      defaultCorsPreflightOptions: {
        allowHeaders: [
          'Content-Type',
          'X-Amz-Date',
          'Authorization',
          'X-Api-Key',
        ],
        allowMethods: apigw.Cors.ALL_METHODS,
        allowCredentials: true,
        allowOrigins: apigw.Cors.ALL_ORIGINS,
      },
    });

    const basePath = api.root.addResource("main");
    basePath.addMethod("POST");


  }
}
