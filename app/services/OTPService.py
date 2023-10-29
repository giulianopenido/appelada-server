import boto3
import hashlib

from botocore.exceptions import ClientError

from app.configs.Environment import get_environment_variables

env = get_environment_variables()


def generate_ref_id(destinationNumber, name):
    refId = name + destinationNumber
    return hashlib.md5(refId.encode()).hexdigest()


otpCodeLength = 5
allowedAttempts = 2
validityPeriod = 15
brandName = env.APP_NAME
originNumber = env.OTP_ORIGIN_NUMBER


class OTPService:
    def __init__(self):
        self.client = boto3.client(
            'pinpoint',
            region_name=env.AWS_REGION_NAME,
            aws_access_key_id=env.AWS_ACCESS_KEY,
            aws_secret_access_key=env.AWS_PRIVATE_KEY
        )

    def send_otp(self, language: str, destinationNumber: str):
        try:
            self.client.send_otp_message(
                ApplicationId=env.AWS_APPLICATION_ID,
                SendOTPMessageRequestParameters={
                    'Channel': 'SMS',
                    'BrandName': env.APP_NAME,
                    'CodeLength': otpCodeLength,
                    'ValidityPeriod': validityPeriod,
                    'AllowedAttempts': allowedAttempts,
                    'Language': language,
                    'DestinationIdentity': destinationNumber,
                    'OriginationIdentity': originNumber,
                    'ReferenceId': generate_ref_id(destinationNumber, brandName)
                }
            )

        except ClientError as e:
            return

    def verify_otp(self, destinationNumber, otp):
        try:
            response = self.client.verify_otp_message(
                ApplicationId=env.AWS_APPLICATION_ID,
                VerifyOTPMessageRequestParameters={
                    'DestinationIdentity': destinationNumber,
                    'ReferenceId': generate_ref_id(destinationNumber, brandName),
                    'Otp': otp
                }
            )
            return response['VerificationResponse']['Valid']

        except ClientError as e:
            return False
