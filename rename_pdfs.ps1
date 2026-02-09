# Script doi ten PDF va cap nhat HTML
# Chay tu PowerShell

# Lay duong dan thu muc (dung Path object de xu ly)
$folderPath = "d:\hoc\code\htmml\project1\de\de tieng anh"
$htmlFile = "d:\hoc\code\htmml\project1\index_FIXED.html"

Write-Host "=== Doi Ten File PDF ===" -ForegroundColor Green

# Lay danh sach file PDF va sap xep theo so
$files = Get-ChildItem -Path $folderPath -Filter "*.pdf" | Sort-Object -Property Name

$mappings = @()

# Doi ten cac file
$count = $files.Count
for ($i = 0; $i -lt $count; $i++) {
    $oldName = $files[$i].FullName
    $newName = Join-Path -Path $folderPath -ChildPath "de_$($i + 1).pdf"
    
    $oldBaseName = Split-Path -Leaf $oldName
    $newBaseName = Split-Path -Leaf $newName
    
    # Luu mapping (dung object)
    $mappings += @{
        "old" = $oldBaseName
        "new" = $newBaseName
    }
    
    # Doi ten file
    Rename-Item -Path $oldName -NewName $newName -Force
    Write-Host "OK $($i + 1). $oldBaseName -> $newBaseName"
}

Write-Host "`n=== Cap Nhat Link Trong HTML ===" -ForegroundColor Green

# Doc file HTML
$htmlContent = Get-Content $htmlFile -Raw -Encoding UTF8

# Thay the tung link
foreach ($mapping in $mappings) {
    $oldName = $mapping["old"]
    $newName = $mapping["new"]
    
    # Doi voi duong dan tieng Viet
    $oldPath = "đề/đề tiếng anh/" + $oldName
    $newPath = "đề/đề tiếng anh/" + $newName
    
    # Dung -replace voi regex escape
    $htmlContent = $htmlContent -replace [regex]::Escape($oldPath), $newPath
    
    Write-Host "OK: $oldName -> $newName"
}

# Ghi lai file HTML
Set-Content -Path $htmlFile -Value $htmlContent -Encoding UTF8

Write-Host "`nHoan tat!" -ForegroundColor Green
