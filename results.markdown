# Some useful informations about the system
```sh
********************************************
*            ADB BROADBAND                 *
*                                          *
*      WARNING: Authorised Access Only     *
********************************************

Welcome
ADB# system shell


BusyBox v1.17.3 (2013-07-05 16:00:10 CEST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

/ $
```

## Uname -a
```sh
/ $ uname -a
Linux localhost 2.6.30 #1 SMP PREEMPT Fri Jul 5 16:26:59 CEST 2013 mips GNU/Linux
```

## Netstat
```sh
/ $ netstat -lapute
netstat: can't scan /proc - are you root?
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 localhost.:9034         0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -
tcp        0      0 192.168.1.1:22          0.0.0.0:*               LISTEN      -
tcp        0      0 192.168.1.1:23          0.0.0.0:*               LISTEN      -
tcp        0      0 192.168.1.1:23          192.168.1.12:40125      ESTABLISHED -
tcp        0      0 192.168.1.1:23          192.168.1.12:40124      TIME_WAIT   -
udp        0      0 0.0.0.0:15000           0.0.0.0:*                           -
udp        0      0 0.0.0.0:53              0.0.0.0:*                           -
udp        0   1504 192.168.1.1:5060        0.0.0.0:*                           -
udp        0      0 0.0.0.0:1900            0.0.0.0:*                           -
udp        0      0 :::53                   :::*                                -
```

## Ps
```
/ $ ps aux
  PID USER       VSZ STAT COMMAND
    1 0         1320 S    init
    2 0            0 SW<  [kthreadd]
    3 0            0 SW<  [migration/0]
    4 0            0 SW   [sirq-high/0]
    5 0            0 SW   [sirq-timer/0]
    6 0            0 SW   [sirq-net-tx/0]
    7 0            0 SW   [sirq-net-rx/0]
    8 0            0 SW   [sirq-block/0]
    9 0            0 SW   [sirq-tasklet/0]
   10 0            0 SW   [sirq-sched/0]
   11 0            0 SW   [sirq-hrtimer/0]
   12 0            0 RW   [sirq-rcu/0]
   13 0            0 SW<  [migration/1]
   14 0            0 SW   [sirq-high/1]
   15 0            0 SW   [sirq-timer/1]
   16 0            0 SW   [sirq-net-tx/1]
   17 0            0 SW   [sirq-net-rx/1]
   18 0            0 SW   [sirq-block/1]
   19 0            0 SW   [sirq-tasklet/1]
   20 0            0 SW   [sirq-sched/1]
   21 0            0 SW   [sirq-hrtimer/1]
   22 0            0 SW   [sirq-rcu/1]
   23 0            0 SW<  [events/0]
   24 0            0 SW<  [events/1]
   25 0            0 SW<  [khelper]
   28 0            0 SW<  [async/mgr]
   62 0            0 SW<  [kblockd/0]
   63 0            0 SW<  [kblockd/1]
   69 0            0 SW<  [khubd]
   95 0            0 SW   [pdflush]
   96 0            0 SW   [pdflush]
   97 0            0 SWN  [kswapd0]
   98 0            0 SW<  [crypto/0]
   99 0            0 SW<  [crypto/1]
  130 0            0 SW<  [mtdblockd]
  205 0            0 SWN  [jffs2_gcd_mtd7]
  245 0         1320 S    init
  248 0         1932 S    logd
  251 0         1308 S    klogd -c3
  263 0          832 S    ec
  328 0         2308 S    cm
  355 0            0 SW   [bcmsw]
  356 0            0 SW<  [linkwatch]
  358 0            0 SW   [bcmsw_timer]
  430 0            0 SW   [dsl0]
 1737 65534     2196 S    nhttpd -c /tmp/nhttpd.conf
 1866 0          756 S    dns
 2140 0          736 S    /bin/wpspbc
 2229 0         1132 S    dropbear -P /tmp/dropbear-local.pid -l 20 -p 192.168
 2389 0         1312 S    telnetd Local -u 20 -b 192.168.1.1:23 -p 23 -I 300
 2828 0         1656 S    /bin/sh /etc/rc.common /etc/rc.d/S11services.sh boot
 2934 0          752 S    minissdpd -i 192.168.1.1
 3003 0          884 S    ec
 3083 0         1316 S    /bin/sh /etc/ah/printk_dump.sh
 3232 0         3552 R    voip
 3234 0         3552 S    voip
 3235 0         3552 S    voip
 3236 0         3552 S    voip
 3237 0         3552 S    voip
 3238 0         3552 S    voip
 3239 0         3552 S    voip
 3241 0            0 SW<  [aoRT]
 3242 0         3552 S    voip
 3303 0            0 SW<  [HTSK]
 3341 0            0 SW<  [HRTBEAT]
 3342 0            0 SW<  [VRGDISP]
 3343 0            0 SW<  [HCAS]
 3344 0            0 SW<  [ISTW]
 3345 0            0 SW   [YAPS_Dsp_Event_]
 3346 0            0 SW   [YAPS_Dsp_Data_R]
 4852 1001      1688 S    -clish
 4853 1001      1688 S    -clish
 4854 1001      1688 S    -clish
 4856 1001      1316 S    sh -c cd /; ENV=/etc/clish/prod/env.sh /bin/ash
 4857 1001      1316 S    /bin/ash
 5343 0         1304 S    sleep 30
 5345 0         1304 S    sleep 10
 5346 1001      1312 R    ps aux
/ $
```

## List of SUID executables
- `/old_root/bin/busybox`
- `/old_root/bin/ledctl`
- `/old_root/bin/swc-backup`
- `/old_root/bin/wlctl`
- `/old_root/bin/wlctl_scan`
- `/old_root/bin/wlctl_scanresults`
- `/old_root/usr/sbin/hostapd_cli`
- `/old_root/usr/sbin/tcpdump`
- `/bin/busybox`
- `/bin/ledctl`
- `/bin/swc-backup`
- `/bin/wlctl`
- `/bin/wlctl_scan`
- `/bin/wlctl_scanresults`
- `/usr/sbin/hostapd_cli`
- `/usr/sbin/tcpdump`
