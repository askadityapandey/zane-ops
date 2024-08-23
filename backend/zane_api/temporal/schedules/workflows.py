from datetime import timedelta

from temporalio import workflow
from temporalio.common import RetryPolicy

from .activities import MonitorDockerDeploymentActivities
from ..shared import HealthcheckDeploymentDetails, DeploymentHealthcheckResult

with workflow.unsafe.imports_passed_through():
    from django.conf import settings


@workflow.defn(name="monitor-docker-deployment-workflow")
class MonitorDockerDeploymentWorkflow:
    @workflow.run
    async def run(self, payload: HealthcheckDeploymentDetails):
        print(f"\nRunning workflow MonitorDockerDeploymentWorkflow with {payload=}")
        retry_policy = RetryPolicy(
            maximum_attempts=5, maximum_interval=timedelta(seconds=30)
        )

        print(f"Running activity `run_deployment_monitor_healthcheck({payload=})`")
        healthcheck_timeout = (
            payload.healthcheck.timeout_seconds
            if payload.healthcheck is not None
            else settings.DEFAULT_HEALTHCHECK_TIMEOUT
        )
        deployment_status, deployment_status_reason = (
            await workflow.execute_activity_method(
                MonitorDockerDeploymentActivities.run_deployment_monitor_healthcheck,
                payload,
                retry_policy=retry_policy,
                start_to_close_timeout=timedelta(seconds=healthcheck_timeout + 5),
            )
        )

        healthcheck_result = DeploymentHealthcheckResult(
            deployment_hash=payload.deployment.hash,
            status=deployment_status,
            reason=deployment_status_reason,
        )
        print(f"Running activity `save_deployment_status({healthcheck_result=})`")
        await workflow.execute_activity_method(
            MonitorDockerDeploymentActivities.save_deployment_status,
            healthcheck_result,
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy=retry_policy,
        )
        return deployment_status, deployment_status_reason