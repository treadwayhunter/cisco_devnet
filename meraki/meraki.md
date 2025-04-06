# Meraki Practice
### Meraki Dashboard
The Meraki Dashboard appears to be extremely intuitive to use.
I launched the reserved sandbox, and I was able to quickly create a new admin account using my own email. Even better, I don't need to use a VPN to do any of this like I do other networks, since all of this stuff is hosted in the cloud.

### API Key
Technically, it's bad to have the api key stored plainly, but this is only for practice. I can use this API key to make requests to the Meraki API.

### What I've Learned So Far
Meraki has their own meraki python module, which can help streamline some things, but I'll want to see some documentation.
From the requests library, I was able to read the API DOC and create a new network in the organization, and successfully see it in the drop down menu on the Meraki dashboard.
When meraki says "single pane of glass" these jokers mean it. It looks like a user can be a member of multiple organizations, and access anything from these orgs.

I can get an organization, get the existing networks, then create a new network. 