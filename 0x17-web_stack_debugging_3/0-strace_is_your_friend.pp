# Write a script that fixes bad phpp ext to php

exec { 'fix-wordpress':
  command => 'sed -i \'s/phpp/php/g\' /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
