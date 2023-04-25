from cdktf import TerraformStack
from cdktf_cdktf_provider_docker.container import Container
from cdktf_cdktf_provider_docker.image import Image
from cdktf_cdktf_provider_docker.provider import DockerProvider
from constructs import Construct


class NginxContainerStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        DockerProvider(
            self,
            "DockerProvider",
        )

        nginx_docker_image = Image(
            self,
            "DockerImage_nginx-latest",
            name="nginx:latest",
            keep_locally=False,
        )

        Container(
            self,
            "DockerContainer_nginx-container",
            name="nginx-container",
            image=nginx_docker_image.name,
            ports=[
                {
                    "internal": 80,
                    "external": 8000,
                }
            ],
            privileged=False,
        )
