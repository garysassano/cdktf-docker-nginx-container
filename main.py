import cdktf
from stacks.nginx_container_stack import NginxContainerStack

app = cdktf.App()

NginxContainerStack(
    app,
    "NginxContainerStack",
)

app.synth()
