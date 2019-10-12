the default routersploit project cannot scan for multiple ips. This repository implement this function.
Usage:
put your target ip to file 'ip_range', an ip per line, and run command 'sudo ./multi_ip_scanner.sh', the results will be stored to folder 'scanner_output'
Implementation:
modified the origin function start(self, argv) in non_interactive_scanner.py to fit this new feature.
Others:
modified rsf project for study purpose, don't use it for evil. Any Questions or problem, pls submit in ISSUE