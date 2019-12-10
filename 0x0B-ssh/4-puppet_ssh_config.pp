# Adds lines to the config file for ssh

file_line { 'Declare identity file':
  path => '/home/vagrant/.ssh/config',
  line => "IdentityFile ~/.ssh/holberton\n",
}
file_line { 'Turn off passwd auth':
  path => '/home/vagrant/.ssh/config',
  line => "PasswordAuthentication no\n",
}
