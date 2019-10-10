# Fix Apache then automate with puppet include path
exec {'replace phpp with php':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}
