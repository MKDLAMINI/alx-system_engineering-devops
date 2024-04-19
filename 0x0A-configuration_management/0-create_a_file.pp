# This code will create the file name school inside the /tmp Directory
file { '/tmp/school' :
  ensure  => file,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
