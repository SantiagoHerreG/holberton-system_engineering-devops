# Adds lines to the config file for ssh

file { 'Turn off passwd auth and declare identity file':
  ensure  => file,
  path    => '/home/vagrant/.ssh/config',
  content => "Host *\n  PasswordAuthentication no\n  IdentityFile ~/.ssh/holberton\n"
}
