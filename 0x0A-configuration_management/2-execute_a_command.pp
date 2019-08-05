#manifest kills process
exec { "killmenow":
    path => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command => "ps -ef | grep nrpe | grep -v pts/1 | /bin/awk '{print \$2}' | xargs pkill -9",
    provider => 'shell',
    subscribe => File["/root/Backup/deploy"],
    refreshonly => true,
}
