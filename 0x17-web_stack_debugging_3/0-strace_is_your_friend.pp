# puppet file that replaces a string in a file

exec { 'fix-wordpress':
  command => "/bin/sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php"
}
