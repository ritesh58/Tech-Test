Problem:

    A 3 tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.

Solution:

![image](https://user-images.githubusercontent.com/3917151/176560214-d275822d-d125-43b2-88a0-0abeff4f7466.png)

   I would be using Infastructure as Code(IaC) approach using Azure Resource Manager (ARM) Template(Reusable JSON code for repeatable or similar         provisioning or deployment).
   
   Environment consists of:
   
       1. A virtual Network
       2. 4 Subnets(Each tier is also placed inside its own subnet)
       3. 4 Network security groups for each subnet
       4. An external load balancer to distribute Internet requests across the instances
       5. An Internal Load Balancer to load balance traffic for app VM's
       6. One jumpbox(bastion host) for ssh access to all other tier VMs
       7. 2 Public IP’s, one for external Load balancer and other for Jump VM
       8. Virtual Machine Availability sets for Web Tier, Application Tier and Database tier.
       9. storage accounts
