# ssh config file using puppet

file { '~/.ssh/config':
  ensure  => file,
  content => "Host *\n\
              Hostname *\n\
              User ubuntu\n\
              IdentityFile ~/.ssh/school\n\
              PreferredAuthentications publickey\n\
              PasswordAuthentication no\n",
}
