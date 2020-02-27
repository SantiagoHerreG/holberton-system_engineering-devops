# puppet file that replaces a string in a file

exec { 'fix--for-nginx':
  command => "/bin/sed -i 's/worker_processes 4/worker_processes 8/g' /etc/nginx/nginx.conf && /etc/init.d/nginx restart"
}
