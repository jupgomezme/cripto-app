import * as cdk from '@aws-cdk/core';
import * as lambda from "@aws-cdk/aws-lambda";
import { PythonFunction } from "@aws-cdk/aws-lambda-python";
import * as apigw from '@aws-cdk/aws-apigateway';
import * as ec2 from '@aws-cdk/aws-ec2';
import * as efs from '@aws-cdk/aws-efs';
import * as path from 'path';

export class CdkCriptoAppBackendStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // const vpc = new ec2.Vpc(this, "Vpc", {
    //   maxAzs: 2,
    //   subnetConfiguration: [
    //     {
    //       name: 'public-subnet-1',
    //       subnetType: ec2.SubnetType.PUBLIC,
    //       cidrMask: 24,
    //     },
    //   ]
    // });

    // const fs = new efs.FileSystem(this, "FIleSystem", {
    //   vpc,
    //   removalPolicy: cdk.RemovalPolicy.DESTROY,
    // });

    // const accessPoint = fs.addAccessPoint("AccessPoint", {
    //   createAcl: {
    //     ownerGid: "1001",
    //     ownerUid: "1001",
    //     permissions: "750"
    //   },
    //   path: "/efs",
    //   posixUser: {
    //     gid: "1001",
    //     uid: "1001"
    //   }
    // })

    const lambdaFunction = new PythonFunction(this, 'MyFunction2', {
      timeout: cdk.Duration.seconds(900),
      functionName: "MainFunction2",
      entry: path.join(__dirname, "./../src"), // required
      index: "index.py",
      handler: 'handler', // optional, defaults to 'handler'
      runtime: lambda.Runtime.PYTHON_3_8, // optional, defaults to lambda.Runtime.PYTHON_3_7
      // vpc,
      // filesystem: lambda.FileSystem.fromEfsAccessPoint(accessPoint, "/mnt/efs"),
      memorySize: 128
    });

    const api = new apigw.LambdaRestApi(this, 'Gateway2', {
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
