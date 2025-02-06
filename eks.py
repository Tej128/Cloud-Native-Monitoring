from kubernetes import client, config

def load_kube_config():
    """Load Kubernetes configuration."""
    config.load_kube_config()

def create_deployment_object():
    """Create a Kubernetes Deployment object."""
    container = client.V1Container(
        name="my-flask-container",
        image="568373317874.dkr.ecr.us-east-1.amazonaws.com/my_monitoring_app_image:latest",
        ports=[client.V1ContainerPort(container_port=5000)]
    )

    pod_spec = client.V1PodSpec(containers=[container])

    pod_template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "my-flask-app"}),
        spec=pod_spec
    )

    deployment_spec = client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(match_labels={"app": "my-flask-app"}),
        template=pod_template
    )

    deployment = client.V1Deployment(
        metadata=client.V1ObjectMeta(name="my-flask-app"),
        spec=deployment_spec
    )
    
    return deployment

def create_service_object():
    """Create a Kubernetes Service object."""
    service_port = client.V1ServicePort(port=5000)

    service_spec = client.V1ServiceSpec(
        selector={"app": "my-flask-app"},
        ports=[service_port]
    )

    service = client.V1Service(
        metadata=client.V1ObjectMeta(name="my-flask-service"),
        spec=service_spec
    )
    
    return service

def create_k8s_resources():
    """Create the Deployment and Service in Kubernetes."""
    api_client = client.ApiClient()

    # Create Deployment
    deployment = create_deployment_object()
    apps_v1_api = client.AppsV1Api(api_client)
    apps_v1_api.create_namespaced_deployment(namespace="default", body=deployment)

    # Create Service
    service = create_service_object()
    core_v1_api = client.CoreV1Api(api_client)
    core_v1_api.create_namespaced_service(namespace="default", body=service)

if __name__ == "__main__":
    # Load the kube config and create the resources
    load_kube_config()
    create_k8s_resources()
