import argparse

parser = argparse.ArgumentParser(
                    prog='SAML DEMONSTRATION SEREVR',
                    description="provides demo api's for SAML auth",
                    epilog="""
                    api/{version}/login
                    \n
                    api/{version}/logout
                    \n
                    api/{version}/me
                    """
                    )
__env_choices__ = (
    'local',
    'dev',
    'prod',
    'test'
)
parser.add_argument('-e','--environment',
                    required=True,
                    type=str,
                    help="specify the env you want to run",
                    choices=__env_choices__,
                    )
