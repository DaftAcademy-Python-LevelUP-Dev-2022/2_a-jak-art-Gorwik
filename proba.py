if __name__ == "__main__":
    required_keys = "company_name", "address", "city_code__city__country"
    new_dict = {}
    REQUIRED_KEYS = []
    for required_key in required_keys:
        new_dict[required_key] = False
        if "__" in required_key:
            required_key = required_key.split("__")
            for list_key in required_key:
              REQUIRED_KEYS.append(list_key)
        else:
            REQUIRED_KEYS.append(required_key)
    
    dict_of_parameters = {
         "country": "Poland",
        "company_name": "DaftCode",
        "address": "Pl. Europejski 1",
        "city": "Warsaw",
        "city_code": "00-844",
        }


    for key in REQUIRED_KEYS:
        if not key in dict_of_parameters.keys():
            raise ValueError

    for required_key in new_dict.keys():
        for key, value in dict_of_parameters.items():
            if key in required_key:
                if not new_dict[required_key]:
                    if not value:
                        new_dict[required_key] = "Empty value"
                        break
                    else:    
                        new_dict[required_key] = value
                        break
                else:
                    new_dict[required_key] = new_dict[required_key] + " " + value
                    break