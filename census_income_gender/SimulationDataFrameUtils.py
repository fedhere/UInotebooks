def _xml_to_dataframe(xml_list):
    ''' Takes a list of XML strings and turns it into a dataframe '''
    # Get the header
    xml_str = xml_list[0]
    root = etree.fromstring(xml_str)
    header = _extract_position_names(root)
    scenario_data = {}
    for position_name in header:
        scenario_data[position_name] = []

    for xml_str in xml_list:
        scenario = etree.fromstring(xml_str)
        positions = scenario[4]
        for position in positions:
            position_size = (position.text).replace(',','')
            scenario_data[position.get('id')].append(float(position_size))

    # Get dates
    scenario_dates = []
    for element in xml_list:
        scenario = etree.fromstring(element)
        date_string = scenario[1].text
        date = datetime.datetime.strptime(date_string, '%Y%m%d')
        scenario_dates.append(date)

    dataframe = pandas.DataFrame(scenario_data, index=scenario_dates)
    return dataframe
