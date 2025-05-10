terraform {
  required_providers {
    iosxe = {
      source  = "CiscoDevNet/iosxe"
      version = ">= 0.3.3"
    }
  }
}

provider "iosxe" {
  username = "developer"
  password = "C1sco12345"
  url      = "https://10.10.20.48"
}

##########################################
# Should not need to change below here ! #
##########################################
variable source_address {
    type = string
    default = "1.1.1.1"
    description = "Source address" 
}

variable receiver_ip {
    type = string
    default = "1.1.1.1"
    description = "Receiver IP" 
}

variable receiver_port  {
    type = string
    default = "57500"
    description = "Port to send data to" 
}