import * as cdk from '@aws-cdk/core';
import * as lambda from "@aws-cdk/aws-lambda";
import { PythonFunction } from "@aws-cdk/aws-lambda-python";
import * as apigw from '@aws-cdk/aws-apigateway';
import * as path from 'path';

export class CdkCriptoAppBackStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // const vpc = new ec2.Vpc(this, "Vpc2", {
    //   maxAzs: 2,
    // });

    // const fs = new efs.FileSystem(this, "FIleSystem2", {
    //   vpc,
    //   removalPolicy: cdk.RemovalPolicy.DESTROY,
    // });

    // const accessPoint = fs.addAccessPoint("AccessPoint2", {
    //   createAcl: {
    //     ownerGid: "1001",
    //     ownerUid: "1001",
    //     permissions: "750"
    //   },
    //   posixUser: {
    //     gid: "1001",
    //     uid: "1001"
    //   }
    // })

    const lambdaFunction = new PythonFunction(this, 'MyFunction3', {
      timeout: cdk.Duration.seconds(30),
      functionName: "MainFunction3",
      entry: path.join(__dirname, "./../src"), // required
      index: "index.py",
      handler: 'handler', // optional, defaults to 'handler'
      runtime: lambda.Runtime.PYTHON_3_8, // optional, defaults to lambda.Runtime.PYTHON_3_7
      // vpc,
      // filesystem: lambda.FileSystem.fromEfsAccessPoint(accessPoint, "/mnt/efs"),
      memorySize: 128,
      // vpc,
      // filesystem: lambda.FileSystem.fromEfsAccessPoint(accessPoint, "/mnt/efs"),
    });

    const api = new apigw.LambdaRestApi(this, 'Gateway3', {
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
