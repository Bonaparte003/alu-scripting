#!/usr/bin/env ruby
# finds a regular expression that will mach the above cases
puts ARGV[0].scan(/hbt{2,5}n/).join
