# Executes a command for killing a process in bash

exec { 'kill process':
  path    => '/usr/bin/',
  cwd     => '/tmp/',
  command => 'pkill killmenow'
}
