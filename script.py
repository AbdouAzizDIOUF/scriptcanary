import subprocess

# Chemins des fichiers journaux système
ftp_log_file = '/var/log/vsftpd.log'
ssh_log_file = '/var/log/auth.log'
http_log_file = '/var/log/apache2/access.log'

# Commandes pour extraire les adresses IP à partir des fichiers journaux
ftp_command = f'grep "FAIL LOGIN" {ftp_log_file} | awk \'{{print $NF}}\''
ssh_command = f'grep "Failed password" {ssh_log_file} | awk \'{{print $NF}}\''
http_command = f'awk \'{{print $1}}\' {http_log_file}'

# Exécution des commandes et récupération des résultats dans des variables
ftp_output = subprocess.check_output(ftp_command, shell=True, text=True)
ssh_output = subprocess.check_output(ssh_command, shell=True, text=True)
http_output = subprocess.check_output(http_command, shell=True, text=True)

# Affichage des résultats
print('IPs des tentatives de connexion FTP :')
print(ftp_output)
print('\nIPs des tentatives de connexion SSH :')
print(ssh_output)
print('\nIPs des tentatives de connexion HTTP :')
print(http_output)
