#Creates a file
file {'config-file':
  ensure  => file,
  path    => '/tmp/holberton',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I Love Puppet',
}