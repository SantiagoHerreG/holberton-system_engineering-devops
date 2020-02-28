# puppet file that replaces a string in a file for allowing a user to have 1000 files open

exec { 'change-os-configuration-for-holberton-user':
  command => "/bin/sed -i 's/holberton hard nofile 5/holberton hard nofile 1000/g' /etc/security/limits.conf && /bin/sed -i 's/holberton soft nofile 4/holberton hard nofile 1000/g' /etc/security/limits.conf"
}
