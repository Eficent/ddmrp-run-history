from connection import connect_to_odoo_server
from set_system_time import change_local_system_time
from datetime import datetime, timedelta


def main():
    db_name, sock, uid, pwd = connect_to_odoo_server()
    print 'Connected to Odoo!'
    d = raw_input("Enter final date ('YYYY-MM-DD'): ")
    inc = raw_input("Enter # days increments: ")
    inc = int(inc)
    target_date = datetime.strptime(d, '%Y-%m-%d')
    today = datetime.today()

    current_date = today
    while current_date < target_date:
        try:
            sock.execute(db_name, uid, pwd, 'stock.warehouse.orderpoint',
                         'cron_ddmrp_adu', 1)
        except Exception as e:
            pass

        try:
            sock.execute(db_name, uid, pwd, 'stock.warehouse.orderpoint',
                         'cron_ddmrp', 1)
        except Exception as e:
            pass

        current_date += timedelta(days=inc)
        change_local_system_time(date=str(current_date.date()))
        print 'Changed system date to %s' % current_date.date()


if __name__ == "__main__":
    main()
