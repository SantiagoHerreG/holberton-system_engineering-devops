# installs a software from a Puppet manifest

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem'
}
