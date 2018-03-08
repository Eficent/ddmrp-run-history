# ddmrp-run-history

DDMRP Run History
=================

This script allows you to build DDMRP history by walking through a range of
dates changing user's system date on steps of X days up to a certain date, and
running the cron jobs that update the DDMRP buffers.

How to execute it
-----------------

run 'sudo python ./ddmrp_run_history.py'. You will be prompted to provide:

* Host (e.g. 'http://localhost:8069')
* Database (e.g. 'demo')
* User (e.g. 'admin')
* Password (e.g. 'admin')
* Future date (e.g. '2019-01-01')
* # days increments (e.g. '30')

This will make the system to log to odoo, run the DDMRP crons, and change the
system date to today's + # days inc
