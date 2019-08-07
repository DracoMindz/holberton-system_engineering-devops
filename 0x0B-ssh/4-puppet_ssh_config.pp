# configuration file to connect to a server without typing password
file_line{'disable password login':
    ensure => 'absent',
    line   => 'PasswordAuthentication yes',
    path   => '/etc/ssh/sshd_config',
    key    => '~/.ssh/holberton'
}