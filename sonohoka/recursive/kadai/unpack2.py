"""
Creating Unpack function for list and dictionary
"""
ETM_FILTER_DATA1 = [{'Description': 'EC2 Instance Security Group created by Entanglement',
                     'GroupName': 'app1-sg-teststack-EtmESpintentanglementapp1Elb-A8LX211UERUF', 'IpPermissions': [
        {'FromPort': 443, 'IpProtocol': 'tcp', 'IpRanges': [], 'Ipv6Ranges': [], 'PrefixListIds': [], 'ToPort': 443,
         'UserIdGroupPairs': [
             {'Description': 'Entanglement rule for EtmESpintentanglementapp1Elb', 'GroupId': 'sg-06d83ed1a616b44aa',
              'UserId': '472973657150'}]}], 'OwnerId': '472973657150', 'GroupId': 'sg-02d46efde34216876',
                     'IpPermissionsEgress': [{'FromPort': 0, 'IpProtocol': 'tcp', 'IpRanges': [
                         {'CidrIp': '127.0.0.1/32',
                          'Description': 'Entanglement rule for EtmESpintentanglementapp1Elb'}], 'Ipv6Ranges': [],
                                              'PrefixListIds': [], 'ToPort': 65335, 'UserIdGroupPairs': []}],
                     'Tags': [{'Key': 'ManifestFilePath', 'Value': 'manifest/app1elb.yml'},
                              {'Key': 'PCI Scope', 'Value': 'CAT2'}, {'Key': 'aws:cloudformation:stack-id',
                                                                      'Value': 'arn:aws:cloudformation:us-west-2:472973657150:stack/app1-sg-teststack/86383a40-729b-11e9-bb0f-06cbb9434982'},
                              {'Key': 'Environment', 'Value': 'E'},
                              {'Key': 'Service', 'Value': 'EtmESpint_entanglementapp1Elb_472973657150'},
                              {'Key': 'Git tag', 'Value': '1.0.0'},
                              {'Key': 'aws:cloudformation:logical-id', 'Value': 'EtmESpintentanglementapp1Elb'},
                              {'Key': 'Git Repo', 'Value': 'https://github.sie.sony.com/SIE/entanglementapp1'},
                              {'Key': 'Name', 'Value': 'Etm-Spint-E-entanglementapp1Elb'},
                              {'Key': 'aws:cloudformation:stack-name', 'Value': 'app1-sg-teststack'}],
                     'VpcId': 'vpc-f4156492'}, {'Description': 'EC2 Instance Security Group created by Entanglement',
                                                'GroupName': 'app2-sg-teststack-EtmESpintentanglementapp2Elb-18VIV4YMTRFNH',
                                                'IpPermissions': [
                                                    {'FromPort': 8888, 'IpProtocol': 'tcp', 'IpRanges': [],
                                                     'Ipv6Ranges': [], 'PrefixListIds': [], 'ToPort': 8888,
                                                     'UserIdGroupPairs': [{
                                                                              'Description': 'Entanglement rule for EtmESpintentanglementapp2Elb',
                                                                              'GroupId': 'sg-09356d729c2c2c28f',
                                                                              'UserId': '472973657150'}]},
                                                    {'FromPort': 443, 'IpProtocol': 'tcp', 'IpRanges': [],
                                                     'Ipv6Ranges': [], 'PrefixListIds': [], 'ToPort': 443,
                                                     'UserIdGroupPairs': [{
                                                                              'Description': 'Entanglement rule for EtmESpintentanglementapp2Elb',
                                                                              'GroupId': 'sg-0568226f2eb3a8b48',
                                                                              'UserId': '472973657150'}, {
                                                                              'Description': 'Entanglement rule for EtmESpintentanglementapp2Elb',
                                                                              'GroupId': 'sg-06d83ed1a616b44aa',
                                                                              'UserId': '472973657150'}]}],
                                                'OwnerId': '472973657150', 'GroupId': 'sg-045b8899afb7d2aad',
                                                'IpPermissionsEgress': [{'FromPort': 0, 'IpProtocol': 'tcp',
                                                                         'IpRanges': [{'CidrIp': '127.0.0.1/32',
                                                                                       'Description': 'Entanglement rule for EtmESpintentanglementapp2Elb'}],
                                                                         'Ipv6Ranges': [], 'PrefixListIds': [],
                                                                         'ToPort': 65335, 'UserIdGroupPairs': []}],
                                                'Tags': [{'Key': 'PCI Scope', 'Value': 'CAT2'},
                                                         {'Key': 'Environment', 'Value': 'E'},
                                                         {'Key': 'Name', 'Value': 'Etm-Spint-E-entanglementapp2Elb'},
                                                         {'Key': 'Service',
                                                          'Value': 'EtmESpint_entanglementapp2Elb_472973657150'},
                                                         {'Key': 'Git Repo',
                                                          'Value': 'https://github.sie.sony.com/SIE/entanglementapp2'},
                                                         {'Key': 'aws:cloudformation:stack-id',
                                                          'Value': 'arn:aws:cloudformation:us-west-2:472973657150:stack/app2-sg-teststack/ff0d1f00-729e-11e9-9d6a-02035744c0fa'},
                                                         {'Key': 'aws:cloudformation:stack-name',
                                                          'Value': 'app2-sg-teststack'},
                                                         {'Key': 'aws:cloudformation:logical-id',
                                                          'Value': 'EtmESpintentanglementapp2Elb'}],
                                                'VpcId': 'vpc-f4156492'}]

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


print(unpack_data(mydic))

def unpack_aws(data):
    result =[]
    if isinstance(data, list):
        for i in range(len(data)):
            if isinstance(data[i], dict):
                inbound_rule = data[i]['IpPermissions']
                # if isinstance(inbound_rule, list):
                #     print('Yes')
                #     print(inbound_rule)
                for rule in inbound_rule:
                    print(rule)


print(unpack_aws(ETM_FILTER_DATA1))