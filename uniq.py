# output only one occurence of an array
groups = ['awx_my_admins','awx_my_users','awx_my_admins']
printed_groups = []

for group in groups:
        found = False
        for printed_group in printed_groups:
            if group == printed_group:
                found = True
        if found == False:
            printed_groups.append(group)

for printed_group in printed_groups:
    print(printed_group)