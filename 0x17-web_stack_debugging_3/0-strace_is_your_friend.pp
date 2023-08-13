file { '/etc/apache2/apache.conf':
  ensure => file,
  source => 'puppet:///modules/apache/apache.conf',
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
}
