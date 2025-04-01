
# Challenge Name: Guthib
## Category: Digital Forensics

## Description

Oops looks like i made a wrong commit there that no body should see, luckily I fixed it in time ;)
  
---
## Approach

You were given a zip file for a .git directory, upon opening git logs, you'll find two commits :

```bash
>>>>  ~/RamadhanCTF/foren/guthib/git  git:(master) git log

commit 41f3e12665dac8df435bd5d632102e6ffc368504 (HEAD -> master)
Author: Kakarot <kakarot@e-spark.com>
Date:   Thu Mar 27 02:12:34 2025 +0100

    Read the note please, thank you.

commit d1f4e837bfbccde47e8f878fb058d44a1ec24e7c
Author: Kakarot <kakarot@e-spark.com>
Date:   Thu Mar 27 02:09:21 2025 +0100

    Flag
```

Opening the commit with the message flag will just show a fake flag, the other one contained a note : 

```bash
>>>>  ~/RamadhanCTF/foren/guthib/git  git:(master) git show 41f3e12665dac8df435bd5d632102e6ffc368504

commit 41f3e12665dac8df435bd5d632102e6ffc368504 (HEAD -> master)
Author: Kakarot <kakarot@e-spark.com>
Date:   Thu Mar 27 02:12:34 2025 +0100

    Read the note please, thank you.

diff --git a/note.md b/note.md
new file mode 100644
index 0000000..54b85c9
--- /dev/null
+++ b/note.md
@@ -0,0 +1 @@
+I sumbitted another flag earlier, but then I deleted that commit because it wasn't supposed to be there.
(END)

```

## Solver

From that note we now know that a commit was deleted that might have contained the flag, all you need to do is restore that deleted commit, you can do it in many ways and one of them is using this command :

```bash
>>>>  ~/RamadhanCTF/foren/guthib/git  git:(master) git fsck --lost-found                            
Checking object directories: 100% (256/256), done.
dangling commit a977b237bbb8abf392a0127bd04f671e1699e2fa
```

You can see that it found a commit that wasn't shown in the git logs, now you can just show that commit and you'll find the flag :

```bash
>>>>  ~/RamadhanCTF/foren/guthib/git  git:(master) git show a977b237bbb8abf392a0127bd04f671e1699e2fa

commit a977b237bbb8abf392a0127bd04f671e1699e2fa
Author: Kakarot <kakarot@e-spark.com>
Date:   Thu Mar 27 02:09:36 2025 +0100

    Real Flag

diff --git a/flag.txt b/flag.txt
new file mode 100644
index 0000000..f7ce687
--- /dev/null
+++ b/flag.txt
@@ -0,0 +1 @@
+Spark{y0u_c0uld_st1ll_f1nd_m3?_1m_1mpr3553d}
\ No newline at end of file
(END)
```

**Flag** : **Spark{y0u_c0uld_st1ll_f1nd_m3?_1m_1mpr3553d}**
