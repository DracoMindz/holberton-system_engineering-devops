#install and configuration of nginx with puppet
# redirection included
package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
    content => 'Holberton School',
}

file_line { 'snoopy':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _',
  line   => 'rewrite ^/redirect_me $https://www.youtube.com/watch?v=WZ9W0nIonnM\n\t}";permanent;',
}


service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}