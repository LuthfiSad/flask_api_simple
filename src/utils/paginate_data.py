def paginate_data(data, page=1, per_page=10):
    """
    Paginate the data.
    :param data: The list of data to paginate.
    :param page: The page number.
    :param per_page: The number of items per page.
    :return: A tuple containing the paginated data and meta information.
    """
    total_data = len(data)
    total_pages = (total_data + per_page - 1) // per_page  # This ensures we always round up

    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = data[start:end]

    meta = {
        "page": page,
        "perPage": per_page,
        "totalData": total_data,
        "totalPages": total_pages
    }

    return paginated_data, meta