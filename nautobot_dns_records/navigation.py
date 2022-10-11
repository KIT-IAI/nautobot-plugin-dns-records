"""Navigation Items to add to Nautobot for nautobot_dns_records."""

from nautobot.core.apps import NavMenuTab, NavMenuGroup, NavMenuItem

menu_items = (
    NavMenuTab(
        name="IPAM",
        groups=(
            NavMenuGroup(
                name="DNS",
                weight=800,
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:address_records_list", name="Address Records", permissions=[]
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:txt_records_list", name="TXT Records", permissions=[]
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:loc_records_list", name="LOC Records", permissions=[]
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:cname_records_list", name="CNAME Records", permissions=[]
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:ptr_records_list", name="PTR Records", permissions=[]
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:sshfp_records_list", name="SSHFP Records", permissions=[]
                    ),
                ),
            ),
        ),
    ),
)
