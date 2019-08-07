# configuration file to connect to a server without typing password
file_line{'disable_password_login':
    path   => '/etc/ssh/sshd_config',
    line   => 'PasswordAuthentication yes',
    ensure => 'absent'
    match  => 'PasswordAuthentication yes',
}

file_line{'use new private key':
    path   => '~/.ssh/'
    line   => 'Identity'
    ensure => '~/.ssh/holberton'
    match  => 'Identity'
}