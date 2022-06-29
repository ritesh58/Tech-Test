Problem:

    A 3 tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.

Solution:

    I would be using Infastructure as Code(IaC) approach using Azure Resource Manager (ARM) Template(Reusable JSON code for repeatable or similar provisioning or deployment).
      Environment consists of:
        1 Virtual Network
        4 Subnets(Each tier is also placed inside its own subnet)
        4 Network security groups for each subnet
        An external load balancer to distribute Internet requests across the instances
        An Internal Load Balancer to load balance traffic for app VM's
        One jumpbox(bastion host) for ssh access to all other tier VMs
        2 Public IP’s, one for external Load balancer and other for Jump VM
        3 Virtual Machine Availability sets for Web Tier, Application Tier and Database tier.
        4 storage accounts