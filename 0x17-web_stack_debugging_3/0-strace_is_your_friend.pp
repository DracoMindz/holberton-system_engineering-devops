# Fix Apache then automate with puppet include path
exec {'replace phpp with php':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}
