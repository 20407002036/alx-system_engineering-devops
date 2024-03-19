#  This will kill a process

exec { 'kill_killmenow_process':
  command     => 'sudo pkill -f killmenow',
  path        => ['/bin', '/usr/bin'], 
  refreshonly => true,                  # Only execute when triggered explicitly
  logoutput   => true,                  # Log the output of the command
}

