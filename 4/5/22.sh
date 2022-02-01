#!/usr/bin/expect -f 
set pid [lindex $argv 0]
set skan1 [lindex $argv 1]
spawn scanmem $pid
expect ">"
send -- "$skan1\r"
sleep 3
set op $skan1
expect '~$'
while { $skan1 == $op } {
set timeout 2
#spawn echo -n ravnie
set op1 [open log/1.log]
set op [read $op1]
close $op1
} 
set op2 [open log/1.log]
set skan2 [read $op2]
send -- "$skan2\r"
#expect '~$'

close $op2
sleep 3
send -- "list\r"
sleep 4
send -- "exit\r"
expect eof
