"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CdkCriptoAppStack = void 0;
const cdk = require("@aws-cdk/core");
const lambda = require("@aws-cdk/aws-lambda");
const aws_lambda_python_1 = require("@aws-cdk/aws-lambda-python");
const apigw = require("@aws-cdk/aws-apigateway");
const path = require("path");
class CdkCriptoAppStack extends cdk.Stack {
    constructor(scope, id, props) {
        super(scope, id, props);
        const lambdaFunction = new aws_lambda_python_1.PythonFunction(this, 'MyFunction', {
            functionName: "MainFunction",
            entry: path.join(__dirname, "./../src"),
            index: "index.py",
            handler: 'handler',
            runtime: lambda.Runtime.PYTHON_3_8,
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
exports.CdkCriptoAppStack = CdkCriptoAppStack;
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiY2RrLWNyaXB0by1hcHAtc3RhY2suanMiLCJzb3VyY2VSb290IjoiIiwic291cmNlcyI6WyJjZGstY3JpcHRvLWFwcC1zdGFjay50cyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiOzs7QUFBQSxxQ0FBcUM7QUFDckMsOENBQThDO0FBQzlDLGtFQUE0RDtBQUM1RCxpREFBaUQ7QUFDakQsNkJBQTZCO0FBRTdCLE1BQWEsaUJBQWtCLFNBQVEsR0FBRyxDQUFDLEtBQUs7SUFDOUMsWUFBWSxLQUFvQixFQUFFLEVBQVUsRUFBRSxLQUFzQjtRQUNsRSxLQUFLLENBQUMsS0FBSyxFQUFFLEVBQUUsRUFBRSxLQUFLLENBQUMsQ0FBQztRQUV4QixNQUFNLGNBQWMsR0FBRyxJQUFJLGtDQUFjLENBQUMsSUFBSSxFQUFFLFlBQVksRUFBRTtZQUM1RCxZQUFZLEVBQUUsY0FBYztZQUM1QixLQUFLLEVBQUUsSUFBSSxDQUFDLElBQUksQ0FBQyxTQUFTLEVBQUUsVUFBVSxDQUFDO1lBQ3ZDLEtBQUssRUFBRSxVQUFVO1lBQ2pCLE9BQU8sRUFBRSxTQUFTO1lBQ2xCLE9BQU8sRUFBRSxNQUFNLENBQUMsT0FBTyxDQUFDLFVBQVU7U0FDbkMsQ0FBQyxDQUFDO1FBRUgsTUFBTSxHQUFHLEdBQUcsSUFBSSxLQUFLLENBQUMsYUFBYSxDQUFDLElBQUksRUFBRSxTQUFTLEVBQUU7WUFDbkQsT0FBTyxFQUFFLGNBQWM7WUFDdkIsS0FBSyxFQUFFLEtBQUs7WUFDWixhQUFhLEVBQUU7Z0JBQ2IsU0FBUyxFQUFFLE1BQU07YUFDbEI7WUFDRCwyQkFBMkIsRUFBRTtnQkFDM0IsWUFBWSxFQUFFO29CQUNaLGNBQWM7b0JBQ2QsWUFBWTtvQkFDWixlQUFlO29CQUNmLFdBQVc7aUJBQ1o7Z0JBQ0QsWUFBWSxFQUFFLEtBQUssQ0FBQyxJQUFJLENBQUMsV0FBVztnQkFDcEMsZ0JBQWdCLEVBQUUsSUFBSTtnQkFDdEIsWUFBWSxFQUFFLEtBQUssQ0FBQyxJQUFJLENBQUMsV0FBVzthQUNyQztTQUNGLENBQUMsQ0FBQztRQUVILE1BQU0sUUFBUSxHQUFHLEdBQUcsQ0FBQyxJQUFJLENBQUMsV0FBVyxDQUFDLE1BQU0sQ0FBQyxDQUFDO1FBQzlDLFFBQVEsQ0FBQyxTQUFTLENBQUMsTUFBTSxDQUFDLENBQUM7SUFHN0IsQ0FBQztDQUNGO0FBcENELDhDQW9DQyIsInNvdXJjZXNDb250ZW50IjpbImltcG9ydCAqIGFzIGNkayBmcm9tICdAYXdzLWNkay9jb3JlJztcbmltcG9ydCAqIGFzIGxhbWJkYSBmcm9tIFwiQGF3cy1jZGsvYXdzLWxhbWJkYVwiO1xuaW1wb3J0IHsgUHl0aG9uRnVuY3Rpb24gfSBmcm9tIFwiQGF3cy1jZGsvYXdzLWxhbWJkYS1weXRob25cIjtcbmltcG9ydCAqIGFzIGFwaWd3IGZyb20gJ0Bhd3MtY2RrL2F3cy1hcGlnYXRld2F5JztcbmltcG9ydCAqIGFzIHBhdGggZnJvbSAncGF0aCc7XG5cbmV4cG9ydCBjbGFzcyBDZGtDcmlwdG9BcHBTdGFjayBleHRlbmRzIGNkay5TdGFjayB7XG4gIGNvbnN0cnVjdG9yKHNjb3BlOiBjZGsuQ29uc3RydWN0LCBpZDogc3RyaW5nLCBwcm9wcz86IGNkay5TdGFja1Byb3BzKSB7XG4gICAgc3VwZXIoc2NvcGUsIGlkLCBwcm9wcyk7XG5cbiAgICBjb25zdCBsYW1iZGFGdW5jdGlvbiA9IG5ldyBQeXRob25GdW5jdGlvbih0aGlzLCAnTXlGdW5jdGlvbicsIHtcbiAgICAgIGZ1bmN0aW9uTmFtZTogXCJNYWluRnVuY3Rpb25cIixcbiAgICAgIGVudHJ5OiBwYXRoLmpvaW4oX19kaXJuYW1lLCBcIi4vLi4vc3JjXCIpLCAvLyByZXF1aXJlZFxuICAgICAgaW5kZXg6IFwiaW5kZXgucHlcIixcbiAgICAgIGhhbmRsZXI6ICdoYW5kbGVyJywgLy8gb3B0aW9uYWwsIGRlZmF1bHRzIHRvICdoYW5kbGVyJ1xuICAgICAgcnVudGltZTogbGFtYmRhLlJ1bnRpbWUuUFlUSE9OXzNfOCwgLy8gb3B0aW9uYWwsIGRlZmF1bHRzIHRvIGxhbWJkYS5SdW50aW1lLlBZVEhPTl8zXzdcbiAgICB9KTtcblxuICAgIGNvbnN0IGFwaSA9IG5ldyBhcGlndy5MYW1iZGFSZXN0QXBpKHRoaXMsICdHYXRld2F5Jywge1xuICAgICAgaGFuZGxlcjogbGFtYmRhRnVuY3Rpb24sXG4gICAgICBwcm94eTogZmFsc2UsXG4gICAgICBkZXBsb3lPcHRpb25zOiB7XG4gICAgICAgIHN0YWdlTmFtZTogJ3Byb2QnLFxuICAgICAgfSxcbiAgICAgIGRlZmF1bHRDb3JzUHJlZmxpZ2h0T3B0aW9uczoge1xuICAgICAgICBhbGxvd0hlYWRlcnM6IFtcbiAgICAgICAgICAnQ29udGVudC1UeXBlJyxcbiAgICAgICAgICAnWC1BbXotRGF0ZScsXG4gICAgICAgICAgJ0F1dGhvcml6YXRpb24nLFxuICAgICAgICAgICdYLUFwaS1LZXknLFxuICAgICAgICBdLFxuICAgICAgICBhbGxvd01ldGhvZHM6IGFwaWd3LkNvcnMuQUxMX01FVEhPRFMsXG4gICAgICAgIGFsbG93Q3JlZGVudGlhbHM6IHRydWUsXG4gICAgICAgIGFsbG93T3JpZ2luczogYXBpZ3cuQ29ycy5BTExfT1JJR0lOUyxcbiAgICAgIH0sXG4gICAgfSk7XG5cbiAgICBjb25zdCBiYXNlUGF0aCA9IGFwaS5yb290LmFkZFJlc291cmNlKFwibWFpblwiKTtcbiAgICBiYXNlUGF0aC5hZGRNZXRob2QoXCJQT1NUXCIpO1xuXG5cbiAgfVxufVxuIl19