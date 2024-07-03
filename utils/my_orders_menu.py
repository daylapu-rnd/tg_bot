from datetime import datetime, timedelta
from utils.general import format_date_time


def create_list_of_orders(ordersData: list, delay: int, status: int) -> list:
    """
    Create List of orders

    Creates a filtered list of orders based on the provided orders data, current date and time, delay, and status.

    :param ordersData: A list of order data, where each order is represented as a dictionary.
    :type ordersData: list
    :param delay: The delay in minutes to be added to the order time for comparison.
    :type delay: int
    :param status: The status filter for orders (0, 1, or 2).
                   0: Include orders that are not 'active' or 'waiting', or orders that have passed the adjusted order time.
                   1: Include orders that are 'agreed' or 'waiting' and have not passed the adjusted trip time.
                   2: Include orders that fall within the delay period.
    :type status: int
    :return: A list of filtered orders based on the provided criteria.
    :rtype: list
    """
    current_datetime = datetime.now()
    data_list = []
    for data in ordersData:
        order_status = data['status']
        order_end_date = datetime.strptime(format_date_time(data['end_date']), "%d.%m.%Y").date()
        order_end_time = datetime.strptime(format_date_time(data['end_time']), "%H:%M").time()
        order_end_datetime = datetime.combine(order_end_date, order_end_time)

        if status == 0:
            order_end_datetime = datetime.combine(order_end_date, order_end_time) + timedelta(minutes=delay)
            if order_status not in ['waiting', 'active']:
                data_list.append(data)
            elif current_datetime >= order_end_datetime:
                data_list.append(data)

        print(f"{current_datetime}\n{order_end_datetime}\n")

        # elif status == 1:
        #     order_end_datetime = datetime.combine(order_end_date, order_end_time) + timedelta(minutes=delay)
        #     if (order_status in ['waiting', 'active']) and (current_datetime <= order_end_datetime):
        #         data_list.append(data)
        #
        # elif status == 2:
        #     if (current_datetime >= order_end_datetime) and (current_datetime <= order_end_datetime + timedelta(minutes=delay)):
        #         data_list.append(data)

    return data_list


def generate_new_str_for_order(user_data):
    """Creates a row depending on the number of items in the list"""
    new_str = ""
    for i, data in enumerate(user_data):
        status = ""
        if data["status"] == "active":
            status = "Активный"
        elif data["status"] == "waiting":
            status = "В ожидании"
        elif data["status"] == "cancelled":
            status = "Отменен"
        elif data["status"] == "complete":
            status = "Завершен"
        else:
            status = "Не актулен"

        if data['apartment'] != '':
            apartment_str = f", кв. {data['apartment']}"
        else:
            apartment_str = ''

        start_date = datetime.strptime(format_date_time(data['start_date']), '%d.%m.%Y').date()
        start_time = datetime.strptime(format_date_time(data['start_time']), '%H:%M').time()
        end_date = datetime.strptime(format_date_time(data['end_date']), '%d.%m.%Y').date()
        end_time = datetime.strptime(format_date_time(data['end_time']), '%H:%M').time()

        start_datetime = datetime.combine(start_date, start_time)
        end_datetime = datetime.combine(end_date, end_time)

        new_str += f"""
{i + 1}.
Статус: {data['status']}
Время начала исполнения: {start_datetime}
Время окончания исполнения: {end_datetime}
Детали: {data['service_details']}
Опции: {data['options']}
Адрес: г. {data['city']}, ул. {data['street']}, д. {data['house']}{apartment_str}
"""
    return new_str