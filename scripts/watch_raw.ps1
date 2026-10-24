# Watch raw/ and run the ingest pipeline after 30 seconds of quiet.
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root
$Raw = Join-Path $Root "raw"
if (-not (Test-Path $Raw)) {
    throw "找不到 raw 目录：$Raw"
}

$state = [hashtable]::Synchronized(@{ LastEvent = [datetime]::MinValue })
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $Raw
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true
$watcher.NotifyFilter = [IO.NotifyFilters]"FileName, LastWrite, Size"
$onEvent = {
    $Event.MessageData.LastEvent = Get-Date
}
Register-ObjectEvent -InputObject $watcher -EventName Created -MessageData $state -Action $onEvent | Out-Null
Register-ObjectEvent -InputObject $watcher -EventName Changed -MessageData $state -Action $onEvent | Out-Null
Register-ObjectEvent -InputObject $watcher -EventName Renamed -MessageData $state -Action $onEvent | Out-Null

Write-Output "正在监视 $Raw 。新增文件安静 30 秒后会更新 wiki、提交并推送。"
python scripts/ingest_raw.py --commit --push
if ($LASTEXITCODE -eq 2) {
    Write-Output "基线或首轮收录因疑似口令而停止。处理完该文件后，下一次变更会再试。"
}

while ($true) {
    Start-Sleep -Seconds 2
    $last = $state.LastEvent
    if ($last -eq [datetime]::MinValue) {
        continue
    }
    if (((Get-Date) - $last).TotalSeconds -lt 30) {
        continue
    }
    $state.LastEvent = [datetime]::MinValue
    Write-Output "$(Get-Date -Format o) 开始收录"
    python scripts/ingest_raw.py --commit --push
    if ($LASTEXITCODE -ne 0) {
        Write-Output "收录退出码 $LASTEXITCODE"
    }
}
