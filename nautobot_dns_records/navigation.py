"""Navigation Items to add to Nautobot for nautobot_dns_records."""

from nautobot.apps.ui import NavMenuTab, NavMenuGroup, NavMenuItem

menu_items = (
    NavMenuTab(
        name="DNS",
        weight=350,
        groups=[
            NavMenuGroup(
                name="Records",
                weight=100,
                items=[
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:addressrecord_list",
                        name="Address Records",
                        permissions=["nautobot_dns_records.view_addressrecord"],
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:txtrecord_list",
                        name="TXT Records",
                        permissions=["nautobot_dns_records.view_txtrecord"],
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:locrecord_list",
                        name="LOC Records",
                        permissions=["nautobot_dns_records.view_locrecord"],
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:cnamerecord_list",
                        name="CNAME Records",
                        permissions=["nautobot_dns_records.view_cnamerecord"],
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:ptrrecord_list",
                        name="PTR Records",
                        permissions=["nautobot_dns_records.view_ptrrecord"],
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:sshfprecord_list",
                        name="SSHFP Records",
                        permissions=["nautobot_dns_records.view_sshfprecord"],
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_dns_records:srvrecord_list",
                        name="SRV Records",
                        permissions=["nautobot_dns_records.view_srvrecord"],
                    ),
                ],
            ),
        ],
    ),
)
