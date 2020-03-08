awsdata = {
    'SecurityGroups': [{
        'Description':
        'default group',
        'GroupName':
        'default',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-e9a7e4d9',
                'GroupName': 'default',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            0,
            'IpProtocol':
            'udp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-e9a7e4d9',
                'GroupName': 'default',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            -1,
            'IpProtocol':
            'icmp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            -1,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-e9a7e4d9',
                'GroupName': 'default',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e9a7e4d9',
        'IpPermissionsEgress': []
    }, {
        'Description':
        'Base Security Group',
        'GroupName':
        'testupdateAprYM-SGBase-9MGT9DA4PH8M',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ccf39cff',
        'IpPermissionsEgress': [],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/testupdateAprYM/c79ded10-3dde-11e8-8557-503acbd4dc99'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'SGBase'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'testupdateAprYM'
        }]
    }, {
        'Description': 'SG for elb YM test051618',
        'GroupName': 'myelbsecuritygroup',
        'IpPermissions': [],
        'OwnerId': '472973657150',
        'GroupId': 'sg-81a6c8b2',
        'IpPermissionsEgress': []
    }, {
        'Description':
        'AutoScaling-Security-Group-1 (2018-07-16 09:07:09.046-07:00)',
        'GroupName': 'AutoScaling-Security-Group-1',
        'IpPermissions': [],
        'OwnerId': '472973657150',
        'GroupId': 'sg-fca1c8cf',
        'IpPermissionsEgress': []
    }, {
        'Description':
        'EC2 Instance Security Group',
        'GroupName':
        'test-SERVICENAME-2HTYZOM8WDHD',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0b955aeb521478620',
        'IpPermissionsEgress': [],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/test/53652fe0-453e-11e9-85f7-0a152f9ae918'
        }, {
            'Key': 'TestingTag',
            'Value': 'TagValue'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'test'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'SERVICENAME'
        }]
    }, {
        'Description':
        'EC2 Instance Security Group',
        'GroupName':
        'Testing-testing-COZMOPJOE3Y3',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'Description': 'test',
                'GroupId': 'sg-0bdad3d4b3094cb2e',
                'GroupName': 's3tocfn-testing1-1SOKI49HKSA0D',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.10.10.10/32',
                'Description': 'test'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-05baa3649a1855563',
        'IpPermissionsEgress': [],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/Testing/4f8613b0-4b4e-11e9-8b1d-0688a7bf983a'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'testing'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'Testing'
        }, {
            'Key': 'TestingTag',
            'Value': 'TagValue'
        }]
    }, {
        'Description':
        'EC2 Instance Security Group',
        'GroupName':
        's3tocfn-testing1-1SOKI49HKSA0D',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0bdad3d4b3094cb2e',
        'IpPermissionsEgress': [],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'testing1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/s3tocfn/e13dfbf0-6bb1-11e9-b497-020d7038e876'
        }, {
            'Key': 'TestingTag',
            'Value': 'TagValue1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 's3tocfn'
        }]
    }, {
        'Description':
        'SG for payments redis cluster',
        'GroupName':
        'payments-redis-sg',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-005507b5e10e879b9',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [{
                'CidrIpv6': '::/0'
            }],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'paymentsRedisSGSandbox'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'SG for GTS team instances',
        'GroupName':
        'nav-sandbox-gts',
        'IpPermissions': [{
            'FromPort': 5439,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5439,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 3306,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3306,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-005b6da7641fcb4a5',
        'IpPermissionsEgress': [{
            'FromPort': 5439,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5439,
            'UserIdGroupPairs': []
        }, {
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 3306,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3306,
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'vouchertransferservers',
        'GroupName':
        'vouchertransferservers',
        'IpPermissions': [{
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '65.112.217.8/32'
            }, {
                'CidrIp': '207.251.96.250/32'
            }, {
                'CidrIp': '54.241.156.131/32'
            }, {
                'CidrIp': '65.125.117.8/32'
            }, {
                'CidrIp': '54.215.187.140/32'
            }, {
                'CidrIp': '65.125.54.250/32'
            }, {
                'CidrIp': '54.241.142.184/32'
            }, {
                'CidrIp': '50.18.189.195/32'
            }, {
                'CidrIp': '69.36.131.254/32'
            }, {
                'CidrIp': '54.219.190.140/32'
            }, {
                'CidrIp': '50.18.199.35/32'
            }, {
                'CidrIp': '50.18.204.1/32'
            }, {
                'CidrIp': '50.18.209.111/32'
            }, {
                'CidrIp': '160.33.195.16/29'
            }, {
                'CidrIp': '70.47.187.140/32'
            }, {
                'CidrIp': '54.219.190.139/32'
            }, {
                'CidrIp': '160.33.43.231/32'
            }, {
                'CidrIp': '50.18.197.27/32'
            }, {
                'CidrIp': '85.133.81.132/32'
            }, {
                'CidrIp': '160.33.108.22/32'
            }, {
                'CidrIp': '54.219.190.128/26'
            }, {
                'CidrIp': '160.33.193.22/32'
            }, {
                'CidrIp': '50.18.211.29/32'
            }, {
                'CidrIp': '160.33.192.22/32'
            }, {
                'CidrIp': '160.33.45.139/32'
            }, {
                'CidrIp': '195.54.59.4/32'
            }, {
                'CidrIp': '139.131.76.101/32'
            }, {
                'CidrIp': '54.219.190.137/32'
            }, {
                'CidrIp': '63.148.46.24/32'
            }, {
                'CidrIp': '50.18.195.63/32'
            }, {
                'CidrIp': '160.33.76.22/32'
            }, {
                'CidrIp': '50.18.141.125/32'
            }, {
                'CidrIp': '54.219.154.186/32'
            }, {
                'CidrIp': '217.156.157.2/32'
            }, {
                'CidrIp': '54.219.190.141/32'
            }, {
                'CidrIp': '54.241.132.246/32'
            }, {
                'CidrIp': '50.18.207.230/32'
            }, {
                'CidrIp': '85.133.81.138/32'
            }, {
                'CidrIp': '198.107.156.131/32'
            }, {
                'CidrIp': '65.51.244.20/32'
            }, {
                'CidrIp': '50.18.204.7/32'
            }, {
                'CidrIp': '54.219.190.138/32'
            }, {
                'CidrIp': '184.169.142.142/32'
            }, {
                'CidrIp': '113.43.77.30/32'
            }, {
                'CidrIp': '174.46.232.13/32'
            }, {
                'CidrIp': '204.236.131.106/32'
            }, {
                'CidrIp': '85.133.81.190/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-011ea05aa0892efa8',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'vouchertransferservers'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'vouchertransferservers'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-globaldef'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-globaldef/0cdf13f0-ce4d-11e8-8913-0a578203aa12'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Security group for all nodes in the cluster',
        'GroupName':
        'test-eks3-NodeSecurityGroup-B8TQJB2Y8XDL',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'Description': 'Allow node to communicate with each other',
                'GroupId': 'sg-012cec7c5e47afba1',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            1025,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'Description':
                'Allow worker Kubelets and pods to receive communication from the cluster control plane',
                'GroupId': 'sg-0d893e70',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Allow pods running extension API servers on port 443 to receive communication from cluster control plane',
                'GroupId': 'sg-0d893e70',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-012cec7c5e47afba1',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'eks-test-3'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'test-eks3'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'NodeSecurityGroup'
        }, {
            'Key': 'kubernetes.io/cluster/test-eks3',
            'Value': 'owned'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/test-eks3/b11291e0-6146-11e9-98d4-0a0f0b9aa76a'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'spinnaker',
        'GroupName':
        'spinnaker-allow-any',
        'IpPermissions': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [{
                'CidrIpv6': '::/0'
            }],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-019b117bea76c1a08',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'spinnaker'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'test-sg',
        'GroupName':
        'test-sg',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-019d81be43a3fdcf0',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Security group for all nodes in the cluster',
        'GroupName':
        'test-eks2-worker-nodes-NodeSecurityGroup-GJCPT7RSEFSX',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'Description': 'Allow node to communicate with each other',
                'GroupId': 'sg-01e98a00647923a10',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            1025,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'Description':
                'Allow worker Kubelets and pods to receive communication from the cluster control plane',
                'GroupId': 'sg-0d893e70',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Allow pods running extension API servers on port 443 to receive communication from cluster control plane',
                'GroupId': 'sg-0d893e70',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-01e98a00647923a10',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/test-eks2',
            'Value': 'owned'
        }, {
            'Key': 'Name',
            'Value': 'eks-test-2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/test-eks2-worker-nodes/3d411570-fa85-11e8-844d-50a68a20128e'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'test-eks2-worker-nodes'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'NodeSecurityGroup'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description': 'no rules inside',
        'GroupName': 'tritenour-sg-ssh-out',
        'IpPermissions': [],
        'OwnerId': '472973657150',
        'GroupId': 'sg-0229e87c',
        'IpPermissionsEgress': [],
        'Tags': [{
            'Key': 'Name',
            'Value': 'sshout'
        }],
        'VpcId': 'vpc-1721cf71'
    }, {
        'Description':
        'oltpNP',
        'GroupName':
        'oltpNP',
        'IpPermissions': [{
            'FromPort':
            1521,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.219.129.246/32'
            }, {
                'CidrIp': '10.201.200.0/22'
            }, {
                'CidrIp': '10.219.131.16/28'
            }, {
                'CidrIp': '10.201.192.0/21'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            1521,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0263142f992e0c083',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbProd-NPdef1/e6d35cf0-c52a-11e8-9fe0-0a3c8425d484'
        }, {
            'Key': 'Name',
            'Value': 'nav-oltp'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbProd-NPdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'oltpNP'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceamazonpaylistenerEMGMT',
        'GroupName':
        'commerceamazonpaylistenerEMGMT',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-027399c8bbc89a3a2',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceamazonpaylistenerEMGMT'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceamazonpaylistenerEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Security group for Kubernetes ELB a1f9e3da35d7811e9bb5b06a35c5c866 (sensu/poc-uchiwa-elb)',
        'GroupName':
        'k8s-elb-a1f9e3da35d7811e9bb5b06a35c5c866',
        'IpPermissions': [{
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 80,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-02a63ca123c62fce8',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/srt-poc',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'managed instance securityGroup by ALB Ingress Controller',
        'GroupName':
        'instance-54972eaf-default-nginxserv-bc24',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-09517b00e308a78b6',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-02cceac7f1a6d0535',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/test-eks3',
            'Value': 'owned'
        }, {
            'Key': 'kubernetes.io/ingress-name',
            'Value': 'nginx-service-ip-ingress'
        }, {
            'Key': 'kubernetes.io/namespace',
            'Value': 'default'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'EC2 Instance Security Group created by Entanglement',
        'GroupName':
        'app1-sg-teststack-EtmESpintentanglementapp1Elb-A8LX211UERUF',
        'IpPermissions': [{
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Entanglement rule for EtmESpintentanglementapp1Elb',
                'GroupId': 'sg-06d83ed1a616b44aa',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-02d46efde34216876',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp':
                '127.0.0.1/32',
                'Description':
                'Entanglement rule for EtmESpintentanglementapp1Elb'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65335,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'GitManifest',
            'Value': 'manifest/app1elb.yml'
        }, {
            'Key': 'PCI Scope',
            'Value': 'CAT2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/app1-sg-teststack/86383a40-729b-11e9-bb0f-06cbb9434982'
        }, {
            'Key': 'Environment',
            'Value': 'E'
        }, {
            'Key': 'Service',
            'Value': 'EtmESpint_entanglementapp1Elb_472973657150'
        }, {
            'Key': 'Git tag',
            'Value': '1.0.0'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'EtmESpintentanglementapp1Elb'
        }, {
            'Key': 'Git Repo',
            'Value': 'https://github.sie.sony.com/SIE/entanglementapp1'
        }, {
            'Key': 'Name',
            'Value': 'Etm-Spint-E-entanglementapp1Elb'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'app1-sg-teststack'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'shardmanagementserviceNP',
        'GroupName':
        'shardmanagementserviceNP',
        'IpPermissions': [{
            'FromPort':
            1521,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.211.198.116/30'
            }, {
                'CidrIp': '10.219.134.96/30'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            1521,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-030307c9e23fa2d76',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'shardmanagementserviceNP'
        }, {
            'Key': 'Name',
            'Value': 'nav-shardmanagementservice'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbProd-NPdef1/e6d35cf0-c52a-11e8-9fe0-0a3c8425d484'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbProd-NPdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'eveaggregationEMGMT',
        'GroupName':
        'eveaggregationEMGMT',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-031d7fdb63f00acfc',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }, {
            'Key': 'Name',
            'Value': 'nav-eveaggregationEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eveaggregationEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'mgssnsresponderEMGMT',
        'GroupName':
        'mgssnsresponderEMGMT',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-03844647ce2d8b0b5',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mgssnsresponderEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }, {
            'Key': 'Name',
            'Value': 'nav-mgssnsresponderEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'eks-harness-poc-worker-node',
        'GroupName':
        'eks-harness-poc-worker-node',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'Description': 'Worker node security group',
                'GroupId': 'sg-038721e5576cefd14',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            1025,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'Description': 'Control plane security group',
                'GroupId': 'sg-0fe9c00568197171b',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description': 'Control plane security group',
                'GroupId': 'sg-0fe9c00568197171b',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-038721e5576cefd14',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'eks-harness-poc-worker-node'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Security group for Kubernetes ELB a6c94a2424c3411e99a350a13514bf23 (default/nc-service)',
        'GroupName':
        'k8s-elb-a6c94a2424c3411e99a350a13514bf23',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-03b0334ae15c99267',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/srt-poc',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'spinnaker-poc-jenkins created 2019-03-07T16:01:36.541-08:00',
        'GroupName':
        'spinnaker-poc-jenkins',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': 'Jenkins from SIE office'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description': 'Jenkins from Spinnaker POC Worker Nodes',
                'GroupId': 'sg-05d4c8baf13162914',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': 'SSH from SIE office'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-03eea6dcb8f8da4f3',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'spinnaker-poc-jenkins'
        }],
        'VpcId':
        'vpc-07320a17be9bda61c'
    }, {
        'Description':
        'SSH-inbound-from-office',
        'GroupName':
        'SSH-inbound',
        'IpPermissions': [{
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-03effa3b8c1a040dc',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'Almilli desktop',
        'GroupName':
        'almilli-desktop',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.12.121/32'
            }, {
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0402a73a9b1a0fbe6',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'managed LoadBalancer securityGroup by ALB Ingress Controller',
        'GroupName':
        '23901e39-2048game-2048ipin-ccc3',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-041b1cd91bc454eee',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/ingress-name',
            'Value': '2048-ip-ingress'
        }, {
            'Key': 'kubernetes.io/namespace',
            'Value': '2048-game'
        }, {
            'Key': 'kubernetes.io/cluster/test-eks2',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commercepaypalresponderPL',
        'GroupName':
        'commercepaypalresponderPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-04411a7a',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercepaypalresponder'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercepaypalresponderPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'EC2 Instance Security Group created by Entanglement',
        'GroupName':
        'app2-sg-teststack-EtmESpintentanglementapp2Elb-18VIV4YMTRFNH',
        'IpPermissions': [{
            'FromPort':
            8888,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8888,
            'UserIdGroupPairs': [{
                'Description':
                'Entanglement rule for EtmESpintentanglementapp2Elb',
                'GroupId': 'sg-09356d729c2c2c28f',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Entanglement rule for EtmESpintentanglementapp2Elb',
                'GroupId': 'sg-0568226f2eb3a8b48',
                'UserId': '472973657150'
            }, {
                'Description':
                'Entanglement rule for EtmESpintentanglementapp2Elb',
                'GroupId': 'sg-06d83ed1a616b44aa',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-045b8899afb7d2aad',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp':
                '127.0.0.1/32',
                'Description':
                'Entanglement rule for EtmESpintentanglementapp2Elb'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65335,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'PCI Scope',
            'Value': 'CAT2'
        }, {
            'Key': 'Environment',
            'Value': 'E'
        }, {
            'Key': 'Name',
            'Value': 'Etm-Spint-E-entanglementapp2Elb'
        }, {
            'Key': 'Service',
            'Value': 'EtmESpint_entanglementapp2Elb_472973657150'
        }, {
            'Key': 'Git Repo',
            'Value': 'https://github.sie.sony.com/SIE/entanglementapp2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/app2-sg-teststack/ff0d1f00-729e-11e9-9d6a-02035744c0fa'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'app2-sg-teststack'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'EtmESpintentanglementapp2Elb'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'Security group for Kubernetes ELB a9da1c884f1bc11e8a1e2069dab24ef7 (microservices-aws/frontend-external)',
        'GroupName':
        'k8s-elb-a9da1c884f1bc11e8a1e2069dab24ef7',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-049207b3d935133fb',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/aws-dev303-workshop',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commerceamazonpayresponderEMGMT',
        'GroupName':
        'commerceamazonpayresponderEMGMT',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-049d29c05452796d1',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceamazonpayresponderEMGMT'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceamazonpayresponderEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Security group for AWS Cloud9 environment aws-cloud9-test9-1-7068281702fb4ddcaca1489b2a717f8f',
        'GroupName':
        'aws-cloud9-test9-1-7068281702fb4ddcaca1489b2a717f8f-InstanceSecurityGroup-BQRFNTNHVM7E',
        'IpPermissions': [{
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '34.217.141.224/27'
            }, {
                'CidrIp': '34.218.119.32/27'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-049e97e83f1ae7ce8',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'InstanceSecurityGroup'
        }, {
            'Key': 'aws:cloud9:owner',
            'Value': 'AROAJ7MLVB4RUHIPTEMAK:manchlia@am.sony.com'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/aws-cloud9-test9-1-7068281702fb4ddcaca1489b2a717f8f/75e12d60-f4f0-11e8-b1b6-0254f5c7f298'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'aws-cloud9-test9-1-7068281702fb4ddcaca1489b2a717f8f'
        }, {
            'Key': 'aws:cloud9:environment',
            'Value': '7068281702fb4ddcaca1489b2a717f8f'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Security group for all nodes in the cluster',
        'GroupName':
        'armory2-poc-worker-nodes-NodeSecurityGroup-1II31JEC4VUPX',
        'IpPermissions': [{
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Allow pods to communicate with the cluster API Server',
                'GroupId': 'sg-05d4c8baf13162914',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-04b2e85f273796032',
        'IpPermissionsEgress': [{
            'FromPort':
            1025,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'Description':
                'Allow the cluster control plane to communicate with worker Kubelet and pods',
                'GroupId': 'sg-05d4c8baf13162914',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Allow the cluster control plane to communicate with pods running extension API servers on port 443',
                'GroupId': 'sg-05d4c8baf13162914',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'NodeSecurityGroup'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/armory2-poc-worker-nodes/a8f72970-1fb6-11e9-9555-02035744c0fa'
        }, {
            'Key': 'TagExtra',
            'Value': 'eks-learn'
        }, {
            'Key': 'kubernetes.io/cluster/armory2-poc',
            'Value': 'owned'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'armory2-poc-worker-nodes'
        }],
        'VpcId':
        'vpc-07320a17be9bda61c'
    }, {
        'Description':
        'eligibilitySB',
        'GroupName':
        'eligibilitySB',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-04fdcdb9b38b3d856',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbdef1'
        }, {
            'Key': 'Name',
            'Value': 'eligibilitySB'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbdef1/5ee996c0-e6c6-11e8-94ad-02e4b221489c'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eligibilitySB'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Security group for Kubernetes ELB a90c519d22a3c11e987910a03e1ddc11 (poc-dev/devmanifest-spin-helm-demo)',
        'GroupName':
        'k8s-elb-a90c519d22a3c11e987910a03e1ddc11',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-050afc7ad844ac081',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/armory3-poc',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-07320a17be9bda61c'
    }, {
        'Description':
        'Security group for Kubernetes ELB a2d0bcc0a558311e99a350a13514bf23 (splunk/splunkalb)',
        'GroupName':
        'k8s-elb-a2d0bcc0a558311e99a350a13514bf23',
        'IpPermissions': [{
            'FromPort': 8000,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8000,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-05142f1df4e16223b',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/srt-poc',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'EKS control plane sg for spinnaker poc',
        'GroupName':
        'eks-spinnaker-poc-control-plane',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-052a060da2ccea770',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'eks-spinnaker-poc-control-plane'
        }, {
            'Key': 'Owner',
            'Value': 'matthew.richardson@sony.com'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'eibRouterENP',
        'GroupName':
        'eibRouterENP',
        'IpPermissions': [{
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '166.23.10.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 8443,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.215.94.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8443,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.211.125.24/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-05674ad9d9404d6e8',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibRouterENP'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbENPdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-eibrouter'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbENPdef1/9dadcbd0-b082-11e8-bdd5-025f28dd83ba'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'EC2 Instance Security Group created by Entanglement',
        'GroupName':
        'app1-sg-teststack-EtmESpintentanglementapp1-EFZ8UT4EC8U1',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'Entanglement rule for EtmESpintentanglementapp1',
                'GroupId': 'sg-0568226f2eb3a8b48',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            53,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp':
                '8.8.8.0/24',
                'Description':
                'Entanglement rule for EtmESpintentanglementapp1'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            53,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0568226f2eb3a8b48',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp':
                '127.0.0.1/32',
                'Description':
                'Entanglement rule for EtmESpintentanglementapp1'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65335,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/app1-sg-teststack/86383a40-729b-11e9-bb0f-06cbb9434982'
        }, {
            'Key': 'Service',
            'Value': 'EtmESpint_entanglementapp1_472973657150'
        }, {
            'Key': 'Environment',
            'Value': 'E'
        }, {
            'Key': 'PCI Scope',
            'Value': 'CAT2'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'app1-sg-teststack'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'EtmESpintentanglementapp1'
        }, {
            'Key': 'Git Repo',
            'Value': 'https://github.sie.sony.com/SIE/entanglementapp1'
        }, {
            'Key': 'GitManifest',
            'Value': 'manifests/app1manifest.yml'
        }, {
            'Key': 'Name',
            'Value': 'Etm-Spint-E-entanglementapp1'
        }, {
            'Key': 'Git tag',
            'Value': '1.0.0'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'Security group for all nodes in the cluster',
        'GroupName':
        'harness-poc-worker-nodes-NodeSecurityGroup-1IIPZJUZ9NXZP',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '43.148.20.0/22'
            }, {
                'CidrIp': '43.148.0.0/20'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-059906b6458156e83',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'harness-poc-worker-nodes'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'NodeSecurityGroup'
        }, {
            'Key': 'kubernetes.io/cluster/harness-poc',
            'Value': 'owned'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/harness-poc-worker-nodes/e6bee850-18e1-11e9-bdaf-0af0816e310e'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'ktang testing',
        'GroupName':
        'ktang-sg-nav-sandbox',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-05998738f94af92f9',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'ktang-sg-nav-sandbox'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'oltpSB',
        'GroupName':
        'oltpSB',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-059a0395223e2a7c7',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbdef1/5ee996c0-e6c6-11e8-94ad-02e4b221489c'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'oltpSB'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbdef1'
        }, {
            'Key': 'Name',
            'Value': 'oltpSB'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'aerospikeNP',
        'GroupName':
        'aerospikeNP',
        'IpPermissions': [{
            'FromPort':
            3000,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.215.92.92/32'
            }, {
                'CidrIp': '10.215.92.91/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3000,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-05c03e7df816966a0',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbProd-NPdef1/e6d35cf0-c52a-11e8-9fe0-0a3c8425d484'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbProd-NPdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-aerospike'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'aerospikeNP'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceamazonpayserverEMGMT',
        'GroupName':
        'commerceamazonpayserverEMGMT',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-05d2fc4db9bae546a',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceamazonpayserverEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceamazonpayserverEMGMT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Security group for all nodes in the cluster',
        'GroupName':
        'armory3-poc-work-nodes-NodeSecurityGroup-XM8HGJTEPTZ6',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-050afc7ad844ac081',
                'UserId': '472973657150'
            }, {
                'Description': 'Allow node to communicate with each other',
                'GroupId': 'sg-05d4c8baf13162914',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-06a380a86073b65ac',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-085eb6b7bac099444',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-0a8b2383061e11de8',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-0b21d3d8d5713d821',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': 'SSH from SIE Offices'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            1025,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'Description':
                'Allow worker Kubelets and pods to receive communication from the cluster control plane',
                'GroupId': 'sg-04b2e85f273796032',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Allow pods running extension API servers on port 443 to receive communication from cluster control plane',
                'GroupId': 'sg-04b2e85f273796032',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-05d4c8baf13162914',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/armory3-poc-work-nodes/7f0873e0-2000-11e9-9a31-02cb67b6aa16'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'armory3-poc-work-nodes'
        }, {
            'Key': 'kubernetes.io/cluster/armory3-poc',
            'Value': 'owned'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'NodeSecurityGroup'
        }],
        'VpcId':
        'vpc-07320a17be9bda61c'
    }, {
        'Description':
        'sie-office-inbound',
        'GroupName':
        'sie-office-inbound',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': ''
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-05ee2a425c9697549',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'EC2 Instance Security Group created by Entanglement',
        'GroupName':
        'app5-sg-teststack-EtmESpintentanglementapp5-1DZY06WQXYZF5',
        'IpPermissions': [{
            'FromPort':
            1521,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            1521,
            'UserIdGroupPairs': [{
                'Description':
                'Entanglement rule for EtmESpintentanglementapp5',
                'GroupId': 'sg-0568226f2eb3a8b48',
                'UserId': '472973657150'
            }, {
                'Description':
                'Entanglement rule for EtmESpintentanglementapp5',
                'GroupId': 'sg-061ef9f386035246c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'Entanglement rule for EtmESpintentanglementapp5',
                'GroupId': 'sg-05fc8c5b3fb37fe0d',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-05fc8c5b3fb37fe0d',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp':
                '127.0.0.1/32',
                'Description':
                'Entanglement rule for EtmESpintentanglementapp5'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65335,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'Etm-Spint-E-entanglementapp5'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'EtmESpintentanglementapp5'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'app5-sg-teststack'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/app5-sg-teststack/3ecf8340-767c-11e9-b0d6-0ad5109330ec'
        }, {
            'Key': 'PCI Scope',
            'Value': 'CAT2'
        }, {
            'Key': 'Git Repo',
            'Value': 'entanglement_repo'
        }, {
            'Key': 'Environment',
            'Value': 'E'
        }, {
            'Key': 'Service',
            'Value': 'EtmESpint_entanglementapp5_472973657150'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'voucherSB',
        'GroupName':
        'voucherSB',
        'IpPermissions': [{
            'FromPort':
            8443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0e1ab52af63f836e5',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            11211,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            11211,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-04fdcdb9b38b3d856',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort': 443,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.211.54.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0617e8c8fb0f792c3',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbdef1/5ee996c0-e6c6-11e8-94ad-02e4b221489c'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'voucherSB'
        }, {
            'Key': 'Name',
            'Value': 'voucherSB'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'EC2 Instance Security Group created by Entanglement',
        'GroupName':
        'app2-sg-teststack-EtmESpintentanglementapp2-XW4JRQ3K626X',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'Description':
                'Entanglement rule for EtmESpintentanglementapp2',
                'GroupId': 'sg-061ef9f386035246c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp':
                '10.215.0.0/24',
                'Description':
                'Entanglement rule for EtmESpintentanglementapp2'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-061ef9f386035246c',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp':
                '127.0.0.1/32',
                'Description':
                'Entanglement rule for EtmESpintentanglementapp2'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65335,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'Etm-Spint-E-entanglementapp2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/app2-sg-teststack/ff0d1f00-729e-11e9-9d6a-02035744c0fa'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'app2-sg-teststack'
        }, {
            'Key': 'PCI Scope',
            'Value': 'CAT2'
        }, {
            'Key': 'Environment',
            'Value': 'E'
        }, {
            'Key': 'Git Repo',
            'Value': 'entanglement_repo'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'EtmESpintentanglementapp2'
        }, {
            'Key': 'Service',
            'Value': 'EtmESpint_entanglementapp2_472973657150'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'commercepmpbserverEMGMT',
        'GroupName':
        'commercepmpbserverEMGMT',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0630fcc9038595fa8',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercepmpbserverEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercepmpbserverEMGMT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'eibElbSandbox',
        'GroupName':
        'eibElbSandbox',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0637967a93276f0e5',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibElbSandbox'
        }, {
            'Key': 'Name',
            'Value': 'nav-eibelb'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-def1/07371630-c8fa-11e8-9131-50a68a0e322a'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-def1'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Security group for all nodes in the cluster',
        'GroupName':
        'srt-poc-worker-nodes-NodeSecurityGroup-1PP1CL94460V',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-02a63ca123c62fce8',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-03b0334ae15c99267',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-05142f1df4e16223b',
                'UserId': '472973657150'
            }, {
                'Description': 'Allow node to communicate with each other',
                'GroupId': 'sg-0646e26bcfc907fb2',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-7b78520a',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            1025,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'Description':
                'Allow worker Kubelets and pods to receive communication from the cluster control plane',
                'GroupId': 'sg-0fe9c00568197171b',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Allow pods running extension API servers on port 443 to receive communication from cluster control plane',
                'GroupId': 'sg-0fe9c00568197171b',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0646e26bcfc907fb2',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Owner',
            'Value': 'chris.barbour@sony.com'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'srt-poc-worker-nodes'
        }, {
            'Key': 'BillTo',
            'Value': 'Navigator'
        }, {
            'Key': 'Name',
            'Value': 'srt-poc-kubectl'
        }, {
            'Key': 'Service',
            'Value': 'Hyperloop'
        }, {
            'Key': 'Team',
            'Value': 'SRT'
        }, {
            'Key': 'Environment',
            'Value': 'sandbox'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'NodeSecurityGroup'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/srt-poc-worker-nodes/4348ad90-4a01-11e9-a7e7-06aa0dcac8ba'
        }, {
            'Key': 'kubernetes.io/cluster/srt-poc',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Security group for Kubernetes ELB a7a76e24a203111e987910a03e1ddc11 (ingress-nginx/ingress-nginx)',
        'GroupName':
        'k8s-elb-a7a76e24a203111e987910a03e1ddc11',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-06a380a86073b65ac',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/armory3-poc',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-07320a17be9bda61c'
    }, {
        'Description':
        'Slave group for Elastic MapReduce created on 2017-10-04T01:13:49.807Z',
        'GroupName':
        'ElasticMapReduce-Slave-Private',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-06bb0d7b',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-7ca41201',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-39b80e44',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            0,
            'IpProtocol':
            'udp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-06bb0d7b',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-7ca41201',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            -1,
            'IpProtocol':
            'icmp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            -1,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-06bb0d7b',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-7ca41201',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-06bb0d7b',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [{
                'CidrIpv6': '::/0'
            }],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Created from the RDS Management Console: 2019/04/30 15:31:20',
        'GroupName':
        'rds-launch-wizard',
        'IpPermissions': [{
            'FromPort': 3306,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3306,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-06c073e9ab84586ec',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'EC2 Instance Security Group created by Entanglement',
        'GroupName':
        'app4-sg-teststack-EtmESpintentanglementapp4-1J8JN7739A1F9',
        'IpPermissions': [{
            'FromPort':
            1521,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            1521,
            'UserIdGroupPairs': [{
                'Description':
                'Entanglement rule for EtmESpintentanglementapp4',
                'GroupId': 'sg-09356d729c2c2c28f',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'Entanglement rule for EtmESpintentanglementapp4',
                'GroupId': 'sg-06d83ed1a616b44aa',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-06d83ed1a616b44aa',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp':
                '127.0.0.1/32',
                'Description':
                'Entanglement rule for EtmESpintentanglementapp4'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65335,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'app4-sg-teststack'
        }, {
            'Key': 'Git Repo',
            'Value': 'entanglement_repo'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/app4-sg-teststack/c29bd5b0-729f-11e9-b90a-0a3d4b08165a'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'EtmESpintentanglementapp4'
        }, {
            'Key': 'Name',
            'Value': 'Etm-Spint-E-entanglementapp4'
        }, {
            'Key': 'Service',
            'Value': 'EtmESpint_entanglementapp4_472973657150'
        }, {
            'Key': 'PCI Scope',
            'Value': 'CAT2'
        }, {
            'Key': 'Environment',
            'Value': 'E'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'wayne_access_sandbox',
        'GroupName':
        'wayne_access_sandbox',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': ''
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            -1,
            'IpProtocol':
            'icmp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': ''
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            -1,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-06fdfa915b3792f47',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'wayne_access_sandbox'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'consolenotificationsPL',
        'GroupName':
        'consolenotificationsPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-07411a79',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'consolenotificationsPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-consolenotifications'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Created from the RDS Management Console: 2019/05/01 21:56:42',
        'GroupName':
        'rds-launch-wizard-2',
        'IpPermissions': [{
            'FromPort': 3306,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3306,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-076ac80a3ee1bb8fc',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'apm-sandbox',
        'GroupName':
        'apm-sandbox',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-078145646768d3a0f',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort': 8080,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8081,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5001,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22'
            }, {
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5001,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-078145646768d3a0f',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'nagios secgroup',
        'GroupName':
        'Ritenour-CFN-SG-increase-test-testbuild2-63J126E6QJSY',
        'IpPermissions': [{
            'FromPort': 17,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 17,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 13,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 13,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 38,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 38,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 59,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 59,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 34,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 34,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 41,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 41,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 2,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 2,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 27,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 27,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 4,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 4,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 23,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 23,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 48,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 48,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 55,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 55,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 6,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 6,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 30,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 30,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 51,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 51,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 8,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 18,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 18,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 14,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 14,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 37,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 37,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 10,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 10,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 33,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 33,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 44,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 44,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 40,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 40,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 26,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 26,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 45,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 45,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 49,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 49,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 56,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 56,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 52,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 52,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 19,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 19,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 11,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 11,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 9,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 9,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 15,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 15,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 36,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 36,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 32,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 32,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 43,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 43,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 60,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 60,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 1,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 1,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 29,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 29,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 21,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 21,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 25,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 25,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 46,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 46,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 3,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 57,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 57,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 5,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 7,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 7,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 16,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 16,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 12,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 12,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 35,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 35,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 39,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 39,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 31,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 31,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 42,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 42,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 28,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 28,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 24,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 24,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 47,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 47,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 20,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 20,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 58,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 58,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 54,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 54,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 50,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 50,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-07ffa8768d87cc0ad',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'RitenourCFNTest2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'testbuild2'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'Ritenour-CFN-SG-increase-test'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/Ritenour-CFN-SG-increase-test/bebdd370-f825-11e8-93fc-50a68a0e328e'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'Security group for Kubernetes ELB ae6cc9b642a3e11e987910a03e1ddc11 (poc-prod/prodmanifest-spin-helm-demo)',
        'GroupName':
        'k8s-elb-ae6cc9b642a3e11e987910a03e1ddc11',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-085eb6b7bac099444',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/armory3-poc',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-07320a17be9bda61c'
    }, {
        'Description':
        'commercebatchtoolESPINT',
        'GroupName':
        'ESPINTsgdef2-commercebatchtoolESPINT-1ECBBX23PT9ID',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-086a0476',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebatchtoolESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercebatchtoolESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'almilli-desktop',
        'GroupName':
        'almilli-desktop',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-087ce3b85891f0b4c',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-07320a17be9bda61c'
    }, {
        'Description':
        'eks test',
        'GroupName':
        'nav-sandbox-sieoffice-eks',
        'IpPermissions': [{
            'FromPort': 5439,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5439,
            'UserIdGroupPairs': []
        }, {
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '173.230.196.15/32'
            }, {
                'CidrIp': '173.230.196.25/32'
            }, {
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '43.148.16.0/22'
            }, {
                'CidrIp': '43.148.20.0/22'
            }, {
                'CidrIp': '43.148.24.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-08f9aea2c666bcdf0',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-07320a17be9bda61c'
    }, {
        'Description':
        ' Default EQANginX MT Grc',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-mtDefaultNGXEQA-7VXRTULRE6G0',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-810d68ff',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-880065f6',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-810d68ff',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-880065f6',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-810d68ff',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-880065f6',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-09026777',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier External ELB for Default EQA'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtDefaultNGXEQA'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'Name',
            'Value': 'mtDefaultNgxEQA'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'vouchertransferservers2',
        'GroupName':
        'vouchertransferservers2',
        'IpPermissions': [{
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '65.112.217.8/32'
            }, {
                'CidrIp': '139.131.76.245/32'
            }, {
                'CidrIp': '173.230.196.15/32'
            }, {
                'CidrIp': '70.47.187.20/32'
            }, {
                'CidrIp': '10.241.96.0/20'
            }, {
                'CidrIp': '64.37.174.20/32'
            }, {
                'CidrIp': '160.33.45.152/32'
            }, {
                'CidrIp': '217.18.16.0/24'
            }, {
                'CidrIp': '63.148.46.24/32'
            }, {
                'CidrIp': '192.16.134.105/32'
            }, {
                'CidrIp': '10.242.128.0/20'
            }, {
                'CidrIp': '80.88.36.195/32'
            }, {
                'CidrIp': '10.242.144.0/20'
            }, {
                'CidrIp': '160.33.178.254/32'
            }, {
                'CidrIp': '10.242.160.0/20'
            }, {
                'CidrIp': '217.18.20.0/24'
            }, {
                'CidrIp': '160.33.45.151/32'
            }, {
                'CidrIp': '66.77.174.166/32'
            }, {
                'CidrIp': '160.33.176.254/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0921d402ff2d8d63f',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-globaldef/0cdf13f0-ce4d-11e8-8913-0a578203aa12'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'vouchertransferservers2'
        }, {
            'Key': 'Name',
            'Value': 'vouchertransferservers2'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-globaldef'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'EC2 Instance Security Group created by Entanglement',
        'GroupName':
        'app3-sg-teststack-EtmESpintentanglementapp3-15ID8VVT1ZRC5',
        'IpPermissions': [{
            'FromPort':
            1521,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            1521,
            'UserIdGroupPairs': [{
                'Description':
                'Entanglement rule for EtmESpintentanglementapp3',
                'GroupId': 'sg-0568226f2eb3a8b48',
                'UserId': '472973657150'
            }, {
                'Description':
                'Entanglement rule for EtmESpintentanglementapp3',
                'GroupId': 'sg-06d83ed1a616b44aa',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'Entanglement rule for EtmESpintentanglementapp3',
                'GroupId': 'sg-09356d729c2c2c28f',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Entanglement rule for EtmESpintentanglementapp3',
                'GroupId': 'sg-061ef9f386035246c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-09356d729c2c2c28f',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp':
                '127.0.0.1/32',
                'Description':
                'Entanglement rule for EtmESpintentanglementapp3'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65335,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'Etm-Spint-E-entanglementapp3'
        }, {
            'Key': 'Environment',
            'Value': 'E'
        }, {
            'Key': 'Git tag',
            'Value': '1.0.0'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'app3-sg-teststack'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'EtmESpintentanglementapp3'
        }, {
            'Key': 'GitManifest',
            'Value': 'manifests/app3manifest.yml'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/app3-sg-teststack/4f306910-729f-11e9-9bc4-0268a47876ba'
        }, {
            'Key': 'PCI Scope',
            'Value': 'CAT2'
        }, {
            'Key': 'Git Repo',
            'Value': 'https://github.sie.sony.com/SIE/entanglementapp3'
        }, {
            'Key': 'Service',
            'Value': 'EtmESpint_entanglementapp3_472973657150'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'managed LoadBalancer securityGroup by ALB Ingress Controller',
        'GroupName':
        '54972eaf-default-nginxserv-bc24',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp':
                '0.0.0.0/0',
                'Description':
                'Allow ingress on port 80 from 0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-09517b00e308a78b6',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/namespace',
            'Value': 'default'
        }, {
            'Key': 'kubernetes.io/ingress-name',
            'Value': 'nginx-service-ip-ingress'
        }, {
            'Key': 'kubernetes.io/cluster/test-eks3',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'sensu server Prodadmin secgroup',
        'GroupName':
        'tessg-sensuPA-I7DCBVPW3AFG',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.208.0/20'
            }, {
                'CidrIp': '10.241.192.0/21'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': []
        }, {
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-4e6db930',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            6379,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.241.192.0/21'
            }, {
                'CidrIp': '10.242.208.0/20'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            6379,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            4567,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.240/32'
            }, {
                'CidrIp': '10.242.208.0/20'
            }, {
                'CidrIp': '10.241.192.0/20'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4567,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0961b577',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key': 'Name',
            'Value': 'sensuPA'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'sensuPA'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'devicemanagementserviceESPINT',
        'GroupName':
        'ESPINTsgdef2-devicemanagementserviceESPINT-Y1C24QJ863VY',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-096a0477',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'devicemanagementserviceESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-devicemanagementserviceESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceamazonpaylistenerENP',
        'GroupName':
        'commerceamazonpaylistenerENP',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-05674ad9d9404d6e8',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-05674ad9d9404d6e8',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-09880968f13308fcf',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerceamazonpaylistener'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceamazonpaylistenerENP'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbENPdef1/9dadcbd0-b082-11e8-bdd5-025f28dd83ba'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbENPdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Allow Local',
        'GroupName':
        'Allow_Local',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22',
                'Description': 'Local Allow all'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 3307,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3307,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            3306,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '74.87.17.222/32'
            }, {
                'CidrIp': '43.148.23.174/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3306,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0992b0eabca39ea09',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'Allow_Local'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'managed instance securityGroup by ALB Ingress Controller',
        'GroupName':
        'instance-23901e39-2048game-2048ingr-6fa0',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0f7b464a9924aca54',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0a4fe68a8dbc7bb41',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/ingress-name',
            'Value': '2048-ingress'
        }, {
            'Key': 'kubernetes.io/cluster/test-eks2',
            'Value': 'owned'
        }, {
            'Key': 'kubernetes.io/namespace',
            'Value': '2048-game'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'default VPC security group',
        'GroupName':
        'default',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0a533057019c1acb8',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0a533057019c1acb8',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-07320a17be9bda61c'
    }, {
        'Description':
        'commerceamexbatchESPINT',
        'GroupName':
        'ESPINTsgdef2-commerceamexbatchESPINT-H2R9TVP07E9G',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0a690774',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerceamexbatchESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceamexbatchESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'memcachedgrcPL',
        'GroupName':
        'memcachedgrcPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0a7b2074',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'memcachedgrcPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-memcachedgrc'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'mohit',
        'GroupName':
        'mohitlocal',
        'IpPermissions': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '64.211.224.254/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0a87d67e0a5aa873f',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Security group for Kubernetes ELB adc6545a2297711e987910a03e1ddc11 (poc-dev/poc-nginx)',
        'GroupName':
        'k8s-elb-adc6545a2297711e987910a03e1ddc11',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0a8b2383061e11de8',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/armory3-poc',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-07320a17be9bda61c'
    }, {
        'Description':
        'hotmppSB',
        'GroupName':
        'hotmppSB',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0a8ff0ac0a1ade84d',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'hotmppSB'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbdef1/5ee996c0-e6c6-11e8-94ad-02e4b221489c'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'hotmppSB'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'nagios secgroup',
        'GroupName':
        'Ritenour-CFN-SG-increase-test-testbuild1-2VF95QF2D75N',
        'IpPermissions': [{
            'FromPort': 17,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 17,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 13,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 13,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 38,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 38,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 59,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 59,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 34,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 34,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 41,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 41,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 2,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 2,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 27,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 27,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 4,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 4,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 23,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 23,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 48,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 48,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 55,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 55,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 6,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 6,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 30,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 30,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 51,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 51,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 8,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 18,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 18,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 14,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 14,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 37,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 37,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 10,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 10,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 33,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 33,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 44,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 44,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 40,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 40,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 26,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 26,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 45,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 45,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 49,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 49,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 56,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 56,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 52,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 52,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 19,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 19,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 11,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 11,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 9,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 9,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 15,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 15,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 36,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 36,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 32,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 32,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 43,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 43,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 60,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 60,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 1,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 1,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 29,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 29,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 21,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 21,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 25,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 25,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 46,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 46,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 3,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 57,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 57,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 5,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 7,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 7,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 16,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 16,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 12,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 12,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 35,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 35,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 39,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 39,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 31,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 31,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 42,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 42,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 28,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 28,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 24,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 24,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 47,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 47,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 20,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 20,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 58,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 58,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 54,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 54,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 50,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 50,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0aa500b8000de2699',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'RitenourCFNTest1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/Ritenour-CFN-SG-increase-test/bebdd370-f825-11e8-93fc-50a68a0e328e'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'testbuild1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'Ritenour-CFN-SG-increase-test'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'paymenthubEMGMT',
        'GroupName':
        'paymenthubEMGMT',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0ae094f1b8b30e9a9',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'paymenthubEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }, {
            'Key': 'Name',
            'Value': 'nav-paymenthubEMGMT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'tsvefsEMGMT',
        'GroupName':
        'tsvefsEMGMT',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0ae4769fc0e6708f1',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'tsvefsEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }, {
            'Key': 'Name',
            'Value': 'nav-tsvefsEMGMT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Security group for Kubernetes ELB a85e7e6e9201411e987910a03e1ddc11 (poc/poc-nginx)',
        'GroupName':
        'k8s-elb-a85e7e6e9201411e987910a03e1ddc11',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0b21d3d8d5713d821',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/armory3-poc',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-07320a17be9bda61c'
    }, {
        'Description':
        'eks armory poc work node',
        'GroupName':
        'eks-armory-poc-work-node',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'Description': 'Worker node security group',
                'GroupId': 'sg-038721e5576cefd14',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            1025,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'Description': 'Control plane security group',
                'GroupId': 'sg-0fe9c00568197171b',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description': 'Control plane security group',
                'GroupId': 'sg-0fe9c00568197171b',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0b2292778ceb9d6f6',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'eks-armory-poc-worker-node'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'to test ssl',
        'GroupName':
        'testssl',
        'IpPermissions': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0b30eb52dab7b732c',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Communication between the control plane and worker node groups',
        'GroupName':
        'eksctl-aws-dev303-workshop-cluster-ControlPlaneSecurityGroup-XO63U4SKM7Y8',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0b513c72409b63d8a',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [{
                'CidrIpv6': '::/0'
            }],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'ControlPlaneSecurityGroup'
        }, {
            'Key':
            'Name',
            'Value':
            'eksctl-aws-dev303-workshop-cluster/ControlPlaneSecurityGroup'
        }, {
            'Key': 'eksctl.cluster.k8s.io/v1alpha1/cluster-name',
            'Value': 'aws-dev303-workshop'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/eksctl-aws-dev303-workshop-cluster/5d6787f0-f1b9-11e8-b1b6-0254f5c7f298'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'eksctl-aws-dev303-workshop-cluster'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'managed instance securityGroup by ALB Ingress Controller',
        'GroupName':
        'instance-23901e39-2048game-2048ipin-ccc3',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-041b1cd91bc454eee',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0b60db0d8adb3156a',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/test-eks2',
            'Value': 'owned'
        }, {
            'Key': 'kubernetes.io/namespace',
            'Value': '2048-game'
        }, {
            'Key': 'kubernetes.io/ingress-name',
            'Value': '2048-ip-ingress'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'NP  EIB CLient to EIB Router',
        'GroupName':
        'eibElbClientNP',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0b86d875',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ELB-ErtrProdLine'
        }, {
            'Key': 'Name',
            'Value': 'eibElbClientNP'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibElbClientNP'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ELB-ErtrProdLine/d7bb6d50-4c41-11e8-a66a-50a68af3968d'
        }, {
            'Key': 'Description',
            'Value': 'NP EIB ELB client security group'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Security group for all nodes in the cluster',
        'GroupName':
        'armory-poc-worker-nodes-NodeSecurityGroup-UWDUAK9Y5NY9',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'Description': 'Allow node to communicate with each other',
                'GroupId': 'sg-0bb3b5c2cdb36a7d9',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            1025,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'Description':
                'Allow worker Kubelets and pods to receive communication from the cluster control plane',
                'GroupId': 'sg-0d265469a35fe1e5a',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Allow pods running extension API servers on port 443 to receive communication from cluster control plane',
                'GroupId': 'sg-0d265469a35fe1e5a',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0bb3b5c2cdb36a7d9',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'EKS-Cluster',
            'Value': 'armory-poc'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'NodeSecurityGroup'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/armory-poc-worker-nodes/bb0845b0-1f5a-11e9-aa59-06ba2e5d70ae'
        }, {
            'Key': 'kubernetes.io/cluster/armory-poc',
            'Value': 'owned'
        }, {
            'Key': 'TagExtra',
            'Value': 'eks-test'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'armory-poc-worker-nodes'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'SECURITY_BLOCK',
        'GroupName':
        'SECURITY_BLOCK',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0bf7e984ffccfb08f',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '127.0.0.0/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'nagios secgroup',
        'GroupName':
        'Ritenour-CFN-SG-increase-test-testbuild3-19CMFKV1B20LU',
        'IpPermissions': [{
            'FromPort': 17,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 17,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 13,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 13,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 38,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 38,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 59,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 59,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 34,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 34,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 41,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 41,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 2,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 2,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 27,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 27,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 4,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 4,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 23,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 23,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 48,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 48,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 55,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 55,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 6,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 6,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 30,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 30,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 51,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 51,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 8,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 18,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 18,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 14,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 14,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 37,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 37,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 10,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 10,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 33,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 33,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 44,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 44,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 40,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 40,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 26,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 26,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 45,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 45,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 49,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 49,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 56,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 56,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 52,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 52,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 19,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 19,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 11,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 11,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 9,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 9,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 15,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 15,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 36,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 36,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 32,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 32,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 43,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 43,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 60,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 60,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 1,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 1,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 29,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 29,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 21,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 21,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 25,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 25,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 46,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 46,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 3,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 57,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 57,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 5,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 7,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 7,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 16,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 16,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 12,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 12,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 35,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 35,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 39,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 39,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 31,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 31,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 42,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 42,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 28,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 28,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 24,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 24,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 47,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 47,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 20,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 20,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 58,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 58,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 54,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 54,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 50,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 50,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0c3577147505e9ba1',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'Ritenour-CFN-SG-increase-test'
        }, {
            'Key': 'Name',
            'Value': 'RitenourCFNTest3'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/Ritenour-CFN-SG-increase-test/bebdd370-f825-11e8-93fc-50a68a0e328e'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'testbuild3'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'commerceproxyacsPL',
        'GroupName':
        'commerceproxyacsPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0c7e2572',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerceproxyacs'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceproxyacsPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'shardmanagementserviceEMGMT',
        'GroupName':
        'EMGMTdef4-shardmanagementserviceEMGMT-4X4Q9L7WFSND',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0c978c6b14867a693',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }, {
            'Key': 'Name',
            'Value': 'nav-shardmanagementserviceEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'shardmanagementserviceEMGMT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Cluster communication with worker nodes',
        'GroupName':
        'armory-eks-vpc-ControlPlaneSecurityGroup-GY52NAP36HS7',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0cd158e18090efa03',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [{
                'CidrIpv6': '::/0'
            }],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'armory-eks-vpc'
        }, {
            'Key': 'TagExtra',
            'Value': 'eks-learn'
        }, {
            'Key': 'EKSCluserName',
            'Value': 'armory-spinnaker'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/armory-eks-vpc/1d74f4a0-1fb0-11e9-abf3-027a46c6b5a2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'ControlPlaneSecurityGroup'
        }],
        'VpcId':
        'vpc-07320a17be9bda61c'
    }, {
        'Description':
        'eks-armory-poc-control-plane',
        'GroupName':
        'eks-armory-poc-control-plane',
        'IpPermissions': [{
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description': 'Worker node security group',
                'GroupId': 'sg-038721e5576cefd14',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow pods to communicate with the cluster API Server',
                'GroupId': 'sg-059906b6458156e83',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow pods to communicate with the cluster API Server',
                'GroupId': 'sg-0bb3b5c2cdb36a7d9',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0d265469a35fe1e5a',
        'IpPermissionsEgress': [{
            'FromPort':
            1025,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'Description': 'Worker node security group',
                'GroupId': 'sg-038721e5576cefd14',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow the cluster control plane to communicate with worker Kubelet and pods',
                'GroupId': 'sg-059906b6458156e83',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow the cluster control plane to communicate with worker Kubelet and pods',
                'GroupId': 'sg-0bb3b5c2cdb36a7d9',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Allow the cluster control plane to communicate with pods running extension API servers on port 443',
                'GroupId': 'sg-059906b6458156e83',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow the cluster control plane to communicate with pods running extension API servers on port 443',
                'GroupId': 'sg-0bb3b5c2cdb36a7d9',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'eks-armory-poc-control-plane'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'eveaggregateSB',
        'GroupName':
        'eveaggregateSB',
        'IpPermissions': [{
            'FromPort':
            1521,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            1521,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-059a0395223e2a7c7',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0d2927de86ec6878e',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbdef1/5ee996c0-e6c6-11e8-94ad-02e4b221489c'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eveaggregateSB'
        }, {
            'Key': 'Name',
            'Value': 'eveaggregateSB'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbdef1'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Created from the RDS Management Console: 2019/04/30 15:35:13',
        'GroupName':
        'rds-launch-wizard-1',
        'IpPermissions': [{
            'FromPort': 3306,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3306,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0d4620f7d4c2497c0',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'evepurchasePL',
        'GroupName':
        'evepurchasePL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0d7b2073',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'evepurchasePL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-evepurchase'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Security group for all nodes in the cluster',
        'GroupName':
        'hlp-jks-poc-worker-nodes-NodeSecurityGroup-J3XII2N3C1SG',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'Description': 'Allow node to communicate with each other',
                'GroupId': 'sg-0d7ccd6e023b37adf',
                'UserId': '472973657150'
            }, {
                'Description': 'Communication from sandbox',
                'GroupId': 'sg-df3acea5',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            1025,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'Description':
                'Allow worker Kubelets and pods to receive communication from the cluster control plane',
                'GroupId': 'sg-0fe9c00568197171b',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Allow pods running extension API servers on port 443 to receive communication from cluster control plane',
                'GroupId': 'sg-0fe9c00568197171b',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0d7ccd6e023b37adf',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'NodeSecurityGroup'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'hlp-jks-poc-worker-nodes'
        }, {
            'Key': 'kubernetes.io/cluster/hlp-jks-poc',
            'Value': 'owned'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/hlp-jks-poc-worker-nodes/c7740560-23f5-11e9-b570-028146f68342'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Slave group for Elastic MapReduce created on 2017-10-03T19:12:23.698Z',
        'GroupName':
        'ElasticMapReduce-slave',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0d893e70',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-f175c28c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            0,
            'IpProtocol':
            'udp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0d893e70',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-f175c28c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            -1,
            'IpProtocol':
            'icmp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            -1,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0d893e70',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-f175c28c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Allow pods to communicate with the cluster API Server',
                'GroupId': 'sg-012cec7c5e47afba1',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow pods to communicate with the cluster API Server',
                'GroupId': 'sg-01e98a00647923a10',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0d893e70',
        'IpPermissionsEgress': [{
            'FromPort':
            1025,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'Description':
                'Allow the cluster control plane to communicate with worker Kubelet and pods',
                'GroupId': 'sg-012cec7c5e47afba1',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow the cluster control plane to communicate with worker Kubelet and pods',
                'GroupId': 'sg-01e98a00647923a10',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Allow the cluster control plane to communicate with pods running extension API servers on port 443',
                'GroupId': 'sg-012cec7c5e47afba1',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow the cluster control plane to communicate with pods running extension API servers on port 443',
                'GroupId': 'sg-01e98a00647923a10',
                'UserId': '472973657150'
            }]
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Created from the RDS Management Console: 2019/03/20 22:47:50',
        'GroupName':
        'rds-launch-wizard-4',
        'IpPermissions': [{
            'FromPort': 5432,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5432,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0dc60d235564e37b8',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'navigatorauthgatewayEMGMT',
        'GroupName':
        'EMGMTdef4-navigatorauthgatewayEMGMT-OJVOYVDW16AF',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0dd86a3bbf08448de',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigatorauthgatewayEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatorauthgatewayEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'eibRouterSandbox',
        'GroupName':
        'eibRouterSandbox',
        'IpPermissions': [{
            'FromPort':
            1521,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            1521,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-062703a54cfe64654',
                'PeeringStatus': 'deleted',
                'VpcId': 'vpc-970b3af3'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0df4581241da97c0a',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-062703a54cfe64654',
                'PeeringStatus': 'deleted',
                'VpcId': 'vpc-970b3af3'
            }]
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-def1/07371630-c8fa-11e8-9131-50a68a0e322a'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibRouterSandbox'
        }, {
            'Key': 'Name',
            'Value': 'nav-eibrouter'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-def1'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commerceadyenresponderESPINT',
        'GroupName':
        'ESPINTsgdef1-commerceadyenresponderESPINT-1U1NWIGQJE1NH',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commerceadyenresponderESPINT',
                'GroupId': 'sg-49147a37',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0e127c70',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerce-adyen-responder'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceadyenresponderESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'accountSB',
        'GroupName':
        'accountSB',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0e1ab52af63f836e5',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'accountSB'
        }, {
            'Key': 'Name',
            'Value': 'accountSB'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbdef1/5ee996c0-e6c6-11e8-94ad-02e4b221489c'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Security group for Kubernetes ELB ab13756b7557b11e9bcc602d07e83d44 (splunk/splunkalb)',
        'GroupName':
        'k8s-elb-ab13756b7557b11e9bcc602d07e83d44',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0e2310097602c748c',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/srt-poc',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commerceblackhawkPL',
        'GroupName':
        'commerceblackhawkPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0e7e2570',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceblackhawk'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceblackhawkPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'memcachedcommerceserverEMGMT',
        'GroupName':
        'EMGMTdef4-memcachedcommerceserverEMGMT-1AA7FSBK8LUBP',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0e979aeaf1efb82ee',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'memcachedcommerceserverEMGMT'
        }, {
            'Key': 'Name',
            'Value': 'nav-memcachedcommerceserverEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceamazonpayserverENP',
        'GroupName':
        'commerceamazonpayserverENP',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-09880968f13308fcf',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8082,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-05674ad9d9404d6e8',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9970,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9970,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-09880968f13308fcf',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.211.40.41/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 443,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.0.0/20'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0eb5caf31ce03915c',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbENPdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceamazonpayserver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceamazonpayserverENP'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbENPdef1/9dadcbd0-b082-11e8-bdd5-025f28dd83ba'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'oracleEMGMT',
        'GroupName':
        'EMGMTdef4-oracleEMGMT-1CZSYAEMNTKWJ',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0ebb02543a0706b6f',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-oracleEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'oracleEMGMT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'tsvEMGMT',
        'GroupName':
        'tsvEMGMT',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0edb4faf39c60b522',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'tsvEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'EMGMTdef4'
        }, {
            'Key': 'Name',
            'Value': 'nav-tsvEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/EMGMTdef4/5b7e09e0-c055-11e8-b884-06dcf5c4ac1e'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'priceSB',
        'GroupName':
        'priceSB',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0ee1cd70d1ceffbde',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbdef1/5ee996c0-e6c6-11e8-94ad-02e4b221489c'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbdef1'
        }, {
            'Key': 'Name',
            'Value': 'priceSB'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'priceSB'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Created from the RDS Management Console: 2019/03/21 00:33:19',
        'GroupName':
        'rds-launch-wizard-5',
        'IpPermissions': [{
            'FromPort': 5432,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5432,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0ef866102545b7bba',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'splunk-elb secgroup',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-splunkElb-1DIQB5QEK6ZB7',
        'IpPermissions': [{
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }, {
                'CidrIp': '52.10.119.198/32'
            }, {
                'CidrIp': '173.230.196.15/32'
            }, {
                'CidrIp': '43.148.20.0/22'
            }, {
                'CidrIp': '52.89.225.15/32'
            }, {
                'CidrIp': '52.43.137.246/32'
            }, {
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '43.148.16.0/22'
            }, {
                'CidrIp': '43.148.3.116/32'
            }, {
                'CidrIp': '43.148.3.115/32'
            }, {
                'CidrIp': '52.89.89.217/32'
            }, {
                'CidrIp': '52.89.176.248/32'
            }, {
                'CidrIp': '43.148.3.117/32'
            }, {
                'CidrIp': '52.42.57.219/32'
            }, {
                'CidrIp': '43.148.24.0/22'
            }, {
                'CidrIp': '173.230.196.25/32'
            }, {
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0f0f6a71',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'splunkElb'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'Name',
            'Value': 'ymtestVPC-splunk-elb'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'managed LoadBalancer securityGroup by ALB Ingress Controller',
        'GroupName':
        '23901e39-2048game-2048ingr-6fa0',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0f7b464a9924aca54',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/test-eks2',
            'Value': 'owned'
        }, {
            'Key': 'kubernetes.io/ingress-name',
            'Value': '2048-ingress'
        }, {
            'Key': 'kubernetes.io/namespace',
            'Value': '2048-game'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'notificationprocessorPL',
        'GroupName':
        'notificationprocessorPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0f7e2571',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'notificationprocessorPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-notificationprocessor'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Communication between the control plane and worker nodegroups',
        'GroupName':
        'eksctl-nav-sandbox-base-cluster-ControlPlaneSecurityGroup-CZY11Q63KCI3',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0f8197b5e57d99759',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [{
                'CidrIpv6': '::/0'
            }],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'Name',
            'Value':
            'eksctl-nav-sandbox-base-cluster/ControlPlaneSecurityGroup'
        }, {
            'Key': 'eksctl.cluster.k8s.io/v1alpha1/cluster-name',
            'Value': 'nav-sandbox-base'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'ControlPlaneSecurityGroup'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'eksctl-nav-sandbox-base-cluster'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/eksctl-nav-sandbox-base-cluster/dcbcc100-3a16-11e9-a5a0-067bdfc711c4'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'spinnaker-poc-kubectl created 2019-03-08T14:24:31.433-08:00',
        'GroupName':
        'spinnaker-poc-kubectl',
        'IpPermissions': [{
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': 'ssh from sie office'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0f85d7bf451c2f9d1',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'eks-harness-poc-control-plane',
        'GroupName':
        'eks-harness-poc-control-plane',
        'IpPermissions': [{
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description': 'Worker node security group',
                'GroupId': 'sg-038721e5576cefd14',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow pods to communicate with the cluster API Server',
                'GroupId': 'sg-0646e26bcfc907fb2',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow pods to communicate with the cluster API Server',
                'GroupId': 'sg-0d7ccd6e023b37adf',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0fe9c00568197171b',
        'IpPermissionsEgress': [{
            'FromPort':
            1025,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'Description': 'Worker node security group',
                'GroupId': 'sg-038721e5576cefd14',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow the cluster control plane to communicate with worker Kubelet and pods',
                'GroupId': 'sg-0646e26bcfc907fb2',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow the cluster control plane to communicate with worker Kubelet and pods',
                'GroupId': 'sg-0d7ccd6e023b37adf',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'Description':
                'Allow the cluster control plane to communicate with pods running extension API servers on port 443',
                'GroupId': 'sg-0646e26bcfc907fb2',
                'UserId': '472973657150'
            }, {
                'Description':
                'Allow the cluster control plane to communicate with pods running extension API servers on port 443',
                'GroupId': 'sg-0d7ccd6e023b37adf',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'eks-harness-poc-control-plane'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'eibElbENP',
        'GroupName':
        'eibElbENP',
        'IpPermissions': [{
            'FromPort': 8080,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.215.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8080,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 8081,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.211.95.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8081,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-0fef1f4b8d0f54e65',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-eibelb'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navneteng-sbENPdef1/9dadcbd0-b082-11e8-bdd5-025f28dd83ba'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibElbENP'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navneteng-sbENPdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'CassandraESPINT',
        'GroupName':
        'ESPINTsgdef1-CassandraESPINT-YA8E2YDRQ0MZ',
        'IpPermissions': [{
            'FromPort': 8443,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.211.114.33/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-10127c6e',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-Cassandra'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'CassandraESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatortaxPL',
        'GroupName':
        'navigatortaxPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-1073286e',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigatortax'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatortaxPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceptproxyPL',
        'GroupName':
        'commerceptproxyPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-107e256e',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerceptproxy'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceptproxyPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'NP  EIB Router SG accepting from EIB CLient',
        'GroupName':
        'eibElbNP',
        'IpPermissions': [{
            'FromPort':
            61616,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            61616,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0b86d875',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0b86d875',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            3900,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3900,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0b86d875',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            4300,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4300,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0b86d875',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9500,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9500,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0b86d875',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8501,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8501,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0b86d875',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            3450,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3450,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0b86d875',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0b86d875',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8500,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8500,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0b86d875',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-108bd56e',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-e987d997',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibElbNP'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ELB-ErtrProdLine/d7bb6d50-4c41-11e8-a66a-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ELB-ErtrProdLine'
        }, {
            'Key': 'Description',
            'Value': 'NP  EIB ELB security group'
        }, {
            'Key': 'Name',
            'Value': 'Eib-ELB-NP'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'grcPL',
        'GroupName':
        'grcPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-1173286f',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-grc'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'grcPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceptserverPL',
        'GroupName':
        'commerceptserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-117e256f',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceptserver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceptserverPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'SG for going to the internet (for YUM repo access etc)',
        'GroupName':
        'nav-sandbox-internet',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '76.167.174.251/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-11dc176f',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-internet'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'NginX MT Accounts',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-mtAccountsNGXENP-GTW0EN4JGDEM',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-9b37b7e5',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-e737b799',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-9b37b7e5',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-e737b799',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-9b37b7e5',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-e737b799',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-1336b66d',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtAccountsNGXENP'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Accounts prod np'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'Name',
            'Value': 'mtAccountsNgxENP'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'rsa secgroup',
        'GroupName':
        'navadmins-secgroups-f4156492-rsa-1J5ZFD9OX5QTU',
        'IpPermissions': [{
            'FromPort': 5500,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5500,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 5580,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5580,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 5550,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5550,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 5500,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5500,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-1366586e',
        'IpPermissionsEgress': [{
            'FromPort': 8443,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.19/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8443,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5500,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.70/32'
            }, {
                'CidrIp': '43.148.62.16/32'
            }, {
                'CidrIp': '43.148.4.42/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5500,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5580,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.62.16/32'
            }, {
                'CidrIp': '43.148.4.42/32'
            }, {
                'CidrIp': '43.148.33.70/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5580,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5550,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.62.16/32'
            }, {
                'CidrIp': '43.148.33.70/32'
            }, {
                'CidrIp': '43.148.4.42/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5550,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5500,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.4.42/32'
            }, {
                'CidrIp': '43.148.33.70/32'
            }, {
                'CidrIp': '43.148.62.16/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5500,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-f4156492'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-neteng-rsa'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-f4156492/4382ec70-c64b-11e7-a229-503aca41a0c5'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'rsa'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'TCP ALLOW ALL',
        'GroupName':
        'TCP ALLOW ALL ',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-1446c769',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'gcimbatch',
        'GroupName':
        'oracledependencies-gcimbatch-1UPUDT0SCTNES',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-16e88d68',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-gcimbatch'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'oracledependencies'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/oracledependencies/fc969580-4289-11e8-b529-50d5ca789eae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'gcimbatch'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'squid-proxy-elb secgroup',
        'GroupName':
        'tessg-squidProxyElb-Y84FIEZ1WVW4',
        'IpPermissions': [{
            'FromPort': 3128,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3128,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-186fbb66',
        'IpPermissionsEgress': [{
            'FromPort':
            3128,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3128,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-766fbb08',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'squidProxyElb'
        }, {
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-squid-proxy-elb'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'epayPL',
        'GroupName':
        'epayPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-19461d67',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-epay'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'epayPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ProdLine NginX MT pci',
        'GroupName':
        'mtpciNGXP',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-65603e1b',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-ce9ec0b0',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-65603e1b',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ce9ec0b0',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-199fc167',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtpciNGXP'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for pci ProdLine'
        }, {
            'Key': 'Name',
            'Value': 'mtpciNGXP'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'MtProdine'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/MtProdine/5c2d0350-4c3d-11e8-8dbe-50a68a2012ba'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'catalogPL',
        'GroupName':
        'catalogPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-1a471c64',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-catalog'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'catalogPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatornativePL',
        'GroupName':
        'navigatornativePL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-1c471c62',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatornativePL'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigatornative'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'sbtest123commerceDbProxySG',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-sbtest123commerceDbProxy-1VAPV9UYMW4SX',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-1c670262',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'sbtest123commerceDbProxy'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-sbtestcommerceDbProxy'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatorlinkPL',
        'GroupName':
        'navigatorlinkPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-1d471c63',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-navigatorlink'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatorlinkPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatormailmailerESPINT',
        'GroupName':
        'testAp26-2018YM-navigatormailmailerESPINT-D2JM8IAFVVL8',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-1e91de60',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-navigatormailmailer'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatormailmailerESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/testAp26-2018YM/072b6130-4968-11e8-a822-503aca41a08d'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'testAp26-2018YM'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'inbound rule via SG',
        'GroupName':
        'tritenour-sg-ssh-inbound',
        'IpPermissions': [{
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': [{
                'Description': '',
                'GroupId': 'sg-0229e87c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-1f26e761',
        'IpPermissionsEgress': [],
        'Tags': [{
            'Key': 'Name',
            'Value': 'sshinbound'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'memcachedautobotPL',
        'GroupName':
        'memcachedautobotPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-1f471c61',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-memcachedautobot'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'memcachedautobotPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'testaccountsclient SG',
        'GroupName':
        'GroupDef-accounts-1PUWNNEAUANHU',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-2aa72d54',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-2aa72d54',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-2cba3052',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-20159e5e',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-testaccounts'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'GroupDef'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/GroupDef/344dc9f0-3eeb-11e8-8ecb-503ac9ec2435'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'accounts'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'LBA_tester_public_jenkins_v2',
        'GroupName':
        'LBA_tester_public_jenkins_v2',
        'IpPermissions': [{
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-28febd58',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'LBA-Tester_public_jenkins_v2'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        ' EMGTExternal MT EIB EMGT',
        'GroupName':
        'mtAccountMGMTYML-mtAccountsExtElbEMGMT-M88LADYINHGN',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-294ad757',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d34ad7ad',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Name',
            'Value': 'mtAccountsExtElbEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtAccountsExtElbEMGMT'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Accounts EMGMT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatortaxefsESPINT',
        'GroupName':
        'ESPINTsgdef1-navigatortaxefsESPINT-1SO0ERTNIX9W5',
        'IpPermissions': [{
            'FromPort':
            2049,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            2049,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for navigatortaxefsESPINT',
                'GroupId': 'sg-bc6907c2',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for navigatortaxefsESPINT',
                'GroupId': 'sg-f266088c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2a157b54',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatortaxefsESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigator-tax-efs'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'testtransactionclient SG',
        'GroupName':
        'GroupDefOLTP-transaction-I42YXXN94482',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-2cba3052',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-91a62cef',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2aa72d54',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-testtransaction'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'GroupDefOLTP'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/GroupDefOLTP/8369b9e0-3f5e-11e8-9027-503ac9841afd'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'transaction'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'hazelcastESPINT',
        'GroupName':
        'ESPINTsgdef1-hazelcastESPINT-7Q4O9FXA7XN8',
        'IpPermissions': [{
            'FromPort':
            5705,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5705,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for hazelcastESPINT',
                'GroupId': 'sg-e9137d97',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            5710,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5710,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for hazelcastESPINT',
                'GroupId': 'sg-81147aff',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2c157b52',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'Name',
            'Value': 'nav-hazelcast'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'hazelcastESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'paymentmanageradminPL',
        'GroupName':
        'paymentmanageradminPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2c712a52',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-paymentmanageradmin'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'paymentmanageradminPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'memcachePL',
        'GroupName':
        'memcachePL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2c7d2652',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'memcachePL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-memcache'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceDbProxySG',
        'GroupName':
        'GroupDefOLTP-commerceDbProxy-2X9K1OK3FGJG',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2cba3052',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'GroupDefOLTP'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-testcommerceDbProxy'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceDbProxy'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/GroupDefOLTP/8369b9e0-3f5e-11e8-9027-503ac9841afd'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceauthserverESPINT',
        'GroupName':
        'ESPINTsgdef1-commerceauthserverESPINT-1NN2R389TS0U9',
        'IpPermissions': [{
            'FromPort':
            3400,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3400,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commerceauthserverESPINT',
                'GroupId': 'sg-a46a04da',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commerceauthserverESPINT',
                'GroupId': 'sg-a96a04d7',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2d157b53',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerce-authserver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceauthserverESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceptrefundPL',
        'GroupName':
        'commerceptrefundPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2e441f50',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerceptrefund'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceptrefundPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'omd secgroup',
        'GroupName':
        'tessg-omd-VNV94380BZ2V',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '43.148.16.0/22'
            }, {
                'CidrIp': '43.148.20.0/22'
            }, {
                'CidrIp': '43.148.24.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': []
        }, {
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d76ebaa9',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort': 6557,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 6557,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2e63b750',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 636,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.85/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 636,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'omd'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-omd'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commercebokuresponderESPINT',
        'GroupName':
        'ESPINTsgdef1-commercebokuresponderESPINT-LUQRH1C6PDK9',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercebokuresponderESPINT',
                'GroupId': 'sg-d3107ead',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2f157b51',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebokuresponderESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-bokuresponder'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercesecureidserverPL',
        'GroupName':
        'commercesecureidserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2f441f51',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commercesecureidserver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercesecureidserverPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'lvdc-ssh secgroup',
        'GroupName':
        'tessg-lvdcSsh-66HNKPPQ9OU4',
        'IpPermissions': [{
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.211.220.14/32'
            }, {
                'CidrIp': '10.219.157.14/32'
            }, {
                'CidrIp': '10.211.205.11/32'
            }, {
                'CidrIp': '10.237.90.41/32'
            }, {
                'CidrIp': '10.211.90.12/32'
            }, {
                'CidrIp': '10.221.90.21/32'
            }, {
                'CidrIp': '10.211.225.10/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-42528d3a',
                'PeeringStatus': 'deleted',
                'VpcId': 'vpc-970b3af3'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2f63b751',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-lvdc-ssh'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'lvdcSsh'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'mgsgatewayPL',
        'GroupName':
        'mgsgatewayPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2f712a51',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-mgsgateway'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mgsgatewayPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'oltp secgroup ',
        'GroupName':
        'GroupDefOLTP-oltp-13YAZULDD5HBT',
        'IpPermissions': [{
            'FromPort':
            1521,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            1521,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-20159e5e',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-2aa72d54',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-2cba3052',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-91a62cef',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-d0169dae',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-2fba3051',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/GroupDefOLTP/8369b9e0-3f5e-11e8-9027-503ac9841afd'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-oltp'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'oltp'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'GroupDefOLTP'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ssh-client-test-sb secgroup',
        'GroupName':
        'sshClientServer-sshClientTestSb-CCUAM3JPZMUW',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-3110c64f',
        'IpPermissionsEgress': [{
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'sshClientServer'
        }, {
            'Key': 'name',
            'Value': 'testSG'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/sshClientServer/a6fdd1d0-3553-11e8-a7aa-503f2a2cee1e'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'sshClientTestSb'
        }, {
            'Key': 'Name',
            'Value': 'sshClientTestSb'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'strongswan',
        'GroupName':
        'strongswan',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '52.26.51.254/32'
            }, {
                'CidrIp': '52.39.115.151/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.16.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            0,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '52.26.51.254/32'
            }, {
                'CidrIp': '52.39.115.151/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-31530f40',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'workflowESPINT',
        'GroupName':
        'ESPINTsgdef2-workflowESPINT-1C8FQVVPXKJRN',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-3267094c',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'Name',
            'Value': 'nav-workflowESPINT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'workflowESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ca-apm-elb secgroup',
        'GroupName':
        'tessg-caApmElb-1PESN7KCT9VJQ',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '10.242.0.0/16'
            }, {
                'CidrIp': '209.249.145.1/32'
            }, {
                'CidrIp': '173.230.196.15/32'
            }, {
                'CidrIp': '173.230.196.25/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8081,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }, {
                'CidrIp': '173.230.196.15/32'
            }, {
                'CidrIp': '173.230.196.25/32'
            }, {
                'CidrIp': '209.249.145.1/32'
            }, {
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5001,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '209.249.145.1/32'
            }, {
                'CidrIp': '10.242.0.0/16'
            }, {
                'CidrIp': '173.230.196.25/32'
            }, {
                'CidrIp': '173.230.196.15/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5001,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-326eba4c',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'caApmElb'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-ca-apm-elb'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Sandbox test SSH client secgroup testvpc',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-SSHClientSB-1L9NDTHNB6WHO',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-32d2034c',
        'IpPermissionsEgress': [{
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'SSHClientSB'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-SSHClientSB'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'splunk-elb secgroup',
        'GroupName':
        'tessg-splunkElb-Y7Z2WTGHBE9M',
        'IpPermissions': [{
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '173.230.196.15/32'
            }, {
                'CidrIp': '52.10.119.198/32'
            }, {
                'CidrIp': '43.148.20.0/22'
            }, {
                'CidrIp': '52.43.137.246/32'
            }, {
                'CidrIp': '52.89.225.15/32'
            }, {
                'CidrIp': '10.0.0.0/8'
            }, {
                'CidrIp': '52.89.176.248/32'
            }, {
                'CidrIp': '52.89.89.217/32'
            }, {
                'CidrIp': '52.42.57.219/32'
            }, {
                'CidrIp': '43.148.16.0/22'
            }, {
                'CidrIp': '43.148.3.115/32'
            }, {
                'CidrIp': '173.230.196.25/32'
            }, {
                'CidrIp': '43.148.24.0/22'
            }, {
                'CidrIp': '43.148.3.116/32'
            }, {
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '43.148.3.117/32'
            }, {
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-336eba4d',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-splunk-elb'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'splunkElb'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'bind secgroup',
        'GroupName':
        'tessg-bind-QV0T2T5A6RVL',
        'IpPermissions': [{
            'FromPort': 53,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-356eba4b',
        'IpPermissionsEgress': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }, {
                'CidrIp': '173.230.215.21/32'
            }, {
                'CidrIp': '173.230.208.21/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'bind'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-bind'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        ' EMGTMT WAF default',
        'GroupName':
        'mtAccountMGMTYML-mtAccountsWafEMGMT-1922BIO92EL7P',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d34ad7ad',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d34ad7ad',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d34ad7ad',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-3649d448',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-db4ed3a5',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'mtAccountsWafEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtAccountsWafEMGMT'
        }, {
            'Key': 'Description',
            'Value': 'MidTier WAF for Accounts EMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Sandbox test SSH server secgroup ymtestVPC',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-SSHServerSB-8IYHQ243QGRD',
        'IpPermissions': [{
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-32d2034c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-36d10048',
        'IpPermissionsEgress': [{
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-SSHServerSB'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'SSHServerSB'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Service access group for Elastic MapReduce created on 2017-10-04T01:13:49.807Z',
        'GroupName':
        'ElasticMapReduce-ServiceAccess',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-39b80e44',
        'IpPermissionsEgress': [{
            'FromPort':
            8443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-06bb0d7b',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-7ca41201',
                'UserId': '472973657150'
            }]
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commercebatchtransresolverESPINT',
        'GroupName':
        'ESPINTsgdef2-commercebatchtransresolverESPINT-1VH21H4R0N2ST',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-3a680644',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commercebatchtransresolverESPINT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebatchtransresolverESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTNginX MT Native',
        'GroupName':
        'mtAccountMGMTYML-mtNativeNGXEMGMT-U13D5R7V4QVH',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ee4bd690',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-f54bd68b',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ee4bd690',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-f54bd68b',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ee4bd690',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-f54bd68b',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-3c4ed342',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier External ELB for Native Enp'
        }, {
            'Key': 'Name',
            'Value': 'mtNativeNgxEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtNativeNGXEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'sbtesttransactionclient SG',
        'GroupName':
        'DefGroupYML-sbtransaction-172B64L5CQ0L7',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-3e8a1c40',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'sbtransaction'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-sbtesttransaction'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/DefGroupYML/229b98b0-401a-11e8-9a54-500c337110fd'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'DefGroupYML'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'This security group was generated by AWS Marketplace and is based on recommended settings for NGINX Plus - Ubuntu AMI (HVM) version 1.2 provided by Nginx Software, Inc.',
        'GroupName':
        'NGINX Plus - Ubuntu AMI -HVM--1-2-AutogenByAWSMP-',
        'IpPermissions': [{
            'FromPort': 5405,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5405,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 80,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '209.249.145.1/32'
            }, {
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 873,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 873,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 443,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-3f376045',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'NGINX-SG'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'pricingPL',
        'GroupName':
        'pricingPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-407d263e',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'pricingPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-pricing'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'EIB Router SG accepting from EIB CLient',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-eibElbNP-170Y4K3B6U0IG',
        'IpPermissions': [{
            'FromPort':
            61616,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            61616,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-89b46ef7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-89b46ef7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            3900,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3900,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-89b46ef7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            4300,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4300,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-89b46ef7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9500,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9500,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-89b46ef7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8501,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8501,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-89b46ef7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            3450,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3450,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-89b46ef7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8500,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8500,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-89b46ef7',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-40b16b3e',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-e9b26897',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'Eib-ELB-NP'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Description',
            'Value': 'EIB ELB security group'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibElbNP'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'squid-proxy-elb secgroup',
        'GroupName':
        'navadmins-secgroups-1721cf71-squidProxyElb-7RTPOPP4GI61',
        'IpPermissions': [{
            'FromPort': 3128,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3128,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-42806538',
        'IpPermissionsEgress': [{
            'FromPort':
            3128,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3128,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-62816418',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-squid-proxy-elb'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-1721cf71/e3e8b010-55f7-11e7-a592-50a686be738e'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-1721cf71'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'squidProxyElb'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'ProdLine MT WAF pci',
        'GroupName':
        'mtpciWafP',
        'IpPermissions': [{
            'FromPort':
            11080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            11086,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-199fc167',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-43623c3d',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-65603e1b',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/MtProdine/5c2d0350-4c3d-11e8-8dbe-50a68a2012ba'
        }, {
            'Key': 'Name',
            'Value': 'mtpciWafP'
        }, {
            'Key': 'Description',
            'Value': 'MidTier WAF for ProdLine'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtpciWafP'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'MtProdine'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'bind secgroup',
        'GroupName':
        'navadmins-secgroups-1721cf71-bind-16KLXAH0ZQPZ7',
        'IpPermissions': [{
            'FromPort': 53,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-43806539',
        'IpPermissionsEgress': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '173.230.208.21/32'
            }, {
                'CidrIp': '10.0.0.0/8'
            }, {
                'CidrIp': '173.230.215.21/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'bind'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-1721cf71'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-bind'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-1721cf71/e3e8b010-55f7-11e7-a592-50a686be738e'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commercepaypalserver',
        'GroupName':
        'sctest-commercepaypalserver-169APBGLEFS7C',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-4524bf3b',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerce-paypal-server'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercepaypalserver'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/sctest/f1353f30-4247-11e8-ae1a-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'sctest'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceptserverESPINT',
        'GroupName':
        'ESPINTsgdef1-commerceptserverESPINT-63ANLXQ0G73G',
        'IpPermissions': [{
            'FromPort':
            9940,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9940,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commerceptserverESPINT',
                'GroupId': 'sg-0a690774',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commerceptserverESPINT',
                'GroupId': 'sg-8d6608f3',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commerceptserverESPINT',
                'GroupId': 'sg-e3147a9d',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-46147a38',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-ptserver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceptserverESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'oltpESPINT',
        'GroupName':
        'ESPINTsgdef1-oltpESPINT-1NHV8TX25HH23',
        'IpPermissions': [{
            'FromPort':
            1521,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            1521,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-096a0477',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-0a690774',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-3267094c',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-46147a38',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-49147a37',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-68127c16',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-68690716',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-69127c17',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-706a040e',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-71117f0f',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-716a040f',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-736a040d',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-81147aff',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-8d6608f3',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-8e6b05f0',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-8f6608f1',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-906b05ee',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-916b05ef',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-a66a04d8',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-bc6907c2',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-c26806bc',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-d3107ead',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-e3147a9d',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-e5147a9b',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-e9137d97',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-f266088c',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-f366088d',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-f566088b',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-fa127c84',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for oltpESPINT',
                'GroupId': 'sg-fc6b0582',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-48147a36',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-oltp'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'oltpESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'autobotefsPL',
        'GroupName':
        'autobotefsPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-48401b36',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-autobotefs'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'autobotefsPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ProdLine ExtElB pci ',
        'GroupName':
        'mtpciExtElbP',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-484b1536',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commerceadyenserverESPINT',
        'GroupName':
        'ESPINTsgdef1-commerceadyenserverESPINT-7V86DMSDGG06',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commerceadyenserverESPINT',
                'GroupId': 'sg-0e127c70',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9990,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9990,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commerceadyenserverESPINT',
                'GroupId': 'sg-0a690774',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commerceadyenserverESPINT',
                'GroupId': 'sg-706a040e',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commerceadyenserverESPINT',
                'GroupId': 'sg-c56806bb',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-49147a37',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-adyen-server'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceadyenserverESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatoroauthPL',
        'GroupName':
        'navigatoroauthPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-49732837',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatoroauthPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigatoroauth'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'idaggregationPL',
        'GroupName':
        'idaggregationPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-4b401b35',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-idaggregation'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'idaggregationPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatoroauthESPINT',
        'GroupName':
        'ESPINTsgdef2-navigatoroauthESPINT-1JG3I7WKO14U3',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-4c6b0532',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatoroauthESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigatoroauthESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'MT WAF default',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-mtAccountsWafENP-TJOVSIIV76FO',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-1336b66d',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-1336b66d',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-1336b66d',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-4e37b730',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-e737b799',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'Name',
            'Value': 'mtAccountsWafENP'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtAccountsWafENP'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Description',
            'Value': 'MidTier WAF for Accounts prod np'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'sensuPA-elb secgroup',
        'GroupName':
        'tessg-sensuPAElb-JS82FEFBLOMM',
        'IpPermissions': [{
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.16.0/22'
            }, {
                'CidrIp': '43.138.0.0/19'
            }, {
                'CidrIp': '43.148.24.0/22'
            }, {
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '43.148.20.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-4e6db930',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'sensuPA-elb'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'sensuPAElb'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'grafana elb secgroup',
        'GroupName':
        'tessg-grafanaELB-JRFJJOS0BEWZ',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.16.0/21'
            }, {
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '43.148.24.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '173.230.196.25/32'
            }, {
                'CidrIp': '43.148.24.0/22'
            }, {
                'CidrIp': '43.148.16.0/21'
            }, {
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-4f62b631',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-grafana-elb'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'grafanaELB'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'mgstelesignresponderPL',
        'GroupName':
        'mgstelesignresponderPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-52451e2c',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-mgstelesignresponder'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mgstelesignresponderPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercelivegamerresponderPL',
        'GroupName':
        'commercelivegamerresponderPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-53451e2d',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercelivegamerresponderPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercelivegamerresponder'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceserverPL',
        'GroupName':
        'commerceserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-54451e2a',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceserverPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceserver'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'LBA - jumpbox and test source',
        'GroupName':
        'LBA - Tester',
        'IpPermissions': [{
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 80,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 8080,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8080,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': ''
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-5473da24',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }, {
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [{
                'CidrIpv6': '::/0'
            }],
            'PrefixListIds': [],
            'ToPort': 0,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'LBA-Tester'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'mgssynapseresponderPL',
        'GroupName':
        'mgssynapseresponderPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-55451e2b',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mgssynapseresponderPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-mgssynapseresponder'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceauthpbPL',
        'GroupName':
        'commerceauthpbPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-56451e28',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceauthpbPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceauthpb'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'launch-wizard-1 created 2018-03-28T11:14:28.906-07:00',
        'GroupName':
        'launch-wizard-1',
        'IpPermissions': [{
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-570bca29',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'navigatorsolrPL',
        'GroupName':
        'navigatorsolrPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-57451e29',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatorsolrPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigatorsolr'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'mdsESPINT',
        'GroupName':
        'testAp26-2018YM-mdsESPINT-1W2FNKNRJC50J',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-58afe026',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mdsESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-mds'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/testAp26-2018YM/072b6130-4968-11e8-a822-503aca41a08d'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'testAp26-2018YM'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'entitlements',
        'GroupName':
        'Output-test-entitlements-1S0NZUHQBQ1KF',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-5c345022',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.10.10.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'Output-test'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'entitlements'
        }, {
            'Key': 'Name',
            'Value': 'nav-entitlements'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/Output-test/0b21a460-4293-11e8-9c7b-503f20f2adae'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebibitbatch',
        'GroupName':
        'Output-test-commercebibitbatch-A7IOI0BZ2YX5',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-5e345020',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.10.10.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/Output-test/0b21a460-4293-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebibitbatch'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'Output-test'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercebibitbatch'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'gcimbatchapi',
        'GroupName':
        'oracledependencies-gcimbatchapi-1JR6F7WP1VXPG',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-5fed8821',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'gcimbatchapi'
        }, {
            'Key': 'Name',
            'Value': 'nav-gcimbatchapi'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'oracledependencies'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/oracledependencies/fc969580-4289-11e8-b529-50d5ca789eae'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ProdLine Internal MT EIB',
        'GroupName':
        'mtPartnerIntElbP',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-62603e1c',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier Internal ELB for Partner ProdLine'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/MtProdine/5c2d0350-4c3d-11e8-8dbe-50a68a2012ba'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtPartnerIntElbP'
        }, {
            'Key': 'Name',
            'Value': 'mtPartnerIntElbP'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'MtProdine'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'squid-proxy secgroup',
        'GroupName':
        'navadmins-secgroups-1721cf71-squidProxy-12SFU6RG8GH0F',
        'IpPermissions': [{
            'FromPort':
            3128,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3128,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-42806538',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-62816418',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-1721cf71/e3e8b010-55f7-11e7-a592-50a686be738e'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-1721cf71'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'squidProxy'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-squid-proxy'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Sandbox test SSH client secgroup ',
        'GroupName':
        'GroupDef-SSHClientSB-1YWFKUUEBN0Z',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-64179c1a',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'SSHClientSB'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'GroupDef'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-testSSHClientSB'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/GroupDef/344dc9f0-3eeb-11e8-8ecb-503ac9ec2435'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'memcachedauthserverPL',
        'GroupName':
        'memcachedauthserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-647e251a',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'memcachedauthserverPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-memcachedauthserver'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ProdLine Internal MT ELB',
        'GroupName':
        'mtpciIntElbP',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-43623c3d',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-65603e1b',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-199fc167',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'mtpciIntElbP'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtpciIntElbP'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'MtProdine'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/MtProdine/5c2d0350-4c3d-11e8-8dbe-50a68a2012ba'
        }, {
            'Key': 'Description',
            'Value': 'MidTier Internal ELB for pci ProdLine'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'squid-proxy-elb secgroup',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-squidProxyElb-12W2EG90C4RHU',
        'IpPermissions': [{
            'FromPort': 3128,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3128,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-65655b18',
        'IpPermissionsEgress': [{
            'FromPort':
            3128,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3128,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f7625c8a',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Name',
            'Value': 'ymtestVPC-squid-proxy-elb'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'squidProxyElb'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'nagios secgroup',
        'GroupName':
        'tessg-nagios-1HANVJMJF6E5W',
        'IpPermissions': [{
            'FromPort': 5667,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5667,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 6557,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 6557,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            6556,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            6556,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-656cb81b',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-656cb81b',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 636,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.85/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 636,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-nagios'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'nagios'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commercebatchtransresolverPL',
        'GroupName':
        'commercebatchtransresolverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-657b201b',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercebatchtransresolver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebatchtransresolverPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceamexbatchPL',
        'GroupName':
        'commerceamexbatchPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-657e251b',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceamexbatchPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceamexbatch'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebibitresponderESPINT',
        'GroupName':
        'ESPINTsgdef1-commercebibitresponderESPINT-JU6WNQENUPY',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercebibitresponderESPINT',
                'GroupId': 'sg-71117f0f',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-66127c18',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebibitresponderESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-bibitresponder'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercelivegamerlistenerESPINT',
        'GroupName':
        'ESPINTsgdef2-commercelivegamerlistenerESPINT-1XHHV9U0ODALJ',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-66690718',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercelivegamerlistenerESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercelivegamerlistenerESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'memcachedmediaPL',
        'GroupName':
        'memcachedmediaPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-667b2018',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'memcachedmediaPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-memcachedmedia'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercedbproxyESPINT',
        'GroupName':
        'ESPINTsgdef1-commercedbproxyESPINT-ZON2U1SX4V30',
        'IpPermissions': [{
            'FromPort':
            4000,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4000,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercedbproxyESPINT',
                'GroupId': 'sg-086a0476',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commercedbproxyESPINT',
                'GroupId': 'sg-3a680644',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commercedbproxyESPINT',
                'GroupId': 'sg-6e117f10',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commercedbproxyESPINT',
                'GroupId': 'sg-8c6608f2',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commercedbproxyESPINT',
                'GroupId': 'sg-e2147a9c',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commercedbproxyESPINT',
                'GroupId': 'sg-e6137d98',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-68127c16',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercedbproxyESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-db-proxy'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceptrefundESPINT',
        'GroupName':
        'ESPINTsgdef2-commerceptrefundESPINT-19SCQWN7T44Y0',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-68690716',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerceptrefundESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceptrefundESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercelivegamerserverESPINT',
        'GroupName':
        'ESPINTsgdef1-commercelivegamerserverESPINT-XT0VLTYRZSC1',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercelivegamerserverESPINT',
                'GroupId': 'sg-e1147a9f',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9928,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9928,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercelivegamerserverESPINT',
                'GroupId': 'sg-66690718',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commercelivegamerserverESPINT',
                'GroupId': 'sg-e3147a9d',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-69127c17',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerce-livegamer-server'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercelivegamerserverESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebokulistenerESPINT',
        'GroupName':
        'ESPINTsgdef2-commercebokulistenerESPINT-1PB5UISPL73HP',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-69690717',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commercebokulistenerESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebokulistenerESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'oltpPL',
        'GroupName':
        'oltpPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-697b2017',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-oltp'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'oltpPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'eventsPL',
        'GroupName':
        'eventsPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-6a461d14',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-events'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eventsPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ProdLine MT WAF default',
        'GroupName':
        'mtWafP',
        'IpPermissions': [{
            'FromPort':
            11080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            11086,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-6d9fc113',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-6a9fc114',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-c9633db7',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/MtProdine/5c2d0350-4c3d-11e8-8dbe-50a68a2012ba'
        }, {
            'Key': 'Description',
            'Value': 'MidTier WAF for ProdLine'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtWafP'
        }, {
            'Key': 'Name',
            'Value': 'mtWafP'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'MtProdine'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercepaymenttrustserverPL',
        'GroupName':
        'commercepaymenttrustserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-6b461d15',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercepaymenttrustserverPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercepaymenttrustserver'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebibitresponderPL',
        'GroupName':
        'commercebibitresponderPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-6c461d12',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commercebibitresponder'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebibitresponderPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercelivegamerlistenerPL',
        'GroupName':
        'commercelivegamerlistenerPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-6d461d13',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commercelivegamerlistener'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercelivegamerlistenerPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebibitbatchPL',
        'GroupName':
        'commercebibitbatchPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-6d732813',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebibitbatchPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercebibitbatch'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ProdLine NginX MT Default',
        'GroupName':
        'mtDefaultNGXP',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-c9633db7',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-db623ca5',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-c9633db7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-db623ca5',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-6d9fc113',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'MtProdine'
        }, {
            'Key': 'Name',
            'Value': 'mtDefaultNGXP'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtDefaultNGXP'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Default ProdLine'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/MtProdine/5c2d0350-4c3d-11e8-8dbe-50a68a2012ba'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'providercacheserverESPINT',
        'GroupName':
        'ESPINTsgdef1-providercacheserverESPINT-X6FLTCRYSX6Q',
        'IpPermissions': [{
            'FromPort':
            4100,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4100,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for providercacheserverESPINT',
                'GroupId': 'sg-8c6608f2',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for providercacheserverESPINT',
                'GroupId': 'sg-e2147a9c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-6e117f10',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'providercacheserverESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-provider-cache-server'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'PL EIB Router SG accepting from EIB CLient',
        'GroupName':
        'eibElbPL',
        'IpPermissions': [{
            'FromPort':
            61616,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            61616,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-9488d6ea',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-9488d6ea',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            3900,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3900,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-9488d6ea',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            4300,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4300,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-9488d6ea',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9500,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9500,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-9488d6ea',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8501,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8501,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-9488d6ea',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            3450,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3450,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-9488d6ea',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-9488d6ea',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8500,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8500,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-9488d6ea',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-6e86d810',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-6f86d811',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ELB-ErtrProdLine'
        }, {
            'Key': 'Name',
            'Value': 'Eib-ELB-PL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ELB-ErtrProdLine/d7bb6d50-4c41-11e8-a66a-50a68af3968d'
        }, {
            'Key': 'Description',
            'Value': 'PL EIB ELB security group'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibElbPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercehandleserverPL',
        'GroupName':
        'commercehandleserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-6f732811',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercehandleserver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercehandleserverPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EQA Internal MT ELB EMGT',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-mtAccountsIntElbEQA-XANXBCQF4PLH',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-857be6fb',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-857be6fb',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-857be6fb',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-6f75e811',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-bd76ebc3',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'mtAccountsIntElbEQA'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtAccountsIntElbEQA'
        }, {
            'Key': 'Description',
            'Value': 'MidTier Internal ELB for Accounts EQA'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'PL EIB Router',
        'GroupName':
        'eibRouterPL',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            61616,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-6e86d810',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-6f86d811',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ELB-ErtrProdLine'
        }, {
            'Key': 'Name',
            'Value': 'EIB router SG PL'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibRouterPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ELB-ErtrProdLine/d7bb6d50-4c41-11e8-a66a-50a68af3968d'
        }, {
            'Key': 'Description',
            'Value': 'PL EIB ELB client security group'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'paymenttrustbatchESPINT',
        'GroupName':
        'ESPINTsgdef2-paymenttrustbatchESPINT-1R1SR6P3VTSNQ',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-706a040e',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-paymenttrustbatchESPINT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'paymenttrustbatchESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebibitserverESPINT',
        'GroupName':
        'ESPINTsgdef1-commercebibitserverESPINT-1HKGO6DKSXRAX',
        'IpPermissions': [{
            'FromPort':
            9930,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9930,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercebibitserverESPINT',
                'GroupId': 'sg-a76a04d9',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commercebibitserverESPINT',
                'GroupId': 'sg-e2147a9c',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commercebibitserverESPINT',
                'GroupId': 'sg-e3147a9d',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercebibitserverESPINT',
                'GroupId': 'sg-66127c18',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-71117f0f',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-bibitserver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebibitserverESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'gcimauthESPINT',
        'GroupName':
        'ESPINTsgdef2-gcimauthESPINT-1CME8T6V6PCNZ',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-716a040f',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-gcimauthESPINT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'gcimauthESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ALLOW ANY',
        'GroupName':
        'ALLOW ANY',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7204850f',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'SG for elb YM test051618',
        'GroupName':
        'myelbsecuritygroup2',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-72b97603',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Security group for Kubernetes ELB a318e51a35d5711e8968006e351a1fff (default/guestbook)',
        'GroupName':
        'k8s-elb-a318e51a35d5711e8968006e351a1fff',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-73478b02',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'kubernetes.io/cluster/preview',
            'Value': 'owned'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'consolenotificationsESPINT',
        'GroupName':
        'ESPINTsgdef2-consolenotificationsESPINT-1SMS002ES919W',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-736a040d',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'Name',
            'Value': 'nav-consolenotificationsESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'consolenotificationsESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'squid-proxy secgroup',
        'GroupName':
        'tessg-squidProxy-D6D6DY8IFL80',
        'IpPermissions': [{
            'FromPort': 8300,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8301,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            3128,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3128,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-186fbb66',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-766fbb08',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'squidProxy'
        }, {
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-squid-proxy'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'gcimauth',
        'GroupName':
        'oracledependencies-gcimauth-1JOE17UR8ZG28',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-76e88d08',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-gcimauth'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'oracledependencies'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/oracledependencies/fc969580-4289-11e8-b529-50d5ca789eae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'gcimauth'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTInternal MT ELB',
        'GroupName':
        'mtAccountMGMTYML-mtDefaultIntElbEMGMT-OEFFZZ4MNF2I',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f24bd68c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f24bd68c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f24bd68c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7745d809',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-b148d5cf',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier Internal ELB for Default Enp'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'Name',
            'Value': 'mtDefaultIntElbEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtDefaultIntElbEMGMT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'gcimauthPL',
        'GroupName':
        'gcimauthPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7a471c04',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-gcimauth'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'gcimauthPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Sie offices SG with inbound access',
        'GroupName':
        'sie-offices-inbound',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '173.230.196.15/32'
            }, {
                'CidrIp': '173.230.196.25/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.12.121/32'
            }, {
                'CidrIp': '43.148.8.11/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7b78520a',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'accountsPL',
        'GroupName':
        'accountsPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7c471c02',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-accounts'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'accountsPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTInternal MT ELB',
        'GroupName':
        'mtAccountMGMTYML-mtoauthIntElbEMGMT-1TQYFQ8041N7H',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-b348d5cd',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-b348d5cd',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-b348d5cd',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7c48d502',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f34bd68d',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'mtoauthIntElbEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtoauthIntElbEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Description',
            'Value': 'MidTier Internal ELB for oauth Enp'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'sboltp secgroup ',
        'GroupName':
        'DefGroupYML-sboltp-MCV3BPMO90WE',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7c8b1d02',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/DefGroupYML/229b98b0-401a-11e8-9a54-500c337110fd'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'sboltp'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'DefGroupYML'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-sboltp'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Oracle',
        'GroupName':
        'resource77a-Oracle-1SF5WLJ4LT9R',
        'IpPermissions': [{
            'FromPort':
            1521,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            1521,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-10127c6e',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-16e88d68',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-5fed8821',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-76e88d08',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-9cee8be2',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-9fed88e1',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7ca0c502',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-Oracle'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/resource77a/6d5defc0-4280-11e8-a66a-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'resource77a'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'Oracle'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Master group for Elastic MapReduce created on 2017-10-04T01:13:49.807Z',
        'GroupName':
        'ElasticMapReduce-Master-Private',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-06bb0d7b',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-7ca41201',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-39b80e44',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            0,
            'IpProtocol':
            'udp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-06bb0d7b',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-7ca41201',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            -1,
            'IpProtocol':
            'icmp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            -1,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-06bb0d7b',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-7ca41201',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7ca41201',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'gcimresourcePL',
        'GroupName':
        'gcimresourcePL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7d471c03',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-gcimresource'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'gcimresourcePL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercesecureidserverESPINT',
        'GroupName':
        'ESPINTsgdef1-commercesecureidserverESPINT-1JV8EF5SQXUBO',
        'IpPermissions': [{
            'FromPort':
            3500,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3500,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercesecureidserverESPINT',
                'GroupId': 'sg-2d157b53',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7e157b00',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercesecureidserverESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-secureidserver'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceauthserverPL',
        'GroupName':
        'commerceauthserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7e471c00',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceauthserver'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceauthserverPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'walletsPL',
        'GroupName':
        'walletsPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7f471c01',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-wallets'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'walletsPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTExternal MT EIB',
        'GroupName':
        'mtAccountMGMTYML-mtGrcExtElbEMGMT-R617QUDW50XJ',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-7f48d501',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f04bd68e',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier External ELB for Grc Enp'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtGrcExtElbEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Name',
            'Value': 'mtGrcExtElbEMGMT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebokulistenerPL',
        'GroupName':
        'commercebokulistenerPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-80401bfe',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercebokulistener'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebokulistenerPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' Default EQAExternal MT EIB',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-mtDefaultExtElbEQA-L7FSQ1T2N896',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-810d68ff',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-09026777',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier External ELB for Default EQA'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Name',
            'Value': 'mtDefaultExtElbEQA'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtDefaultExtElbEQA'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'accountsESPINT',
        'GroupName':
        'ESPINTsgdef1-accountsESPINT-1W4T7L8P3GCH2',
        'IpPermissions': [{
            'FromPort':
            5710,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5711,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for accountsESPINT',
                'GroupId': 'sg-2c157b52',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-81147aff',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'accountsESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-accounts'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'memcahcedmediaPL',
        'GroupName':
        'memcahcedmediaPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-81401bff',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-memcahcedmedia'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'memcahcedmediaPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatortaxefsPL',
        'GroupName':
        'navigatortaxefsPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-827823fc',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatortaxefsPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigatortaxefs'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'aerospikecachingSG',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-aerospikecaching-9WQ6HY4NKMFX',
        'IpPermissions': [{
            'FromPort':
            3000,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3000,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-c47da7ba',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8279a3fc',
        'IpPermissionsEgress': [{
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-aerospikecaching'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'aerospikecaching'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EQA EIB Router EMGT',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-eibRouterEQA-1QP99I4FTSB2C',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            61616,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f874e986',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-827be6fc',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'Description',
            'Value': 'EIB ELB client security group'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Name',
            'Value': 'EIB router SG'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibRouterEQA'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'gcimbatchapiPL',
        'GroupName':
        'gcimbatchapiPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-83401bfd',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-gcimbatchapi'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'gcimbatchapiPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'splunk secgroup',
        'GroupName':
        'tessg-splunk-6E5Y74RXEO3P',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-8462b6fa',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort': 8001,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.16.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8001,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            8000,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.20.0/22'
            }, {
                'CidrIp': '43.148.24.0/22'
            }, {
                'CidrIp': '160.33.240.95/32'
            }, {
                'CidrIp': '43.138.16.79/32'
            }, {
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '43.138.8.224/32'
            }, {
                'CidrIp': '173.230.196.15/32'
            }, {
                'CidrIp': '43.148.16.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8000,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-336eba4d',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8089,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '173.230.196.0/23'
            }, {
                'CidrIp': '43.138.8.224/32'
            }, {
                'CidrIp': '173.230.211.0/24'
            }, {
                'CidrIp': '43.148.3.117/32'
            }, {
                'CidrIp': '43.138.16.79/32'
            }, {
                'CidrIp': '43.148.3.116/32'
            }, {
                'CidrIp': '173.230.215.0/24'
            }, {
                'CidrIp': '173.230.210.0/24'
            }, {
                'CidrIp': '43.148.3.115/32'
            }, {
                'CidrIp': '43.148.16.0/22'
            }, {
                'CidrIp': '10.0.0.0/8'
            }, {
                'CidrIp': '160.33.240.95/32'
            }, {
                'CidrIp': '43.148.32.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8089,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            9997,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '173.230.211.0/24'
            }, {
                'CidrIp': '43.138.8.224/32'
            }, {
                'CidrIp': '43.148.3.115/32'
            }, {
                'CidrIp': '43.148.32.0/24'
            }, {
                'CidrIp': '173.230.215.0/24'
            }, {
                'CidrIp': '43.148.3.116/32'
            }, {
                'CidrIp': '10.0.0.0/8'
            }, {
                'CidrIp': '160.33.240.95/32'
            }, {
                'CidrIp': '173.230.210.0/24'
            }, {
                'CidrIp': '43.138.16.79/32'
            }, {
                'CidrIp': '43.148.3.117/32'
            }, {
                'CidrIp': '173.230.196.0/23'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9997,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            8090,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.3.117/32'
            }, {
                'CidrIp': '43.148.3.115/32'
            }, {
                'CidrIp': '43.148.3.116/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8090,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 6556,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 6556,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            8088,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8088,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-336eba4d',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort': 443,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8462b6fa',
        'IpPermissionsEgress': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.90/32'
            }, {
                'CidrIp': '43.148.32.97/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': []
        }, {
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }, {
                'CidrIp': '43.148.32.85/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 465,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 465,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.97/32'
            }, {
                'CidrIp': '43.148.32.90/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-splunk'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'splunk'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        ' EQA MT WAF default',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-mtAccountsWafEQA-1DRZNZ5U5IFX',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-bd76ebc3',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-bd76ebc3',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8084,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-bd76ebc3',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-857be6fb',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtAccountsWafEQA'
        }, {
            'Key': 'Name',
            'Value': 'mtAccountsWafEQA'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Description',
            'Value': 'MidTier WAF for Accounts EQA'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'haproxy security group 2 for routing',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-navigatorGateway2-1TBXJIRYOT4Z9',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-860065f8',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '34.223.209.0/25'
            }, {
                'CidrIp': '34.223.207.0/27'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-860065f8',
        'IpPermissionsEgress': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-860065f8',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort': 443,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 443,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatorGateway2'
        }, {
            'Key': 'Name',
            'Value': 'ymtestVPC-nav-prod-navigator-gateway2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatorguidePL',
        'GroupName':
        'navigatorguidePL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-867d26f8',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatorguidePL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigatorguide'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' Default EQAInternal MT ELB',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-mtDefaultIntElbEQA-169ERG42EJPVD',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-8d0e6bf3',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-8d0e6bf3',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-8d0e6bf3',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-880065f6',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-09026777',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier Internal ELB for Default EQA'
        }, {
            'Key': 'Name',
            'Value': 'mtDefaultIntElbEQA'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtDefaultIntElbEQA'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'aerospikePL',
        'GroupName':
        'aerospikePL',
        'IpPermissions': [{
            'FromPort':
            1521,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.215.92.91/32'
            }, {
                'CidrIp': '10.215.92.92/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            1521,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.211.201.80/28'
            }, {
                'CidrIp': '10.219.136.160/27'
            }, {
                'CidrIp': '10.211.201.56/31'
            }, {
                'CidrIp': '10.211.201.160/27'
            }, {
                'CidrIp': '10.211.201.120/29'
            }, {
                'CidrIp': '10.219.136.0/28'
            }, {
                'CidrIp': '10.219.136.176/28'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            4333,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.219.136.0/28'
            }, {
                'CidrIp': '10.219.136.176/28'
            }, {
                'CidrIp': '10.211.201.120/29'
            }, {
                'CidrIp': '10.211.201.160/27'
            }, {
                'CidrIp': '10.211.201.80/28'
            }, {
                'CidrIp': '10.211.201.56/31'
            }, {
                'CidrIp': '10.219.136.160/27'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4333,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            3000,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.219.136.176/28'
            }, {
                'CidrIp': '10.211.201.80/28'
            }, {
                'CidrIp': '10.219.136.160/27'
            }, {
                'CidrIp': '10.211.201.120/29'
            }, {
                'CidrIp': '10.219.136.0/28'
            }, {
                'CidrIp': '10.211.201.160/27'
            }, {
                'CidrIp': '10.211.201.56/31'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3000,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            8081,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.211.201.120/29'
            }, {
                'CidrIp': '10.219.136.176/28'
            }, {
                'CidrIp': '10.219.136.0/28'
            }, {
                'CidrIp': '10.211.201.160/27'
            }, {
                'CidrIp': '10.211.201.80/28'
            }, {
                'CidrIp': '10.219.136.160/27'
            }, {
                'CidrIp': '10.211.201.56/31'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8081,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-887d26f6',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-aerospike'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'aerospikePL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'haproxy security group for routing',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-navigatorGateway-KLXCZZCOMGER',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-890065f7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.211.42.150/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            8443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.16.0/22'
            }, {
                'CidrIp': '43.148.0.0/20'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8443,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '72.246.52.0/24'
            }, {
                'CidrIp': '23.62.239.0/24'
            }, {
                'CidrIp': '104.96.220.0/24'
            }, {
                'CidrIp': '184.27.120.0/24'
            }, {
                'CidrIp': '165.254.134.0/24'
            }, {
                'CidrIp': '23.212.53.0/24'
            }, {
                'CidrIp': '2.16.183.0/24'
            }, {
                'CidrIp': '184.84.239.0/24'
            }, {
                'CidrIp': '10.241.0.0/20'
            }, {
                'CidrIp': '23.219.163.0/24'
            }, {
                'CidrIp': '23.211.118.0/24'
            }, {
                'CidrIp': '184.29.106.0/24'
            }, {
                'CidrIp': '23.79.240.0/24'
            }, {
                'CidrIp': '95.101.82.0/24'
            }, {
                'CidrIp': '2.18.240.0/24'
            }, {
                'CidrIp': '95.101.2.0/24'
            }, {
                'CidrIp': '104.71.131.0/24'
            }, {
                'CidrIp': '72.247.10.0/24'
            }, {
                'CidrIp': '23.215.15.0/24'
            }, {
                'CidrIp': '23.219.162.0/24'
            }, {
                'CidrIp': '10.237.50.140/32'
            }, {
                'CidrIp': '72.246.216.0/24'
            }, {
                'CidrIp': '184.51.199.0/24'
            }, {
                'CidrIp': '96.17.145.0/24'
            }, {
                'CidrIp': '184.51.101.0/24'
            }, {
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '104.97.78.0/24'
            }, {
                'CidrIp': '52.89.229.109/32'
            }, {
                'CidrIp': '23.73.181.0/24'
            }, {
                'CidrIp': '205.169.30.0/24'
            }, {
                'CidrIp': '173.223.52.0/24'
            }, {
                'CidrIp': '23.215.10.0/24'
            }, {
                'CidrIp': '52.34.224.158/32'
            }, {
                'CidrIp': '54.244.55.0/24'
            }, {
                'CidrIp': '23.62.238.0/24'
            }, {
                'CidrIp': '72.246.43.0/24'
            }, {
                'CidrIp': '184.84.243.0/24'
            }, {
                'CidrIp': '10.241.96.0/20'
            }, {
                'CidrIp': '54.69.116.37/32'
            }, {
                'CidrIp': '23.216.10.0/24'
            }, {
                'CidrIp': '23.205.170.0/24'
            }, {
                'CidrIp': '165.254.47.0/24'
            }, {
                'CidrIp': '23.33.186.0/24'
            }, {
                'CidrIp': '72.246.150.0/24'
            }, {
                'CidrIp': '95.101.129.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-890065f7',
        'IpPermissionsEgress': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }, {
                'CidrIp': '173.230.216.10/32'
            }, {
                'CidrIp': '173.230.216.11/32'
            }, {
                'CidrIp': '173.230.200.0/21'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-890065f7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.90/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 636,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.85/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 636,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 3269,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.85/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3269,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 443,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 443,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatorGateway'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Name',
            'Value': 'ymtestVPC-nav-prod-navigator-gateway'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'default VPC security group',
        'GroupName':
        'default',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-8913ccf4',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8913ccf4',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'providercacheserverPL',
        'GroupName':
        'providercacheserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-897d26f7',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Name',
            'Value': 'nav-providercacheserver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'providercacheserverPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'EIB CLient to EIB Router',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-eibElbClientNP-19QHCPQSNXGR7',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-89b46ef7',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'EIB ELB client security group'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Name',
            'Value': 'eibElbClientNP'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibElbClientNP'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ProdLine NginX MT Partner',
        'GroupName':
        'mtPartnerNGXP',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-62603e1c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-62603e1c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9500,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9503,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-62603e1c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8501,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8504,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-62603e1c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            4300,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4303,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-62603e1c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-62603e1c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-62603e1c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8a613ff4',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'mtPartnerNGXP'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtPartnerNGXP'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/MtProdine/5c2d0350-4c3d-11e8-8dbe-50a68a2012ba'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Partner ProdLine'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'MtProdine'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatormediaPL',
        'GroupName':
        'navigatormediaPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8b7d26f5',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-navigatormedia'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatormediaPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'providerdataserverESPINT',
        'GroupName':
        'ESPINTsgdef2-providerdataserverESPINT-140HLLP8P1ELY',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8c6608f2',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'providerdataserverESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-providerdataserverESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'mgssmsPL',
        'GroupName':
        'mgssmsPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8c7229f2',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mgssmsPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-mgssms'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' Default EQAMT WAF default',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-mtDefaultWafEQA-140MHH76E6BDZ',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-09026777',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-09026777',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-09026777',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8d0e6bf3',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-880065f6',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'mtDefaultWafEQA'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtDefaultWafEQA'
        }, {
            'Key': 'Description',
            'Value': 'MidTier WAF for Default EQA'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceptbatchESPINT',
        'GroupName':
        'ESPINTsgdef2-commerceptbatchESPINT-1HPMHXZ4D0V10',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8d6608f3',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceptbatchESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceptbatchESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebatchtoolPL',
        'GroupName':
        'commercebatchtoolPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8d7229f3',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commercebatchtool'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebatchtoolPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'gcimbatchESPINT',
        'GroupName':
        'ESPINTsgdef2-gcimbatchESPINT-YNU47N10BQKW',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8e6b05f0',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'gcimbatchESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-gcimbatchESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceredserverESPINT',
        'GroupName':
        'ESPINTsgdef1-commerceredserverESPINT-DOT6H6EGLVW5',
        'IpPermissions': [{
            'FromPort':
            4200,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4200,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commerceredserverESPINT',
                'GroupId': 'sg-e2147a9c',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commerceredserverESPINT',
                'GroupId': 'sg-e3147a9d',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8f137df1',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-redserver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceredserverESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatorsolrESPINT',
        'GroupName':
        'ESPINTsgdef2-navigatorsolrESPINT-P9APDA5VSFJY',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-8f6608f1',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigatorsolrESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatorsolrESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'gcimresourceESPINT',
        'GroupName':
        'ESPINTsgdef2-gcimresourceESPINT-1KHMF5OAEXQI',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-906b05ee',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-gcimresourceESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'gcimresourceESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'catalogESPINT',
        'GroupName':
        'ESPINTsgdef2-catalogESPINT-MLQ2SKB9HIUA',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-916b05ef',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-catalogESPINT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'catalogESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Sandbox pricing secgroup ',
        'GroupName':
        'GroupDefOLTP-pricing-7VETY2BIJYQF',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-91a62cef',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'pricing'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-testpricing'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/GroupDefOLTP/8369b9e0-3f5e-11e8-9027-503ac9841afd'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'GroupDefOLTP'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'For NFS',
        'GroupName':
        'nav-sandbox-efs',
        'IpPermissions': [{
            'FromPort':
            2049,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            2049,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-945594ea',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-df3acea5',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-945594ea',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-efs'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'PL EIB CLient to EIB Router',
        'GroupName':
        'eibElbClientPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-9488d6ea',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ELB-ErtrProdLine'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ELB-ErtrProdLine/d7bb6d50-4c41-11e8-a66a-50a68af3968d'
        }, {
            'Key': 'Name',
            'Value': 'eibElbClientPL'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibElbClientPL'
        }, {
            'Key': 'Description',
            'Value': 'PL EIB ELB client security group'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTEIB CLient to EIB Router EMGMT',
        'GroupName':
        'mtAccountMGMTYML-eibElbClientMGMT-179X9XTHFT77I',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-984ed3e6',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'Name',
            'Value': 'eibElbClientMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibElbClientMGMT'
        }, {
            'Key': 'Description',
            'Value': 'EIB ELB client security group'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'cisESPINT',
        'GroupName':
        'testAp26-2018YM-cisESPINT-BYV8OYQLAEV1',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-98afe0e6',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'testAp26-2018YM'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'cisESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-cis'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/testAp26-2018YM/072b6130-4968-11e8-a822-503aca41a08d'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatorpcESPINT',
        'GroupName':
        'testAp26-2018YM-navigatorpcESPINT-1PKLCJPJSCZ11',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-99afe0e7',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'testAp26-2018YM'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatorpcESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/testAp26-2018YM/072b6130-4968-11e8-a822-503aca41a08d'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigatorpc'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'External MT EIB',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-mtAccountsExtElbENP-PGSRI4XBTA1Z',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-9b37b7e5',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-1336b66d',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier External ELB for Accounts prod np'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'Name',
            'Value': 'mtAccountsExtElbENP'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtAccountsExtElbENP'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceptbatchPL',
        'GroupName':
        'commerceptbatchPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-9c451ee2',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceptbatch'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceptbatchPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'gcimresource',
        'GroupName':
        'oracledependencies-gcimresource-QFDFFCRXILFL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-9cee8be2',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-gcimresource'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/oracledependencies/fc969580-4289-11e8-b529-50d5ca789eae'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'oracledependencies'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'gcimresource'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercepaypalserverPL',
        'GroupName':
        'commercepaypalserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-9d451ee3',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commercepaypalserver'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercepaypalserverPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebibitserverPL',
        'GroupName':
        'commercebibitserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-9e7328e0',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebibitserverPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercebibitserver'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebokuresponderPL',
        'GroupName':
        'commercebokuresponderPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-9f7328e1',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebokuresponderPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercebokuresponder'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'workflow',
        'GroupName':
        'oracledependencies-workflow-1QXGK66PR104Y',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-9fed88e1',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-workflow'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/oracledependencies/fc969580-4289-11e8-b529-50d5ca789eae'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'oracledependencies'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'workflow'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatortaxuiPL',
        'GroupName':
        'navigatortaxuiPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a07328de',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-navigatortaxui'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatortaxuiPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Sandbox sbpricing secgroup ',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-sbpricing-1W67GIHYIDDAF',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a16306df',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-sbtestpricing'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'sbpricing'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatorresourcePL',
        'GroupName':
        'navigatorresourcePL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a17328df',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-navigatorresource'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatorresourcePL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'cassandraPL',
        'GroupName':
        'cassandraPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a2411adc',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'cassandraPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-cassandra'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTInternal MT ELB',
        'GroupName':
        'mtAccountMGMTYML-mtGrcIntElbEMGMT-1N8XDTB6X58JJ',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-a44fd2da',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-a44fd2da',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-a44fd2da',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a24fd2dc',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f04bd68e',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'mtGrcIntElbEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtGrcIntElbEMGMT'
        }, {
            'Key': 'Description',
            'Value': 'MidTier Internal ELB for Grc Enp'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTExternal MT EIB',
        'GroupName':
        'mtAccountMGMTYML-mtVersaExtElbEMGMT-1SDG05WXUAOVH',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a34fd2dd',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d84ed3a6',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtVersaExtElbEMGMT'
        }, {
            'Key': 'Name',
            'Value': 'mtVersaExtElbEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Versa Enp'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'omd-elb secgroup',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-omdElb-EEVELHKW3H85',
        'IpPermissions': [{
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '173.230.196.15/32'
            }, {
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '43.148.16.0/22'
            }, {
                'CidrIp': '43.148.20.0/22'
            }, {
                'CidrIp': '43.148.24.0/22'
            }, {
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a40267da',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 636,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.85/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 636,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Name',
            'Value': 'ymtestVPC-omd-elb'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'omdElb'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'cassandraESPINT',
        'GroupName':
        'ESPINTsgdef1-cassandraESPINT-AVMSLW04H397',
        'IpPermissions': [{
            'FromPort':
            9042,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9042,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for cassandraESPINT',
                'GroupId': 'sg-4c6b0532',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for cassandraESPINT',
                'GroupId': 'sg-c46806ba',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for cassandraESPINT',
                'GroupId': 'sg-f066088e',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a4127cda',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'cassandraESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-cassandra'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceamexbatch',
        'GroupName':
        'Output-test-commerceamexbatch-AMCU7DAPWQ27',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a43450da',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.10.10.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerceamexbatch'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'Output-test'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/Output-test/0b21a460-4293-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceamexbatch'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTMT WAF default',
        'GroupName':
        'mtAccountMGMTYML-mtGrcWafEMGMT-K64K5LENN34S',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f04bd68e',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f04bd68e',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f04bd68e',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a44fd2da',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-a24fd2dc',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtGrcWafEMGMT'
        }, {
            'Key': 'Name',
            'Value': 'mtGrcWafEMGMT'
        }, {
            'Key': 'Description',
            'Value': 'MidTier WAF for Grc Enp'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceproxyaasESPINT',
        'GroupName':
        'ESPINTsgdef2-commerceproxyaasESPINT-1ESEGBFAWA6VT',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a46a04da',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceproxyaasESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceproxyaasESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTExternal MT EIB',
        'GroupName':
        'mtAccountMGMTYML-mtPartnerExtElbEMGMT-JWR1FNE17U7M',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a54fd2db',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtPartnerExtElbEMGMT'
        }, {
            'Key': 'Name',
            'Value': 'mtPartnerExtElbEMGMT'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Partner Enp'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'tlilletTest created 2018-03-20T09:28:22.675-07:00',
        'GroupName':
        'tlilleyTest',
        'IpPermissions': [{
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 80,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            7199,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': 'Needed for Cassandra'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            7199,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 27100,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '139.131.108.5/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 27100,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            7000,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': 'Needed for Cassandra'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            7001,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            9160,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': 'Needed for Cassandra'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9160,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            9042,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': 'Needed for Cassandra'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9042,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a59a80da',
        'IpPermissionsEgress': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0',
                'Description': 'aci '
            }],
            'Ipv6Ranges': [{
                'CidrIpv6': '::/0',
                'Description': 'aci '
            }],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'commerceincommESPINT',
        'GroupName':
        'ESPINTsgdef1-commerceincommESPINT-K2VPY2ZOTV4S',
        'IpPermissions': [{
            'FromPort':
            9960,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9960,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for commerceincommESPINT',
                'GroupId': 'sg-e2147a9c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a6117fd8',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceincommESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-incomm'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebibitbatchESPINT',
        'GroupName':
        'ESPINTsgdef2-commercebibitbatchESPINT-7WT1S2IUMLOO',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a66a04d8',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebibitbatchESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercebibitbatchESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'aerospikeESPINT',
        'GroupName':
        'ESPINTsgdef1-aerospikeESPINT-1FQ9EUV2P9ZAD',
        'IpPermissions': [{
            'FromPort':
            3000,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3000,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for aerospikeESPINT',
                'GroupId': 'sg-096a0477',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for aerospikeESPINT',
                'GroupId': 'sg-68127c16',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for aerospikeESPINT',
                'GroupId': 'sg-81147aff',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for aerospikeESPINT',
                'GroupId': 'sg-916b05ef',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for aerospikeESPINT',
                'GroupId': 'sg-e9137d97',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for aerospikeESPINT',
                'GroupId': 'sg-f366088d',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for aerospikeESPINT',
                'GroupId': 'sg-f566088b',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a71779d9',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-aerospike'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'aerospikeESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ad replication secgroup',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-adRepl-QXXEGUZERQTK',
        'IpPermissions': [{
            'FromPort': 445,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 445,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 138,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 138,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 464,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 464,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 464,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 464,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 135,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 135,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 5722,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5722,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53211,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53213,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 389,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 389,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 389,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 389,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 445,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 445,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 3268,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3269,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 88,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 88,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 139,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 139,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 135,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 135,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 88,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 88,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a768bed9',
        'IpPermissionsEgress': [{
            'FromPort':
            445,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            445,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            138,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            138,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            464,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            464,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            464,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            464,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            135,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            135,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5722,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5722,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            53211,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            53213,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            389,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            389,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            53,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            53,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            389,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            389,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            123,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            123,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            445,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            445,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            3268,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3269,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            88,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            88,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            139,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            139,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            135,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            135,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            53,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            53,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            88,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            88,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'adRepl'
        }, {
            'Key': 'Name',
            'Value': 'ymtestVPC-ad'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebibitlistenerESPINT',
        'GroupName':
        'ESPINTsgdef2-commercebibitlistenerESPINT-1184DJ2DP6HLT',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a76a04d9',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebibitlistenerESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercebibitlistenerESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ca-apm-mom secgroup',
        'GroupName':
        'tessg-caApmMom-19D7OO3IKX7XF',
        'IpPermissions': [{
            'FromPort': 5432,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5432,
            'UserIdGroupPairs': []
        }, {
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-326eba4c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            5001,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.237.50.0/24'
            }, {
                'CidrIp': '10.219.140.0/24'
            }, {
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5001,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 8081,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8081,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a76cb8d9',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 465,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 465,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-ca-apm-mom'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'caApmMom'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'mgscheetahresponderPL',
        'GroupName':
        'mgscheetahresponderPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a8461dd6',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mgscheetahresponderPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-mgscheetahresponder'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercepaypalresponderESPINT',
        'GroupName':
        'ESPINTsgdef1-commercepaypalresponderESPINT-131WHMBNDNFCB',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercepaypalresponderESPINT',
                'GroupId': 'sg-fa127c84',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a9117fd7',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-paypal-responder'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercepaypalresponderESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceblackhawkESPINT',
        'GroupName':
        'ESPINTsgdef1-commerceblackhawkESPINT-WXA7E8T94JME',
        'IpPermissions': [{
            'FromPort':
            9910,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9910,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commerceblackhawkESPINT',
                'GroupId': 'sg-e2147a9c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a9127cd7',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerce-blackhawk'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceblackhawkESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'consolegatewayESPINT',
        'GroupName':
        'ESPINTsgdef2-consolegatewayESPINT-1VSSUG2IVMAJK',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-a96a04d7',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'consolegatewayESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'Name',
            'Value': 'nav-consolegatewayESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'protegrityresponderPL',
        'GroupName':
        'protegrityresponderPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-aa461dd4',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-protegrityresponder'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'protegrityresponderPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'mgsmqpPL',
        'GroupName':
        'mgsmqpPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-aa7e25d4',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-mgsmqp'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mgsmqpPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceadyenserverPL',
        'GroupName':
        'commerceadyenserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ab461dd5',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerceadyenserver'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceadyenserverPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercetaxbridgePL',
        'GroupName':
        'commercetaxbridgePL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ab7e25d5',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commercetaxbridge'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercetaxbridgePL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'influxdb',
        'GroupName':
        'influxdb',
        'IpPermissions': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [{
                'CidrIpv6': '::/0'
            }],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }, {
            'FromPort': -1,
            'IpProtocol': 'icmp',
            'IpRanges': [],
            'Ipv6Ranges': [{
                'CidrIpv6': '::/0'
            }],
            'PrefixListIds': [],
            'ToPort': -1,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ac0690dc',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'influxdb'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'cartPL',
        'GroupName':
        'cartPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ac7e25d2',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-cart'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'cartPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'pcitokenizerPL',
        'GroupName':
        'pcitokenizerPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ad7e25d3',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-pcitokenizer'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'pcitokenizerPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTNginX MT Partner',
        'GroupName':
        'mtAccountMGMTYML-mtPartnerNGXEMGMT-K4B7NQPSQNGU',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-a54fd2db',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-a54fd2db',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-a54fd2db',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ae48d5d0',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Partner Enp'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtPartnerNGXEMGMT'
        }, {
            'Key': 'Name',
            'Value': 'mtPartnerNgxEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'squid-proxy secgroup',
        'GroupName':
        'navadmins-secgroups-f4156492-squidProxy-11UJHP1K6N1OP',
        'IpPermissions': [{
            'FromPort': 8300,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8301,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            3128,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3128,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ce6957b3',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ae6658d3',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-neteng-squid-proxy'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'squidProxy'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-f4156492'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-f4156492/4382ec70-c64b-11e7-a229-503aca41a0c5'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        ' EMGTMT WAF default',
        'GroupName':
        'mtAccountMGMTYML-mtVersaWafEMGMT-1HHDDBSB4SU1L',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d84ed3a6',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d84ed3a6',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d84ed3a6',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-af48d5d1',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d04ad7ae',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Name',
            'Value': 'mtVersaWafEMGMT'
        }, {
            'Key': 'Description',
            'Value': 'MidTier WAF for Versa Enp'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtVersaWafEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'paymenttrustbatchPL',
        'GroupName':
        'paymenttrustbatchPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-af7e25d1',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'paymenttrustbatchPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-paymenttrustbatch'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'spotubes secgroup',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-spotubes-18FXX8QL5AIN5',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-b00c69ce',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'spotubes'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Name',
            'Value': 'ymtestVPC-spotubes'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTMT WAF default',
        'GroupName':
        'mtAccountMGMTYML-mtNativeWafEMGMT-1TTKHQGGQBZIQ',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-3c4ed342',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-3c4ed342',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-3c4ed342',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-b048d5ce',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ee4bd690',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier WAF for Native Enp'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Name',
            'Value': 'mtNativeWafEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtNativeWafEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'hazelcastPL',
        'GroupName':
        'hazelcastPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-b07b20ce',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-hazelcast'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'hazelcastPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'omd secgroup',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-omd-EOCAYAR21B8K',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.20.0/22'
            }, {
                'CidrIp': '43.148.16.0/22'
            }, {
                'CidrIp': '43.148.24.0/22'
            }, {
                'CidrIp': '43.148.0.0/20'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': []
        }, {
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-a40267da',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort': 6557,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 6557,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-b10f6acf',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 636,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.85/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 636,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Name',
            'Value': 'ymtestVPC-omd'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'omd'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTNginX MT Default',
        'GroupName':
        'mtAccountMGMTYML-mtDefaultNGXEMGMT-27U8R5TTC4Z0',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-7745d809',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-d94ed3a7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-7745d809',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-d94ed3a7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-7745d809',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-d94ed3a7',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-b148d5cf',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'Name',
            'Value': 'mtDefaultNgxEMGMT'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Default Enp'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtDefaultNGXEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'bind secgroup',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-bind-1L5I1VRP8UUFF',
        'IpPermissions': [{
            'FromPort': 53,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-b1655bcc',
        'IpPermissionsEgress': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '173.230.215.21/32'
            }, {
                'CidrIp': '173.230.208.21/32'
            }, {
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'ymtestVPC-bind'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'bind'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'mdsPL',
        'GroupName':
        'mdsPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-b27b20cc',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-mds'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mdsPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTMT WAF default',
        'GroupName':
        'mtAccountMGMTYML-mtoauthWafEMGMT-2O7CE50HZ1PH',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f34bd68d',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f34bd68d',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f34bd68d',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-b348d5cd',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-7c48d502',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Name',
            'Value': 'mtoauthWafEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtoauthWafEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'Description',
            'Value': 'MidTier WAF for oauth Enp'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'entitlementsPL',
        'GroupName':
        'entitlementsPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-b37b20cd',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-entitlements'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'entitlementsPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'sbcommerceDbProxySG',
        'GroupName':
        'DefGroupYML-sbcommerceDbProxy-1SONWK6NNDZBY',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-b38c1acd',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'sbcommerceDbProxy'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-sbtestcommerceDbProxy'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/DefGroupYML/229b98b0-401a-11e8-9a54-500c337110fd'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'DefGroupYML'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebokuserverPL',
        'GroupName':
        'commercebokuserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-b57b20cb',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercebokuserver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebokuserverPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'LBA - for all other servers in LBA',
        'GroupName':
        'LBA-Services',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32',
                'Description': 'For Testing (remove me)'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }, {
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18',
                'Description': 'For Perf CT job from prod (remove me)'
            }, {
                'CidrIp':
                '10.242.0.0/16',
                'Description':
                'For Perf CT job from nonprod (remove me)'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-b966cfc9',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }, {
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.201.68.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'LBA-Services'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        ' EQA EIB CLient to EIB Router EQA',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-eibElbClientQA-H1QHIG37T7MO',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ba76ebc4',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'EIB ELB client security group'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Name',
            'Value': 'eibElbClientQA'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibElbClientQA'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatortaxuiESPINT',
        'GroupName':
        'ESPINTsgdef2-navigatortaxuiESPINT-1HT837N2LGY4H',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-bc6907c2',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatortaxuiESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigatortaxuiESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercepaypallistenerESPINT',
        'GroupName':
        'ESPINTsgdef2-commercepaypallistenerESPINT-1MPOHUHP53I72',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-bd6907c3',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercepaypallistenerESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercepaypallistenerESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EQA NginX MT Accounts EMGT',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-mtAccountsNGXEQA-1XYGK9R2YE2Z3',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-6f75e811',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-f471ec8a',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-6f75e811',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-f471ec8a',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-6f75e811',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-f471ec8a',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-bd76ebc3',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'mtAccountsNGXEQA'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtAccountsNGXEQA'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Accounts EQA'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceproxyaasPL',
        'GroupName':
        'commerceproxyaasPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-be471cc0',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceproxyaasPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceproxyaas'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'consolenotifications',
        'GroupName':
        'Output-test-consolenotifications-1XSZSQ9LE6UEA',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-bf284cc1',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.10.10.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'consolenotifications'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'Output-test'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/Output-test/0b21a460-4293-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'Name',
            'Value': 'nav-consolenotifications'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercepbPL',
        'GroupName':
        'commercepbPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-bf471cc1',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercepbPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercepb'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'centralauthPL',
        'GroupName':
        'centralauthPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-c1471cbf',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-centralauth'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'centralauthPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'test May29',
        'GroupName':
        'testym0529',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-c23f8fb3',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'gcimbatchapiESPINT',
        'GroupName':
        'ESPINTsgdef2-gcimbatchapiESPINT-1CDIRZ2M5EPRA',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-c26806bc',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-gcimbatchapiESPINT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'gcimbatchapiESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'centralauthESPINT',
        'GroupName':
        'ESPINTsgdef2-centralauthESPINT-F5T1J4DYJ2IE',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-c46806ba',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'centralauthESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-centralauthESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'accountsclient SG',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-accounts-1G3JSIZWA9G3J',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-c47da7ba',
        'IpPermissionsEgress': [{
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-accounts'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'accounts'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceadyenlistenerESPINT',
        'GroupName':
        'ESPINTsgdef2-commerceadyenlistenerESPINT-IPIKQANGVUEO',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-c56806bb',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceadyenlistenerESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceadyenlistenerESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ad replication secgroup',
        'GroupName':
        'navadmins-secgroups-f4156492-adRepl-1FOIKCLFLWUBS',
        'IpPermissions': [{
            'FromPort': 445,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 445,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 138,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 138,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 464,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 464,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 464,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 464,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 135,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 135,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 5722,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5722,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53211,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53213,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 389,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 389,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 389,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 389,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 445,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 445,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 3268,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3269,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 88,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 88,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 139,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 139,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 135,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 135,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 88,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 88,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-c68d5cb8',
        'IpPermissionsEgress': [{
            'FromPort':
            445,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            445,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            138,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            138,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            464,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            464,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            464,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            464,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            135,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            135,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5722,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5722,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            53211,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            53213,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            389,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            389,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            53,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            53,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            389,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            389,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            123,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            123,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            445,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            445,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            3268,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3269,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            88,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            88,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            139,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            139,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            135,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            135,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            53,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            53,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            88,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            88,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-f4156492/4382ec70-c64b-11e7-a229-503aca41a0c5'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'adRepl'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-f4156492'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-neteng-ad'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'commercelivegamerserverPL',
        'GroupName':
        'commercelivegamerserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-c8441fb6',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercelivegamerserverPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercelivegamerserver'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'mgsroadsterresponderPL',
        'GroupName':
        'mgsroadsterresponderPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-c9441fb7',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mgsroadsterresponderPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'Name',
            'Value': 'nav-mgsroadsterresponder'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ProdLine Internal MT ELB',
        'GroupName':
        'mtDefaultIntElbP',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-6a9fc114',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-c9633db7',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-6d9fc113',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtDefaultIntElbP'
        }, {
            'Key': 'Name',
            'Value': 'mtDefaultIntElbP'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'MtProdine'
        }, {
            'Key': 'Description',
            'Value': 'MidTier Internal ELB for Default ProdLine'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/MtProdine/5c2d0350-4c3d-11e8-8dbe-50a68a2012ba'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'spgsPL',
        'GroupName':
        'spgsPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ca441fb4',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'spgsPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-spgs'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceincommPL',
        'GroupName':
        'commerceincommPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-cb441fb5',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceincommPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceincomm'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebibitlistenerPL',
        'GroupName':
        'commercebibitlistenerPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-cc712ab2',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebibitlistenerPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercebibitlistener'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'storage-gateway',
        'GroupName':
        'storage-gateway',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ccd328b1',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commerceproxyacsESPINT',
        'GroupName':
        'ESPINTsgdef2-commerceproxyacsESPINT-1MB61ZAYLJFZJ',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ce6709b0',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceproxyacsESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceproxyacsESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'squid-proxy-elb secgroup',
        'GroupName':
        'navadmins-secgroups-f4156492-squidProxyElb-9RWTJJSM3IO0',
        'IpPermissions': [{
            'FromPort': 3128,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3128,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ce6957b3',
        'IpPermissionsEgress': [{
            'FromPort':
            3128,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3128,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ae6658d3',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-neteng-squid-proxy-elb'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-f4156492'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'squidProxyElb'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-f4156492/4382ec70-c64b-11e7-a229-503aca41a0c5'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'commerceredserverPL',
        'GroupName':
        'commerceredserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ce712ab0',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceredserver'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceredserverPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'gcimbatchPL',
        'GroupName':
        'gcimbatchPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ce7f24b0',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-gcimbatch'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'gcimbatchPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ProdLine ExtElB pci ',
        'GroupName':
        'mtpciExtElbP',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ce9ec0b0',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-199fc167',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/MtProdine/5c2d0350-4c3d-11e8-8dbe-50a68a2012ba'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Prodline pci'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtpciExtElbP'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'MtProdine'
        }, {
            'Key': 'Name',
            'Value': 'mtpciExtElbP'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'cpeproxiesPL',
        'GroupName':
        'cpeproxiesPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-cf712ab1',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'cpeproxiesPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Name',
            'Value': 'nav-cpeproxies'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceadyenresponderPL',
        'GroupName':
        'commerceadyenresponderPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-cf7f24b1',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceadyenresponderPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceadyenresponder'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'DeviceManagementServiceSG',
        'GroupName':
        'GroupDef-DeviceManagementService-FO2VY9OMP6IR',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-91a62cef',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            6379,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            6379,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-20159e5e',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d0169dae',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-testDeviceManagementService'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'GroupDef'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/GroupDef/344dc9f0-3eeb-11e8-8ecb-503ac9ec2435'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'DeviceManagementService'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTInternal MT ELB',
        'GroupName':
        'mtAccountMGMTYML-mtVersaIntElbEMGMT-DBY6RQ60O1HG',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-af48d5d1',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-af48d5d1',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-af48d5d1',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d04ad7ae',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d84ed3a6',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier Internal ELB for Versa Enp'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Name',
            'Value': 'mtVersaIntElbEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtVersaIntElbEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commerceadyenlistenerPL',
        'GroupName':
        'commerceadyenlistenerPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d0712aae',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceadyenlistenerPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerceadyenlistener'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'mgsexactresponderPL',
        'GroupName':
        'mgsexactresponderPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d1712aaf',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-mgsexactresponder'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mgsexactresponderPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercedbproxyPL',
        'GroupName':
        'commercedbproxyPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d17f24af',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commercedbproxy'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercedbproxyPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebokuserverESPINT',
        'GroupName':
        'ESPINTsgdef1-commercebokuserverESPINT-YFLGQIMY6I8X',
        'IpPermissions': [{
            'FromPort':
            9925,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9925,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercebokuserverESPINT',
                'GroupId': 'sg-69690717',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commercebokuserverESPINT',
                'GroupId': 'sg-e2147a9c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercebokuserverESPINT',
                'GroupId': 'sg-2f157b51',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d3107ead',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commerce-boku-server'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebokuserverESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTNginX MT Accounts EMGT',
        'GroupName':
        'mtAccountMGMTYML-mtAccountsNGXEMGMT-1P7APJOGMUM2O',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-294ad757',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-db4ed3a5',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-294ad757',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-db4ed3a5',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-294ad757',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-db4ed3a5',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d34ad7ad',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier External ELB for Accounts EMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'Name',
            'Value': 'mtAccountsNGXEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtAccountsNGXEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercetaxbridgeserverPL',
        'GroupName':
        'commercetaxbridgeserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d3712aad',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-commercetaxbridgeserver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercetaxbridgeserverPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'devicemanagementservicePL',
        'GroupName':
        'devicemanagementservicePL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d37f24ad',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'devicemanagementservicePL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-devicemanagementservice'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'nagios secgroup',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-nagios-1LOT8NWSEE6GY',
        'IpPermissions': [{
            'FromPort': 5667,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5667,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 6557,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 6557,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            6556,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            6556,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d40366aa',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d40366aa',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 636,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.85/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 636,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'ymtestVPC-nagios'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'nagios'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'catalog',
        'GroupName':
        'Output-test-catalog-XSD99MLREIGH',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d42a4eaa',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.10.10.0/24'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/Output-test/0b21a460-4293-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'Name',
            'Value': 'nav-catalog'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'Output-test'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'catalog'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'rsa secgroup',
        'GroupName':
        'tessg-rsa-I9TVUR4QI58',
        'IpPermissions': [{
            'FromPort': 5500,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5500,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 5580,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5580,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 5550,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5550,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 5500,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5500,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d463b7aa',
        'IpPermissionsEgress': [{
            'FromPort': 8443,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.19/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8443,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5500,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.70/32'
            }, {
                'CidrIp': '43.148.62.16/32'
            }, {
                'CidrIp': '43.148.4.42/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5500,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5580,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.62.16/32'
            }, {
                'CidrIp': '43.148.4.42/32'
            }, {
                'CidrIp': '43.148.33.70/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5580,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5550,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.70/32'
            }, {
                'CidrIp': '43.148.4.42/32'
            }, {
                'CidrIp': '43.148.62.16/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5550,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5500,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.4.42/32'
            }, {
                'CidrIp': '43.148.33.70/32'
            }, {
                'CidrIp': '43.148.62.16/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5500,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'rsa'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-rsa'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'default VPC security group',
        'GroupName':
        'default',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d4d97fa9',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d4d97fa9',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ad replication secgroup',
        'GroupName':
        'tessg-adRepl-1UC1J1J918IP7',
        'IpPermissions': [{
            'FromPort': 445,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 445,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 138,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 138,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 464,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 464,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 464,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 464,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 135,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 135,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 5722,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5722,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53211,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53213,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 389,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 389,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 389,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 389,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 445,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 445,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 3268,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3269,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 88,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 88,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 139,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 139,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 135,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 135,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 53,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 88,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 88,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d563b7ab',
        'IpPermissionsEgress': [{
            'FromPort':
            445,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            445,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            138,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            138,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            464,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            464,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            464,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            464,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            135,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            135,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            5722,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5722,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            53211,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            53213,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            389,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            389,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            53,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            53,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            389,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            389,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            123,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            123,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            445,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            445,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            3268,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3269,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            88,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            88,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            139,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            139,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            135,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.75/32'
            }, {
                'CidrIp': '43.148.33.76/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            135,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            53,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            53,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            88,
            'IpProtocol':
            'udp',
            'IpRanges': [{
                'CidrIp': '43.148.33.76/32'
            }, {
                'CidrIp': '43.148.33.75/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            88,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'adRepl'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-ad'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        ' EMGTExternal MT EIB',
        'GroupName':
        'mtAccountMGMTYML-mtoauthExtElbEMGMT-NPWQ3WWXN8CM',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d64ed3a8',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f34bd68d',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for oauth Enp'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtoauthExtElbEMGMT'
        }, {
            'Key': 'Name',
            'Value': 'mtoauthExtElbEMGMT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'consul secgroup',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-consul-11V8AARDWK8FK',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/16'
            }, {
                'CidrIp': '10.201.128.0/21'
            }, {
                'CidrIp': '10.243.128.0/20'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d70366a9',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d70366a9',
        'IpPermissionsEgress': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }, {
                'CidrIp': '43.148.32.90/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [{
                'Description': 'S3 Endpoint',
                'PrefixListId': 'pl-68a54001'
            }],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'consul'
        }, {
            'Key': 'Name',
            'Value': 'ymtestVPC-consul'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'test no ingress',
        'GroupName':
        'noingress',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d72898a6',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'omd-elb secgroup',
        'GroupName':
        'tessg-omdElb-LZT8BVCCRV8B',
        'IpPermissions': [{
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.16.0/22'
            }, {
                'CidrIp': '173.230.196.15/32'
            }, {
                'CidrIp': '43.148.20.0/22'
            }, {
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '43.148.24.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d76ebaa9',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 636,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.85/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 636,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'omdElb'
        }, {
            'Key': 'Name',
            'Value': 'nav-prodadmin-metrics-omd-elb'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        ' EMGTNginX MT Versa',
        'GroupName':
        'mtAccountMGMTYML-mtVersaNGXEMGMT-1FDLUZ26GXWN8',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-a34fd2dd',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-d04ad7ae',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-a34fd2dd',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-d04ad7ae',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-a34fd2dd',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-d04ad7ae',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d84ed3a6',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier External ELB for Versa Enp'
        }, {
            'Key': 'Name',
            'Value': 'mtVersaNgxEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtVersaNGXEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTExternal MT EIB',
        'GroupName':
        'mtAccountMGMTYML-mtDefaultExtElbEMGMT-1QVEEMN3VBE7L',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d94ed3a7',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-b148d5cf',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier External ELB for Default Enp'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'Name',
            'Value': 'mtDefaultExtElbEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtDefaultExtElbEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'protegrityresponderESPINT',
        'GroupName':
        'testAp26-2018YM-protegrityresponderESPINT-JYRPGF4DWLLM',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-d994dba7',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'protegrityresponderESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-protegrityresponder'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/testAp26-2018YM/072b6130-4968-11e8-a822-503aca41a08d'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'testAp26-2018YM'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTEIB Router EMGT',
        'GroupName':
        'mtAccountMGMTYML-eibRouterEMGMT-1MQWFFI09YRII',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            61616,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f14bd68f',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-da4ed3a4',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibRouterEMGMT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'Description',
            'Value': 'EIB ELB client security group'
        }, {
            'Key': 'Name',
            'Value': 'EIB router SG'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTInternal MT ELB EMGT',
        'GroupName':
        'mtAccountMGMTYML-mtAccountsIntElbEMGMT-EGBGCFPBL7BA',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-3649d448',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-3649d448',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-3649d448',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-db4ed3a5',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-d34ad7ad',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtAccountsIntElbEMGMT'
        }, {
            'Key': 'Name',
            'Value': 'mtAccountsIntElbEMGMT'
        }, {
            'Key': 'Description',
            'Value': 'MidTier Internal ELB for Accounts EMGMT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'ProdLine ExtElB Default ',
        'GroupName':
        'mtDefaultExtElbP',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-db623ca5',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-6d9fc113',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/MtProdine/5c2d0350-4c3d-11e8-8dbe-50a68a2012ba'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Defaul ProdLine'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'MtProdine'
        }, {
            'Key': 'Name',
            'Value': 'mtDefaultExtElbP'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtDefaultExtElbP'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'bind secgroup',
        'GroupName':
        'navadmins-secgroups-f4156492-bind-1URSVMHJAKSXR',
        'IpPermissions': [{
            'FromPort': 53,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 53,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-de6759a3',
        'IpPermissionsEgress': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '173.230.208.21/32'
            }, {
                'CidrIp': '173.230.215.21/32'
            }, {
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-f4156492/4382ec70-c64b-11e7-a229-503aca41a0c5'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-neteng-bind'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-f4156492'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'bind'
        }],
        'VpcId':
        'vpc-f4156492'
    }, {
        'Description':
        'sieoffices secgroup',
        'GroupName':
        'navadmins-secgroups-1721cf71-sieoffices-XLSHDAAYTMKI',
        'IpPermissions': [{
            'FromPort': 5439,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 5439,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-df3acea5',
                'UserId': '472973657150'
            }]
        }, {
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '43.148.16.0/22'
            }, {
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '173.230.196.15/32'
            }, {
                'CidrIp': '43.148.24.0/22'
            }, {
                'CidrIp': '173.230.196.25/32'
            }, {
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '43.148.20.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0d7ccd6e023b37adf',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '174.46.232.2/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f582678f',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            2049,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            2049,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-945594ea',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-df3acea5',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'sieoffices'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-1721cf71/e3e8b010-55f7-11e7-a592-50a686be738e'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-sieoffices'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-1721cf71'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'Test on awscli YM',
        'GroupName':
        'clitestYM',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-df886cae',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'evidenceserverESPINT',
        'GroupName':
        'ESPINTsgdef1-evidenceserverESPINT-X4Y4T0006GI2',
        'IpPermissions': [{
            'FromPort':
            7860,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            7860,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for evidenceserverESPINT',
                'GroupId': 'sg-e2147a9c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e0147a9e',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-evidence-server'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'evidenceserverESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercelivegamerresponderESPINT',
        'GroupName':
        'ESPINTsgdef1-commercelivegamerresponderESPINT-1CN0YBJA508LL',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercelivegamerresponderESPINT',
                'GroupId': 'sg-69127c17',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e1147a9f',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercelivegamerresponderESPINT'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-livegamer-responder'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Access to Core Services Prod',
        'GroupName':
        'CoreAccessProd',
        'IpPermissions': [{
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '173.230.196.25/32'
            }, {
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '173.230.196.15/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 8500,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8500,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 8300,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8302,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 8600,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8600,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e1f4a89f',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 8443,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.208.50.19/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8443,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 0,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ProdCore/66c65450-4bf3-11e8-b65f-50a68d01a68d'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ProdCore'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'CoreAccessProd'
        }, {
            'Key': 'Description',
            'Value': 'Prod Core Access'
        }, {
            'Key': 'Name',
            'Value': 'CoreAccessProd'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commerceserverESPINT',
        'GroupName':
        'ESPINTsgdef1-commerceserverESPINT-H404WXXEEAY8',
        'IpPermissions': [{
            'FromPort':
            9925,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9925,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-d3107ead',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9960,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9960,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-a6117fd8',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9930,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9930,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-71117f0f',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9928,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9928,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-69127c17',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            3850,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3850,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-46147a38',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-49147a37',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-69127c17',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-71117f0f',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-a96a04d7',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-ce6709b0',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-d3107ead',
                'UserId': '472973657150'
            }, {
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-fa127c84',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9980,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9980,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-fa127c84',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            4200,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4200,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-8f137df1',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            7860,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            7860,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-e0147a9e',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9990,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9990,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-49147a37',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9940,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9940,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-46147a38',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9910,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9910,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for commerceserverESPINT',
                'GroupId': 'sg-a9127cd7',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e2147a9c',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-server'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commerceserverESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'paymentmanagerESPINT',
        'GroupName':
        'ESPINTsgdef1-paymentmanagerESPINT-1IOMGRKRZSF6P',
        'IpPermissions': [{
            'FromPort':
            9925,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9925,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for paymentmanagerESPINT',
                'GroupId': 'sg-d3107ead',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9930,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9930,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for paymentmanagerESPINT',
                'GroupId': 'sg-71117f0f',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9928,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9928,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for paymentmanagerESPINT',
                'GroupId': 'sg-69127c17',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9980,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9980,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for paymentmanagerESPINT',
                'GroupId': 'sg-fa127c84',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            3750,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3750,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for paymentmanagerESPINT',
                'GroupId': 'sg-e2147a9c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            4200,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4200,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for paymentmanagerESPINT',
                'GroupId': 'sg-8f137df1',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9920,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9920,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for paymentmanagerESPINT',
                'GroupId': 'sg-e5147a9b',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9990,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9990,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for paymentmanagerESPINT',
                'GroupId': 'sg-49147a37',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9940,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9940,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for paymentmanagerESPINT',
                'GroupId': 'sg-46147a38',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e3147a9d',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-payment-manager'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'paymentmanagerESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'sieoffices secgroup',
        'GroupName':
        'tessg-sieoffices-1P7NFEKY35K91',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '43.148.24.0/22'
            }, {
                'CidrIp': '43.148.20.0/22'
            }, {
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '209.249.145.1/32'
            }, {
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '43.148.16.0/22'
            }, {
                'CidrIp': '173.230.196.15/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e46db99a',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'sieoffices'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key':
            'Name',
            'Value':
            'nav-prodadmin-metrics-nav-prodadmin-metrics-sieoffices'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commercepaymenttrustserverESPINT',
        'GroupName':
        'ESPINTsgdef1-commercepaymenttrustserverESPINT-1581GZCMIGTKJ',
        'IpPermissions': [{
            'FromPort':
            9920,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9920,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercepaymenttrustserverESPINT',
                'GroupId': 'sg-0a690774',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commercepaymenttrustserverESPINT',
                'GroupId': 'sg-706a040e',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commercepaymenttrustserverESPINT',
                'GroupId': 'sg-e3147a9d',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e5147a9b',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-payment-trust-server'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercepaymenttrustserverESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'nginx security group',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-nginx-1Q205X8PLWFJL',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '52.11.221.90/32'
            }, {
                'CidrIp': '54.69.116.37/32'
            }, {
                'CidrIp': '34.210.5.96/32'
            }, {
                'CidrIp': '52.89.229.109/32'
            }, {
                'CidrIp': '52.89.22.32/32'
            }, {
                'CidrIp': '174.46.232.2/32'
            }, {
                'CidrIp': '52.34.19.200/32'
            }, {
                'CidrIp': '52.89.20.175/32'
            }, {
                'CidrIp': '35.167.163.149/32'
            }, {
                'CidrIp': '52.23.49.54/32'
            }, {
                'CidrIp': '52.34.224.158/32'
            }, {
                'CidrIp': '52.34.253.0/32'
            }, {
                'CidrIp': '173.230.196.15/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-e60e6b98',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.211.220.15/32'
            }, {
                'CidrIp': '10.219.157.15/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e60e6b98',
        'IpPermissionsEgress': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-e60e6b98',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 443,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '173.230.216.215/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 443,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'nginx'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Name',
            'Value': 'ymtestVPC-nginx'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercehandleserverESPINT',
        'GroupName':
        'ESPINTsgdef1-commercehandleserverESPINT-15U3NNRVO5W84',
        'IpPermissions': [{
            'FromPort':
            3600,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3600,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercehandleserverESPINT',
                'GroupId': 'sg-e2147a9c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e6137d98',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercehandleserverESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-handleserver'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Internal MT ELB',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-mtAccountsIntElbENP-XPI1YIMUAL4S',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-4e37b730',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-4e37b730',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-4e37b730',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e737b799',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-1336b66d',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'Name',
            'Value': 'mtAccountsIntElbENP'
        }, {
            'Key': 'Description',
            'Value': 'MidTier Internal ELB for Accounts prod np'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtAccountsIntElbENP'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'grafana backend secgroup',
        'GroupName':
        'tessg-grafanaBackend-155G7OHSGD0DS',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-4f62b631',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e76db999',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'tessg'
        }, {
            'Key': 'name',
            'Value': 'ym'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/tessg/8aff21b0-34f8-11e8-9090-50a68af3968d'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'grafanaBackend'
        }, {
            'Key': 'Name',
            'Value': 'nav-prodadmin-grafana-backend'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'memcachednativePL',
        'GroupName':
        'memcachednativePL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e77d2699',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'memcachednativePL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Name',
            'Value': 'nav-memcachednative'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'mgsemailPL',
        'GroupName':
        'mgsemailPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e8401b96',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-mgsemail'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mgsemailPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'wallets secgroup',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-wallets-MLZO2YTSOSHP',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e9006597',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'wallets'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'Name',
            'Value': 'ymtestVPC-wallets'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'entitlementsESPINT',
        'GroupName':
        'ESPINTsgdef1-entitlementsESPINT-N6FU2S2O1KMW',
        'IpPermissions': [{
            'FromPort':
            5705,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            5705,
            'UserIdGroupPairs': [{
                'Description': 'First NP build rules for entitlementsESPINT',
                'GroupId': 'sg-2c157b52',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e9137d97',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-entitlements'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'entitlementsESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'transactionPL',
        'GroupName':
        'transactionPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e9401b97',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'transactionPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-transaction'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'NP  EIB Router',
        'GroupName':
        'eibRouterNP',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            61616,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-108bd56e',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e987d997',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ELB-ErtrProdLine/d7bb6d50-4c41-11e8-a66a-50a68af3968d'
        }, {
            'Key': 'Description',
            'Value': 'NP EIB ELB client security group'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibRouterNP'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ELB-ErtrProdLine'
        }, {
            'Key': 'Name',
            'Value': 'PL EIB router SG NP'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'EIB Router',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-eibRouterProdNP-1FU08JY3BNPVZ',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            61616,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-40b16b3e',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-e9b26897',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'EIB router SG'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibRouterProdNP'
        }, {
            'Key': 'Description',
            'Value': 'EIB ELB client security group'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'mgsxmbPL',
        'GroupName':
        'mgsxmbPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ea401b94',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-mgsxmb'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mgsxmbPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'autobotPL',
        'GroupName':
        'autobotPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-eb401b95',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'autobotPL'
        }, {
            'Key': 'Name',
            'Value': 'nav-autobot'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'paymentmanagerpciclient SG',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-paymentmanagerpci-1ARCCEDWHQNGI',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ec7ca692',
        'IpPermissionsEgress': [{
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-paymentmanagerpci'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'paymentmanagerpci'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTInternal MT ELB',
        'GroupName':
        'mtAccountMGMTYML-mtNativeIntElbEMGMT-8PN0S5BAKAHH',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-b048d5ce',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-b048d5ce',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-b048d5ce',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ee4bd690',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-3c4ed342',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'mtNativeIntElbEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtNativeIntElbEMGMT'
        }, {
            'Key': 'Description',
            'Value': 'MidTier Internal ELB for Native Enp'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'providerdataserverPL',
        'GroupName':
        'providerdataserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ee722990',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'providerdataserverPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Name',
            'Value': 'nav-providerdataserver'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercebibitserverpciSG',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-commercebibitserverpci-1PX24YYUO1WLB',
        'IpPermissions': [{
            'FromPort':
            9930,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9930,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ec7ca692',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-ee73a990',
        'IpPermissionsEgress': [{
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-sandbox-commercebibitserverpci'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercebibitserverpci'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'workflowPL',
        'GroupName':
        'workflowPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f0451e8e',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'workflowPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key': 'Name',
            'Value': 'nav-workflow'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTNginX MT Grc',
        'GroupName':
        'mtAccountMGMTYML-mtGrcNGXEMGMT-J5GF0YSRB7MG',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-7f48d501',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-a24fd2dc',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-7f48d501',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-a24fd2dc',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-7f48d501',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-a24fd2dc',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f04bd68e',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Description',
            'Value': 'MidTier External ELB for Grc Enp'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'Name',
            'Value': 'mtGrcNgxEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtGrcNGXEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'spgsESPINT',
        'GroupName':
        'ESPINTsgdef2-spgsESPINT-DLPCR4S20CMI',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f066088e',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-spgsESPINT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'spgsESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'consolegatewayPL',
        'GroupName':
        'consolegatewayPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f072298e',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-consolegateway'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'consolegatewayPL'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTEIB Router SG accepting from EIB CLient EMGMT',
        'GroupName':
        'mtAccountMGMTYML-eibElbMGMT-1GNX5D8FZ3BRM',
        'IpPermissions': [{
            'FromPort':
            61616,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            61616,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-984ed3e6',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-984ed3e6',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            3900,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3900,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-984ed3e6',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            4300,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4300,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-984ed3e6',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9500,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9500,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-984ed3e6',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8501,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8501,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-984ed3e6',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            3450,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3450,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-984ed3e6',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8500,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8500,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-984ed3e6',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f14bd68f',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-da4ed3a4',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibElbMGMT'
        }, {
            'Key': 'Description',
            'Value': 'EIB ELB security group'
        }, {
            'Key': 'Name',
            'Value': 'Eib-ELB-MGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'evidenceserverPL',
        'GroupName':
        'evidenceserverPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f172298f',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-evidenceserver'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'evidenceserverPL'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'Master group for Elastic MapReduce created on 2017-10-03T19:12:23.698Z',
        'GroupName':
        'ElasticMapReduce-master',
        'IpPermissions': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0d893e70',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-f175c28c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '205.251.233.48/29'
            }, {
                'CidrIp': '54.240.230.184/29'
            }, {
                'CidrIp': '54.240.230.240/29'
            }, {
                'CidrIp': '205.251.233.160/28'
            }, {
                'CidrIp': '205.251.234.32/28'
            }, {
                'CidrIp': '205.251.233.32/28'
            }, {
                'CidrIp': '54.240.230.176/29'
            }, {
                'CidrIp': '205.251.233.176/29'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8443,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            0,
            'IpProtocol':
            'udp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0d893e70',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-f175c28c',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            -1,
            'IpProtocol':
            'icmp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            -1,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0d893e70',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-f175c28c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f175c28c',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'sandbox test ssh server secgroup',
        'GroupName':
        'sshClientServer-sshServertestSb-19Y43WAVL6NXR',
        'IpPermissions': [{
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-3110c64f',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f1ba6b8f',
        'IpPermissionsEgress': [{
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/sshClientServer/a6fdd1d0-3553-11e8-a7aa-503f2a2cee1e'
        }, {
            'Key': 'Name',
            'Value': 'sshServertestSb'
        }, {
            'Key': 'name',
            'Value': 'testSG'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'sshServertestSb'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'sshClientServer'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        ' EMGTMT WAF default',
        'GroupName':
        'mtAccountMGMTYML-mtDefaultWafEMGMT-1HNPI7N0P0VUG',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-b148d5cf',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-b148d5cf',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-b148d5cf',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f24bd68c',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-7745d809',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'mtDefaultWafEMGMT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtDefaultWafEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'Description',
            'Value': 'MidTier WAF for Default Enp'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'navigatortaxESPINT',
        'GroupName':
        'ESPINTsgdef2-navigatortaxESPINT-DFBYXXUG7R2A',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f266088c',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-navigatortaxESPINT'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'navigatortaxESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'commercepaypallistenerPL',
        'GroupName':
        'commercepaypallistenerPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f3451e8d',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-commercepaypallistener'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercepaypallistenerPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef1'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef1/ae045070-4cb5-11e8-8820-500c32c86cd1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTNginX MT oauth',
        'GroupName':
        'mtAccountMGMTYML-mtoauthNGXEMGMT-YY8ZUA8VWP4N',
        'IpPermissions': [{
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-7c48d502',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-d64ed3a8',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8082,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-7c48d502',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-d64ed3a8',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            443,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            443,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-7c48d502',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-d64ed3a8',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f34bd68d',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for oauth Enp'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtoauthNGXEMGMT'
        }, {
            'Key': 'Name',
            'Value': 'mtoauthNgxEMGMT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'pricingESPINT',
        'GroupName':
        'ESPINTsgdef2-pricingESPINT-LQCA04W6F1OO',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f366088d',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'pricingESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-pricingESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'paymentmanagerPL',
        'GroupName':
        'paymentmanagerPL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f372298d',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.128.0/18'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'nav-paymentmanager'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/PLdef2/ff1b2cd0-4cb6-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'paymentmanagerPL'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'PLdef2'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EQA External MT EIB EMGT',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-mtAccountsExtElbEQA-X26QZXGJN0GL',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f471ec8a',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-bd76ebc3',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'Name',
            'Value': 'mtAccountsExtElbEQA'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtAccountsExtElbEQA'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Accounts EQA'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        ' EMGTExternal MT EIB',
        'GroupName':
        'mtAccountMGMTYML-mtNativeExtElbEMGMT-EH7CGSGST0XE',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f54bd68b',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-3c4ed342',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/mtAccountMGMTYML/3af9a9c0-4136-11e8-a65d-503ac9841ad1'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'mtAccountMGMTYML'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'mtNativeExtElbEMGMT'
        }, {
            'Key': 'Name',
            'Value': 'mtNativeExtElbEMGMT'
        }, {
            'Key': 'Description',
            'Value': 'MidTier External ELB for Native Enp'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'transactionESPINT',
        'GroupName':
        'ESPINTsgdef2-transactionESPINT-TCBBUMUR29PK',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f566088b',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'transactionESPINT'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-transactionESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'jenkins secgroup',
        'GroupName':
        'navadmins-secgroups-1721cf71-jenkins-ZHYBQ9DX12QU',
        'IpPermissions': [{
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.211.42.150/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-0f85d7bf451c2f9d1',
                'UserId': '472973657150'
            }, {
                'GroupId': 'sg-42528d3a',
                'PeeringStatus': 'deleted',
                'VpcId': 'vpc-970b3af3'
            }, {
                'GroupId': 'sg-f582678f',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8443,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.0.0/20'
            }, {
                'CidrIp': '43.148.16.0/22'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8443,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f582678f',
        'IpPermissionsEgress': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }, {
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }, {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.90/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 22,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 636,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.85/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 636,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 3269,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.32.85/32'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 3269,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'jenkins'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-1721cf71/e3e8b010-55f7-11e7-a592-50a686be738e'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-1721cf71'
        }, {
            'Key': 'Name',
            'Value': 'nav-sandbox-nav-sandbox-jenkins'
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'squid-proxy secgroup',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-squidProxy-69PQH9PIPLXB',
        'IpPermissions': [{
            'FromPort': 8300,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 8301,
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            3128,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3128,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-65655b18',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f7625c8a',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key': 'Name',
            'Value': 'ymtestVPC-squid-proxy'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'squidProxy'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'jchang-deleteme-test-sg',
        'GroupName':
        'jchang-deleteme-test-sg',
        'IpPermissions': [{
            'FromPort':
            22,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '43.148.12.85/32',
                'Description': 'jchang-desktop-ip'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            22,
            'UserIdGroupPairs': []
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f8613d89',
        'IpPermissionsEgress': [{
            'IpProtocol': '-1',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': []
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        ' EQA EIB Router SG accepting from EIB CLient EQA',
        'GroupName':
        'navadmins-secgroups-6ac8ba0c-eibElbQA-152FIB02ZGVGQ',
        'IpPermissions': [{
            'FromPort':
            61616,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            61616,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ba76ebc4',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            80,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            80,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ba76ebc4',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            3900,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3900,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ba76ebc4',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            4300,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            4300,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ba76ebc4',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9500,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9500,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ba76ebc4',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8501,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8501,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ba76ebc4',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            3450,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3450,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ba76ebc4',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            8500,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8500,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-ba76ebc4',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f874e986',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': [{
                'GroupId': 'sg-827be6fc',
                'UserId': '472973657150'
            }]
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': 'Eib-ELB-QA'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'navadmins-secgroups-6ac8ba0c'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/navadmins-secgroups-6ac8ba0c/725b1c70-c64b-11e7-9c21-50a686be7356'
        }, {
            'Key': 'Description',
            'Value': 'EIB ELB security group'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'eibElbQA'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'default VPC security group',
        'GroupName':
        'default',
        'IpPermissions': [{
            'IpProtocol':
            '-1',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'UserIdGroupPairs': [{
                'GroupId': 'sg-f9061282',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-f9061282',
        'IpPermissionsEgress': [{
            'IpProtocol':
            '-1',
            'IpRanges': [{
                'CidrIp': '10.0.0.0/8'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [{
                'PrefixListId': 'pl-68a54001'
            }],
            'UserIdGroupPairs': []
        }, {
            'FromPort':
            3306,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.142.76/32',
                'Description': ''
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            3306,
            'UserIdGroupPairs': []
        }, {
            'FromPort': 123,
            'IpProtocol': 'udp',
            'IpRanges': [{
                'CidrIp': '0.0.0.0/0'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 123,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'Name',
            'Value': ''
        }],
        'VpcId':
        'vpc-1721cf71'
    }, {
        'Description':
        'commercepaypalserverESPINT',
        'GroupName':
        'ESPINTsgdef1-commercepaypalserverESPINT-1Q9W9LKFXA1FM',
        'IpPermissions': [{
            'FromPort':
            8080,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            8080,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercepaypalserverESPINT',
                'GroupId': 'sg-a9117fd7',
                'UserId': '472973657150'
            }]
        }, {
            'FromPort':
            9980,
            'IpProtocol':
            'tcp',
            'IpRanges': [],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            9980,
            'UserIdGroupPairs': [{
                'Description':
                'First NP build rules for commercepaypalserverESPINT',
                'GroupId': 'sg-bd6907c3',
                'UserId': '472973657150'
            }, {
                'Description':
                'First NP build rules for commercepaypalserverESPINT',
                'GroupId': 'sg-e2147a9c',
                'UserId': '472973657150'
            }]
        }],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-fa127c84',
        'IpPermissionsEgress': [{
            'FromPort':
            0,
            'IpProtocol':
            'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17',
                'Description': 'NP Build Cidr Fule'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort':
            65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef1/c43491c0-441d-11e8-9ef5-503ac9ec2461'
        }, {
            'Key': 'Name',
            'Value': 'nav-commerce-paypal-server'
        }, {
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef1'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'commercepaypalserverESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }, {
        'Description':
        'paymentmanageradminESPINT',
        'GroupName':
        'ESPINTsgdef2-paymentmanageradminESPINT-1W2XC41OZWL37',
        'IpPermissions': [],
        'OwnerId':
        '472973657150',
        'GroupId':
        'sg-fc6b0582',
        'IpPermissionsEgress': [{
            'FromPort': 0,
            'IpProtocol': 'tcp',
            'IpRanges': [{
                'CidrIp': '10.242.0.0/17'
            }],
            'Ipv6Ranges': [],
            'PrefixListIds': [],
            'ToPort': 65535,
            'UserIdGroupPairs': []
        }],
        'Tags': [{
            'Key': 'aws:cloudformation:stack-name',
            'Value': 'ESPINTsgdef2'
        }, {
            'Key': 'Name',
            'Value': 'nav-paymentmanageradminESPINT'
        }, {
            'Key':
            'aws:cloudformation:stack-id',
            'Value':
            'arn:aws:cloudformation:us-west-2:472973657150:stack/ESPINTsgdef2/c43315b0-441e-11e8-9c7b-503f20f2adae'
        }, {
            'Key': 'aws:cloudformation:logical-id',
            'Value': 'paymentmanageradminESPINT'
        }],
        'VpcId':
        'vpc-6ac8ba0c'
    }],
    'ResponseMetadata': {
        'RequestId': 'de6c82c1-d02f-4960-981c-253813f947fa',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'content-type': 'text/xml;charset=UTF-8',
            'transfer-encoding': 'chunked',
            'vary': 'accept-encoding',
            'date': 'Thu, 16 May 2019 00:26:31 GMT',
            'server': 'AmazonEC2'
        },
        'RetryAttempts': 0
    }
}

ETM_FILTER_DATA1 = [{
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app1-sg-teststack-EtmESpintentanglementapp1Elb-A8LX211UERUF',
    'IpPermissions': [{
        'FromPort':
        443,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        443,
        'UserIdGroupPairs': [{
            'Description':
            'Entanglement rule for EtmESpintentanglementapp1Elb',
            'GroupId': 'sg-06d83ed1a616b44aa',
            'UserId': '472973657150'
        }]
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-02d46efde34216876',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp1Elb'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key': 'GitManifest',
        'Value': 'manifest/app1elb.yml'
    }, {
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app1-sg-teststack/86383a40-729b-11e9-bb0f-06cbb9434982'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp1Elb_472973657150'
    }, {
        'Key': 'Git tag',
        'Value': '1.0.0'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp1Elb'
    }, {
        'Key': 'Git Repo',
        'Value': 'https://github.sie.sony.com/SIE/entanglementapp1'
    }, {
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp1Elb'
    }, {
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app1-sg-teststack'
    }],
    'VpcId':
    'vpc-f4156492'
}, {
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app2-sg-teststack-EtmESpintentanglementapp2Elb-18VIV4YMTRFNH',
    'IpPermissions': [{
        'FromPort':
        8888,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        8888,
        'UserIdGroupPairs': [{
            'Description':
            'Entanglement rule for EtmESpintentanglementapp2Elb',
            'GroupId': 'sg-09356d729c2c2c28f',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        443,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        443,
        'UserIdGroupPairs': [{
            'Description':
            'Entanglement rule for EtmESpintentanglementapp2Elb',
            'GroupId': 'sg-0568226f2eb3a8b48',
            'UserId': '472973657150'
        }, {
            'Description':
            'Entanglement rule for EtmESpintentanglementapp2Elb',
            'GroupId': 'sg-06d83ed1a616b44aa',
            'UserId': '472973657150'
        }]
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-045b8899afb7d2aad',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp2Elb'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }, {
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp2Elb'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp2Elb_472973657150'
    }, {
        'Key': 'Git Repo',
        'Value': 'https://github.sie.sony.com/SIE/entanglementapp2'
    }, {
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app2-sg-teststack/ff0d1f00-729e-11e9-9d6a-02035744c0fa'
    }, {
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app2-sg-teststack'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp2Elb'
    }],
    'VpcId':
    'vpc-f4156492'
}, {
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app1-sg-teststack-EtmESpintentanglementapp1-EFZ8UT4EC8U1',
    'IpPermissions': [{
        'FromPort':
        8080,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        8080,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp1',
            'GroupId': 'sg-0568226f2eb3a8b48',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        53,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '8.8.8.0/24',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp1'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        53,
        'UserIdGroupPairs': []
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-0568226f2eb3a8b48',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp1'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app1-sg-teststack/86383a40-729b-11e9-bb0f-06cbb9434982'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp1_472973657150'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }, {
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app1-sg-teststack'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp1'
    }, {
        'Key': 'Git Repo',
        'Value': 'https://github.sie.sony.com/SIE/entanglementapp1'
    }, {
        'Key': 'GitManifest',
        'Value': 'manifests/app1manifest.yml'
    }, {
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp1'
    }, {
        'Key': 'Git tag',
        'Value': '1.0.0'
    }],
    'VpcId':
    'vpc-f4156492'
}, {
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app5-sg-teststack-EtmESpintentanglementapp5-1DZY06WQXYZF5',
    'IpPermissions': [{
        'FromPort':
        1521,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        1521,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp5',
            'GroupId': 'sg-0568226f2eb3a8b48',
            'UserId': '472973657150'
        }, {
            'Description': 'Entanglement rule for EtmESpintentanglementapp5',
            'GroupId': 'sg-061ef9f386035246c',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        8080,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        8080,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp5',
            'GroupId': 'sg-05fc8c5b3fb37fe0d',
            'UserId': '472973657150'
        }]
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-05fc8c5b3fb37fe0d',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp5'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp5'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp5'
    }, {
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app5-sg-teststack'
    }, {
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app5-sg-teststack/3ecf8340-767c-11e9-b0d6-0ad5109330ec'
    }, {
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key': 'Git Repo',
        'Value': 'entanglement_repo'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp5_472973657150'
    }],
    'VpcId':
    'vpc-f4156492'
}, {
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app2-sg-teststack-EtmESpintentanglementapp2-XW4JRQ3K626X',
    'IpPermissions': [{
        'FromPort':
        80,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        80,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp2',
            'GroupId': 'sg-061ef9f386035246c',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        443,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '10.215.0.0/24',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp2'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        443,
        'UserIdGroupPairs': []
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-061ef9f386035246c',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp2'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp2'
    }, {
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app2-sg-teststack/ff0d1f00-729e-11e9-9d6a-02035744c0fa'
    }, {
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app2-sg-teststack'
    }, {
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }, {
        'Key': 'Git Repo',
        'Value': 'entanglement_repo'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp2'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp2_472973657150'
    }],
    'VpcId':
    'vpc-f4156492'
}, {
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app4-sg-teststack-EtmESpintentanglementapp4-1J8JN7739A1F9',
    'IpPermissions': [{
        'FromPort':
        1521,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        1521,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp4',
            'GroupId': 'sg-09356d729c2c2c28f',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        8080,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        8080,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp4',
            'GroupId': 'sg-06d83ed1a616b44aa',
            'UserId': '472973657150'
        }]
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-06d83ed1a616b44aa',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp4'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app4-sg-teststack'
    }, {
        'Key': 'Git Repo',
        'Value': 'entanglement_repo'
    }, {
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app4-sg-teststack/c29bd5b0-729f-11e9-b90a-0a3d4b08165a'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp4'
    }, {
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp4'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp4_472973657150'
    }, {
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }],
    'VpcId':
    'vpc-f4156492'
}, {
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app3-sg-teststack-EtmESpintentanglementapp3-15ID8VVT1ZRC5',
    'IpPermissions': [{
        'FromPort':
        1521,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        1521,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp3',
            'GroupId': 'sg-0568226f2eb3a8b48',
            'UserId': '472973657150'
        }, {
            'Description': 'Entanglement rule for EtmESpintentanglementapp3',
            'GroupId': 'sg-06d83ed1a616b44aa',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        8080,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        8080,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp3',
            'GroupId': 'sg-09356d729c2c2c28f',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        443,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        443,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp3',
            'GroupId': 'sg-061ef9f386035246c',
            'UserId': '472973657150'
        }]
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-09356d729c2c2c28f',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp3'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp3'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }, {
        'Key': 'Git tag',
        'Value': '1.0.0'
    }, {
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app3-sg-teststack'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp3'
    }, {
        'Key': 'GitManifest',
        'Value': 'manifests/app3manifest.yml'
    }, {
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app3-sg-teststack/4f306910-729f-11e9-9bc4-0268a47876ba'
    }, {
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key': 'Git Repo',
        'Value': 'https://github.sie.sony.com/SIE/entanglementapp3'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp3_472973657150'
    }],
    'VpcId':
    'vpc-f4156492'
}]

ALL_ETM_SG_DATA = [{
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app1-sg-teststack-EtmESpintentanglementapp1Elb-A8LX211UERUF',
    'IpPermissions': [{
        'FromPort':
        443,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        443,
        'UserIdGroupPairs': [{
            'Description':
            'Entanglement rule for EtmESpintentanglementapp1Elb',
            'GroupId': 'sg-06d83ed1a616b44aa',
            'UserId': '472973657150'
        }]
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-02d46efde34216876',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp1Elb'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key': 'GitManifest',
        'Value': 'manifest/app1elb.yml'
    }, {
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app1-sg-teststack/86383a40-729b-11e9-bb0f-06cbb9434982'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp1Elb_472973657150'
    }, {
        'Key': 'Git tag',
        'Value': '1.0.0'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp1Elb'
    }, {
        'Key': 'Git Repo',
        'Value': 'https://github.sie.sony.com/SIE/entanglementapp1'
    }, {
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp1Elb'
    }, {
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app1-sg-teststack'
    }],
    'VpcId':
    'vpc-f4156492'
}, {
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app2-sg-teststack-EtmESpintentanglementapp2Elb-18VIV4YMTRFNH',
    'IpPermissions': [{
        'FromPort':
        8888,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        8888,
        'UserIdGroupPairs': [{
            'Description':
            'Entanglement rule for EtmESpintentanglementapp2Elb',
            'GroupId': 'sg-09356d729c2c2c28f',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        443,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        443,
        'UserIdGroupPairs': [{
            'Description':
            'Entanglement rule for EtmESpintentanglementapp2Elb',
            'GroupId': 'sg-0568226f2eb3a8b48',
            'UserId': '472973657150'
        }, {
            'Description':
            'Entanglement rule for EtmESpintentanglementapp2Elb',
            'GroupId': 'sg-06d83ed1a616b44aa',
            'UserId': '472973657150'
        }]
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-045b8899afb7d2aad',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp2Elb'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }, {
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp2Elb'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp2Elb_472973657150'
    }, {
        'Key': 'Git Repo',
        'Value': 'https://github.sie.sony.com/SIE/entanglementapp2'
    }, {
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app2-sg-teststack/ff0d1f00-729e-11e9-9d6a-02035744c0fa'
    }, {
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app2-sg-teststack'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp2Elb'
    }],
    'VpcId':
    'vpc-f4156492'
}, {
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app1-sg-teststack-EtmESpintentanglementapp1-EFZ8UT4EC8U1',
    'IpPermissions': [{
        'FromPort':
        8080,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        8080,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp1',
            'GroupId': 'sg-0568226f2eb3a8b48',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        53,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '8.8.8.0/24',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp1'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        53,
        'UserIdGroupPairs': []
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-0568226f2eb3a8b48',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp1'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app1-sg-teststack/86383a40-729b-11e9-bb0f-06cbb9434982'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp1_472973657150'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }, {
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app1-sg-teststack'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp1'
    }, {
        'Key': 'Git Repo',
        'Value': 'https://github.sie.sony.com/SIE/entanglementapp1'
    }, {
        'Key': 'GitManifest',
        'Value': 'manifests/app1manifest.yml'
    }, {
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp1'
    }, {
        'Key': 'Git tag',
        'Value': '1.0.0'
    }],
    'VpcId':
    'vpc-f4156492'
}, {
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app5-sg-teststack-EtmESpintentanglementapp5-1DZY06WQXYZF5',
    'IpPermissions': [{
        'FromPort':
        1521,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        1521,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp5',
            'GroupId': 'sg-0568226f2eb3a8b48',
            'UserId': '472973657150'
        }, {
            'Description': 'Entanglement rule for EtmESpintentanglementapp5',
            'GroupId': 'sg-061ef9f386035246c',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        8080,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        8080,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp5',
            'GroupId': 'sg-05fc8c5b3fb37fe0d',
            'UserId': '472973657150'
        }]
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-05fc8c5b3fb37fe0d',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp5'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp5'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp5'
    }, {
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app5-sg-teststack'
    }, {
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app5-sg-teststack/3ecf8340-767c-11e9-b0d6-0ad5109330ec'
    }, {
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key': 'Git Repo',
        'Value': 'entanglement_repo'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp5_472973657150'
    }],
    'VpcId':
    'vpc-f4156492'
}, {
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app2-sg-teststack-EtmESpintentanglementapp2-XW4JRQ3K626X',
    'IpPermissions': [{
        'FromPort':
        80,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        80,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp2',
            'GroupId': 'sg-061ef9f386035246c',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        443,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '10.215.0.0/24',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp2'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        443,
        'UserIdGroupPairs': []
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-061ef9f386035246c',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp2'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp2'
    }, {
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app2-sg-teststack/ff0d1f00-729e-11e9-9d6a-02035744c0fa'
    }, {
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app2-sg-teststack'
    }, {
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }, {
        'Key': 'Git Repo',
        'Value': 'entanglement_repo'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp2'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp2_472973657150'
    }],
    'VpcId':
    'vpc-f4156492'
}, {
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app4-sg-teststack-EtmESpintentanglementapp4-1J8JN7739A1F9',
    'IpPermissions': [{
        'FromPort':
        1521,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        1521,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp4',
            'GroupId': 'sg-09356d729c2c2c28f',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        8080,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        8080,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp4',
            'GroupId': 'sg-06d83ed1a616b44aa',
            'UserId': '472973657150'
        }]
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-06d83ed1a616b44aa',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp4'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app4-sg-teststack'
    }, {
        'Key': 'Git Repo',
        'Value': 'entanglement_repo'
    }, {
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app4-sg-teststack/c29bd5b0-729f-11e9-b90a-0a3d4b08165a'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp4'
    }, {
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp4'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp4_472973657150'
    }, {
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }],
    'VpcId':
    'vpc-f4156492'
}, {
    'Description':
    'EC2 Instance Security Group created by Entanglement',
    'GroupName':
    'app3-sg-teststack-EtmESpintentanglementapp3-15ID8VVT1ZRC5',
    'IpPermissions': [{
        'FromPort':
        1521,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        1521,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp3',
            'GroupId': 'sg-0568226f2eb3a8b48',
            'UserId': '472973657150'
        }, {
            'Description': 'Entanglement rule for EtmESpintentanglementapp3',
            'GroupId': 'sg-06d83ed1a616b44aa',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        8080,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        8080,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp3',
            'GroupId': 'sg-09356d729c2c2c28f',
            'UserId': '472973657150'
        }]
    }, {
        'FromPort':
        443,
        'IpProtocol':
        'tcp',
        'IpRanges': [],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        443,
        'UserIdGroupPairs': [{
            'Description': 'Entanglement rule for EtmESpintentanglementapp3',
            'GroupId': 'sg-061ef9f386035246c',
            'UserId': '472973657150'
        }]
    }],
    'OwnerId':
    '472973657150',
    'GroupId':
    'sg-09356d729c2c2c28f',
    'IpPermissionsEgress': [{
        'FromPort':
        0,
        'IpProtocol':
        'tcp',
        'IpRanges': [{
            'CidrIp':
            '127.0.0.1/32',
            'Description':
            'Entanglement rule for EtmESpintentanglementapp3'
        }],
        'Ipv6Ranges': [],
        'PrefixListIds': [],
        'ToPort':
        65335,
        'UserIdGroupPairs': []
    }],
    'Tags': [{
        'Key': 'Name',
        'Value': 'Etm-Spint-E-entanglementapp3'
    }, {
        'Key': 'Environment',
        'Value': 'E'
    }, {
        'Key': 'Git tag',
        'Value': '1.0.0'
    }, {
        'Key': 'aws:cloudformation:stack-name',
        'Value': 'app3-sg-teststack'
    }, {
        'Key': 'aws:cloudformation:logical-id',
        'Value': 'EtmESpintentanglementapp3'
    }, {
        'Key': 'GitManifest',
        'Value': 'manifests/app3manifest.yml'
    }, {
        'Key':
        'aws:cloudformation:stack-id',
        'Value':
        'arn:aws:cloudformation:us-west-2:472973657150:stack/app3-sg-teststack/4f306910-729f-11e9-9bc4-0268a47876ba'
    }, {
        'Key': 'PCI Scope',
        'Value': 'CAT2'
    }, {
        'Key': 'Git Repo',
        'Value': 'https://github.sie.sony.com/SIE/entanglementapp3'
    }, {
        'Key': 'Service',
        'Value': 'EtmESpint_entanglementapp3_472973657150'
    }],
    'VpcId':
    'vpc-f4156492'
}]
