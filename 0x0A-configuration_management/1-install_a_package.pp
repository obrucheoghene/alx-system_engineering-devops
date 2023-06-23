# install flask from pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install-flask':
  command => 'pip3 install flask',
  path    => ['/usr/bin', '/usr/local/bin'],
  require => Package['python3-pip'],
}
