# Voice (one take, kept as spoken), music, render and final copies for one or more episodes, in order.
# Usage: .\produire.ps1 <episode> [<episode> ...]   (FAL_KEY in env; takes and the Margot line come from the episode)
param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Episodes)
Set-Location $PSScriptRoot
foreach ($ep in $Episodes) {
    $d = python -c "import comptes; print(comptes.root(comptes.EPISODES['$ep']) / '$ep')"
    # the line compared to the others: Margot's introduction (nutrition), else the line after the opening
    $line = python -c "import comptes; e = comptes.EPISODES['$ep']; print(next(iter(e.get('cards', {})), 1))"
    "=== $ep"
    # one take (cost), or every take already made if there are several
    $takes = python -c "import comptes; e = comptes.EPISODES['$ep']; p = comptes.root(e) / '$ep' / 'voix' / 'prises'; print(max(e.get('takes', 1), len(list(p.glob('take_*.wav')))))"
    python prises.py $ep $takes $line 2>&1 | Select-String "take \d: |kept|rror|skipped"
    # the episode's engine (grok by default; h3 for full-motion shots, 2.2x cheaper per second)
    python assets.py $ep anim 2>&1 | Select-String "ERROR|ok \(" # chained stills (free when every clip exists)
    python musique.py $ep lyria 2>&1 | Select-Object -Last 1
    Copy-Item "$d\music_lyria.mp3" "$d\music.mp3" -Force
    $out = python render_video.py $ep 2>&1 | Select-Object -Last 1
    $out
    # a failed render must never pass the old video off as the new one (O01/O02 v5: « Pour » not found, unnoticed)
    if ("$out" -notmatch "^ok ") { "RENDER FAILED for ${ep}: the final video was NOT updated"; continue }
    python finir.py $ep  # final video, caption and loudness, named in Python (accents)
}
