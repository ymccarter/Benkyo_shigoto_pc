"""
Creating Unpack function for list and dictionary
"""
simple_data = [{1:[{'1a':'bar'}, {'1b':'neko'}]},{2:[{'2a':'Mickey'}, {'2b':'airport'}]},{3:'foo'}]
simple_data2 = [{1:[{'1a':'bar'}, {'1b':'neko'}]},{2:[{'2a':'Mickey'}, {'2b':'airport'}]},{3:'foo'}, "apple"]
simple_data3 = [{1:[{'1a':'bar'}, {'1b':'neko'}]},{2:[{'2a':'Mickey'}, {'2b':'airport'}]},{3:'foo'}, 'apple', 'orange', {4:['jacuzzie', 'sunset']}]


def flatten_list(my_list):
    """this will unpack list in list"""
    result = []
    for item in my_list:
        if isinstance(item, list):
            flat_list = flatten_list(item)
            result += flat_list
        else:
            result.append(item)
    return result


def flatten_dictionary(my_dictionary):
    result = []
    for k, v in my_dictionary.items():
        if isinstance(v, dict):
            new_dict = flatten_value(v)
            result += new_dict
        else:
            result.append("{0}".format(v))
    return result


mydic = {'sg':[1,2,3], 'ec2-ami':[234, 455, 678], 'vpc-id':{'1234':'5678'}, 'happy':[[['mickey', 'neko'], 'jacczzy'], 'airport']}

def unpack_data(my_dictionary):
    result = []
    for k, v in my_dictionary.items():
        if isinstance(v, dict):
            new_dict = flatten_dictionary(v)
            result += new_dict
        elif isinstance(v, list):
            for x in v:
                if isinstance(x,list):
                    new_list = flatten_list(x)
                    for y in new_list:
                        result.append(y)
                else:
                    result.append(x)
        else:
            result.append("{0}".format(v))
    return result

# print(unpack_data(mydic))

def unpack_data2(data):
    result = []
    if isinstance(data,list):
        for item in data:
            #print(item)
            if isinstance(item, str):
                result.append(item)
            else:
                for k,v in item.items():
                    if isinstance(v, list):
                        #import pdb;pdb.set_trace()
                        new_list = flatten_list(v)
                        #
                        result += new_list
                        for y in new_list:
                            if isinstance(y, dict):
                                new_dict = flatten_dictionary(y)
                                result += new_dict
                    else:
                        result.append(v)
    return result

#print(unpack_data2(simple_data))
#print(unpack_data2(simple_data2))
print(unpack_data2(simple_data3))