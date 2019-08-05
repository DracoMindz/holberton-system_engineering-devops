#manifest kills process
exec { "killmenow":
        command => "/usr/bin/pkill -x killmenow",
}
