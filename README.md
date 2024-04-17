
Open EduCate SyncLogs
----

for this docker image, I simply used an official odoo and postgre container image 
and then created my docker-compose.yml file with a simple configuration for this task.

This Repo Contains the Full Docker with odoo and postgre
Navigate To The repo directory and simply run 

    docker-compose up -d

and Then You'll Find the System accessible through <yourdomain-name.com:3333>
The Custom Module with All Related Work will be found under addons/openeducate_sync_log

Getting Started with the Feature
-------------------------

in the root menus, you'll find a sync Log menu [ONLY AVAILABLE FOR BACK OFFICE ADMIN GROUP ]
once clicked, you'll see all the sync logs that happened on Parent and Student As Requested.




